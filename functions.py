import sys
import teachers
import nltk
nltk.download('punkt_tab')
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# from sentence_transformers import SentenceTransformer
# sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')


def train_model():
    sentences = ["I ate dinner.", "We had a three-course meal.", "Brad came to dinner with us.", "He loves fish tacos.",
                 "In the end, we all felt like we ate too much.", "We all agreed; it was a magnificent evening."]

    # Tokenization of each document
    tokenized_sent = []
    for s in sentences:
        tokenized_sent.append(nltk.word_tokenize(s.lower()))

    tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_sent)]

    model = Doc2Vec(tagged_data, vector_size=20, window=2, min_count=1, epochs=100)

    return model


# student has name, age, subject, gender, description
# teacher has name, age_range, gender, phone_num, description
def match_teacher(student):
    # filter the teachers that don't qualify - subject and age
    teachers_dt = teachers.load_data()
    print(teachers_dt)

    # filter the DataFrame
    mask = (
            teachers_dt['Age Range'].str.split('-').apply(
                lambda x: int(x[0]) <= int(student['Age']) <= int(x[1])
            )
            & (teachers_dt['Subject'] == student['Subject'])
    )

    # Apply the mask to filter teachers_dt
    teachers_dt = teachers_dt[mask]
    print(teachers_dt)

    teachers_descriptions = [str(desc) for desc in teachers_dt['Short Explanation']]
    student_description = str(student['Short Explanation'])

    # now match the best teacher for the student based on the short explanation
    # first tokenise all the descriptions
    tokenized_teacher_descriptions = [nltk.word_tokenize(desc.lower()) for desc in teachers_descriptions]
    tokenized_student_description = nltk.word_tokenize(student_description)  # sentence vector

    ## Train doc2vec model
    model = train_model()

    # transform sentence tokens to vectors using the model
    vectorized_teachers_description = [model.infer_vector(tokenized_sent) for tokenized_sent in tokenized_teacher_descriptions]
    vectorized_student_description = model.infer_vector(tokenized_student_description)

    # resetting parameters
    min_cosine_similarity = sys.maxsize
    teacher_match_index = -1

    # find the closest vectors
    for vector_i in range(len(vectorized_teachers_description)):
        cosine_similarity = cosine(vectorized_teachers_description[vector_i], vectorized_student_description)
        if cosine_similarity < min_cosine_similarity:
            min_cosine_similarity = cosine_similarity
            teacher_match_index = vector_i

    if teacher_match_index != -1:
        print(student)
        print(teachers_dt[teachers_dt['Short Explanation'] == teachers_descriptions[teacher_match_index]])
    else:
        print('could not match teacher')



# def get_cosine(vec1, vec2):
#     intersection = set(vec1.keys()) & set(vec2.keys())
#     numerator = sum([vec1[x] * vec2[x] for x in intersection])
#
#     sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
#     sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
#     denominator = math.sqrt(sum1) * math.sqrt(sum2)
#
#     if not denominator:
#         return 0.0
#     else:
#         return float(numerator) / denominator

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


# https://www.analyticsvidhya.com/blog/2020/08/top-4-sentence-embedding-techniques-using-python/
def create_student(name, age, subject, gender, description):
    student = {'Name': name, 'Age': age, 'Subject': subject, 'Gender': gender, 'Short Explanation': description}
    return student


student1 = create_student(name='Alex Johnson', age=14, subject='Math', gender='Male', description='struggles with geometry and functions')
match_teacher(student1)
