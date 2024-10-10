import teachers
import numpy as np
from sentence_transformers import SentenceTransformer
sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')


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

    vectorized_teachers_descriptions = [sbert_model.encode(desc) for desc in teachers_descriptions]
    vectorized_student_description = sbert_model.encode(student_description)

    # resetting parameters
    min_cosine_similarity = -1
    teacher_match_index = -1

    # find the closest vectors
    for vector_i in range(len(vectorized_teachers_descriptions)):
        cosine_similarity = cosine(vectorized_student_description, vectorized_teachers_descriptions[vector_i])
        if cosine_similarity > min_cosine_similarity:
            min_cosine_similarity = cosine_similarity
            teacher_match_index = vector_i

    if teacher_match_index != -1:
        print(student)
        matched_teacher = teachers_dt[teachers_dt['Short Explanation'] == teachers_descriptions[teacher_match_index]].head(2)
        return matched_teacher

    else:
        print('could not match teacher')
        return None


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

def create_student(name, age, subject, gender, description):
    student = {'Name': name, 'Age': age, 'Subject': subject, 'Gender': gender, 'Short Explanation': description}
    return student

# student1 = create_student(name='Alex Johnson', age=14, subject='Math', gender='Male',
#                           description='struggles with geometry and functions')
# print(match_teacher(student1))

# https://www.analyticsvidhya.com/blog/2020/08/top-4-sentence-embedding-techniques-using-python/
# it works yippie