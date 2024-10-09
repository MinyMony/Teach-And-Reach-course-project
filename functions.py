import pandas as pd
from teachers import teachers_df

# student has name, age, subject, gender, description
# teacher has name, age_range, gender, phone_num, description
def match_it(student):
    # filter the teachers that don't qualify - subject and age
    teachers_dt = teachers_df.copy()
    teachers_dt = teachers_dt[teachers_dt['subject'] == student['subject']]
    teachers_dt = teachers_dt[teachers_dt['age_range'].split('-')[0] <= student['age'] and teachers_dt['age_range'].split('-')[1] >= student['age']]

    # by the description decide the most fitting teacher
