import pandas as pd
import pygame

# Creating a DataFrame for teachers
teachers_data = {
    'Full Name': ['Miriam Cohen', 'Yossi Levi', 'Dana Friedman', 'Oren Mizrahi', 'Shachar Rabinowitz',
                  'Ravit Avraham', 'Itai Shuster', 'Maayan Barak', 'Noa Alon', 'Daniel Golan'],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
    'Subject': ['Math', 'Science', 'Literature', 'History', 'Geography', 'Art', 'Music', 'Physics', 'Chemistry',
                'Biology'],
    'Age Range': ['10-15', '12-18', '10-17', '15-20', '11-16', '8-14', '12-19', '13-18', '10-15', '9-16'],
    'Phone Number': [
        '050-1234567', '050-2345678', '050-3456789', '050-4567890', '050-5678901',
        '050-6789012', '050-7890123', '050-8901234', '050-9012345', '050-0123456'
    ],
    'Short Explanation': [
        'Algebra, geometry, and problem-solving techniques.',
        'Biology, chemistry, and hands-on experiments.',
        'Poetry analysis, creative writing, and literary theory.',
        'World history, significant events, and cultural impacts.',
        'Physical geography, human geography, and environmental studies.',
        'Drawing, painting, and art history.',
        'Music theory, composition, and instrumental practice.',
        'Classical mechanics, electricity, and thermodynamics.',
        'Organic chemistry, reactions, and lab safety.',
        'Ecology, evolution, and human biology.'
    ]
}

teachers_df = pd.DataFrame(teachers_data)

teachers_df.to_csv('teachers_data.csv', index=False)

def addTeachers(full_name, gender, subject, age_range, phone_number, short_explanation):
    teachers_df['Full Name'].append(full_name)
    teachers_df['Gender'].append(gender)
    teachers_df['Subject'].append(subject)
    teachers_df['Age Range'].append(age_range)
    teachers_df['Phone Number'].append(phone_number)
    teachers_df['Short Explanation'].append(short_explanation)
    return teachers_df

def screen_after_teacher():
    pygame.display.set_caption('The details you entered have been added to the database!')
    screen.fill(consts.BORDER_COLOR)
    pygame.display.flip()
