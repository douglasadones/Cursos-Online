student_dict = {
    "student": ["Angela", "James", "Lily"],
    "scores": [56, 76, 98],
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)  # Todos os estudantes
    print(row.scores)  # Todas as notas
    if row.student == "Angela":
        print(row.scores)  # Nota da Angela
