import sys
from teachers import teachers_df
import nltk
import math


# student has name, age, subject, gender, description
# teacher has name, age_range, gender, phone_num, description
def match_student(student):
    # filter the teachers that don't qualify - subject and age
    teachers_dt = teachers_df.copy()
    teachers_dt = teachers_dt[teachers_dt['subject'] == student['subject']]
    teachers_dt = teachers_dt[
        teachers_dt['age_range'].split('-')[0] <= student['age'] and teachers_dt['age_range'].split('-')[1] >= student[
            'age']]

    # by the description decide the most fitting teacher
    teacher_descriptions_tokens = [nltk.word_tokenize(desc) for desc in teachers_dt['description']]

    student_description_tokens = nltk.word_tokenize(student['description'])  # sentence vector
    min_cosine_similarity = sys.maxsize
    teacher_match_index = 0

    for tokens_i in range(len(teacher_descriptions_tokens)):
        cosine_similarity = get_cosine(student_description_tokens, teacher_descriptions_tokens[tokens_i])
        if cosine_similarity < min_cosine_similarity:
            min_cosine_similarity = cosine_similarity
            teacher_match_index = tokens_i

    return teachers_dt[teacher_match_index]


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator
