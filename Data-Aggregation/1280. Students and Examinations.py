import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
      return (pd.merge(students, subjects, how ='cross')
            .merge(examinations.groupby(['student_id','subject_name']).size()
            
            .reset_index(name = 'attended_exams'), how ='left', 
                         on = ['student_id','subject_name'])

            .sort_values(by = ['student_id','subject_name'])
            .fillna({'attended_exams':0}))