# Usando a técnica de compreensão de dicionário (Simples)
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Modelo: students_score = {new_key:new_value for item in list}
# Aqui será gerado notas aleatórias para cada estudante
students_score = {students: random.randint(1, 100) for students in names}
print(students_score)


# Usando a técnica de compreensão de dicionário (Completa)
# Aqui será gerado um dicionário apenas com os alunos que passaram.
# Modelo: passed_students = {key:value for (key, value) in dict.items() if test}
passed_students = {students: score for (students, score) in students_score.items() if score >= 60}
print(passed_students)
