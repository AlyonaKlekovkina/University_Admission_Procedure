# write your code here
from collections import namedtuple


def get_students_list():
    file = open('applicants.txt', 'r')
    students = []
    for student in file:
        student = student.split()
        student = student[0:2] + [float(student[2])] + [float(student[3])] + [float(student[4])] + [float(student[5])] + student[6:]
        students.append(student)
    file.close()
    return students


def first_priority_calculation(sorted_students, iteration):
    calculated_mean_score_list = []
    for i in sorted_students:
        score = ''
        name = i[0]
        last_name = i[1]
        physics_score = i[2]
        chemistry_score = i[3]
        math_score = i[4]
        compscience_score = i[5]
        the_priority = i[iteration]
        if the_priority == 'Physics':
            score = (physics_score + math_score) / 2
        if the_priority == 'Chemistry':
            score = chemistry_score
        if the_priority == 'Mathematics':
            score = math_score
        if the_priority == 'Engineering':
            score = (compscience_score + math_score) / 2
        if the_priority == 'Biotech':
            score = (chemistry_score + physics_score) / 2
        person = [name, last_name, physics_score, chemistry_score, math_score, compscience_score, i[6], i[7], i[8], score]
        calculated_mean_score_list.append(person)
    return calculated_mean_score_list


def first_priority(list_of_students, number_to_accept, iter, biotech, chemistry, engineering, mathematics, physics):
    to_remove = []
    sorted_students = sorted(list_of_students, key=lambda x: (-x[9], x[0]))
    for i in sorted_students:
        priority = i[iter]
        if priority == 'Biotech' and len(biotech) < number_to_accept:
            biotech.append(i)
            to_remove.append(i)
        if priority == 'Chemistry' and len(chemistry) < number_to_accept:
            chemistry.append(i)
            to_remove.append(i)
        if priority == 'Mathematics' and len(mathematics) < number_to_accept:
            mathematics.append(i)
            to_remove.append(i)
        if priority == 'Engineering' and len(engineering) < number_to_accept:
            engineering.append(i)
            to_remove.append(i)
        if priority == 'Physics' and len(physics) < number_to_accept:
            physics.append(i)
            to_remove.append(i)

    return biotech, chemistry, engineering, mathematics, physics, to_remove


def remove_accepted_students(list_of_students, list_to_remove):
    clean_list = []
    for i in list_of_students:
        if i not in list_to_remove:
            clean_list.append(i)
    return clean_list


def form_a_list(n_students):
    global initital_list
    biotech = []
    chemistry = []
    engineering = []
    mathematics = []
    physics = []
    for i in range(6, 9):
        print(len(initital_list))
        first_iteration_sort = first_priority_calculation(initital_list, i)
        initital_list = first_iteration_sort
        first_distribution = first_priority(initital_list, n_students, i, biotech, chemistry, engineering,
                                            mathematics, physics)
        list_to_remove = first_distribution[5]
        print(len(list_to_remove))
        initital_list = remove_accepted_students(initital_list, list_to_remove)
        print(len(initital_list))
    return biotech, chemistry, engineering, mathematics, physics


n_students = int(input())
initital_list = get_students_list()
accepted_students = form_a_list(n_students)
biotech_students = sorted(accepted_students[0], key=lambda x: (-x[9], x[0]))
chemistry_students = sorted(accepted_students[1], key=lambda x: (-x[9], x[0]))
engineering_students = sorted(accepted_students[2], key=lambda x: (-x[9], x[0]))
mathematics_students = sorted(accepted_students[3], key=lambda x: (-x[9], x[0]))
physics_students = sorted(accepted_students[4], key=lambda x: (-x[9], x[0]))

print('Biotech')
with open("biotech.txt", "w") as f:
    for i in biotech_students:
        string = str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[9])
        print(string)
        f.write(string)
        f.write('\n')
print()
print('Chemistry')
with open("chemistry.txt", "w") as f:
    for i in chemistry_students:
        string = str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[9])
        print(string)
        f.write(string)
        f.write('')
        f.write('\n')
print()
print('Engineering')
with open("engineering.txt", "w") as f:
    for i in engineering_students:
        string = str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[9])
        print(string)
        f.write(string)
        f.write('\n')
print()
print('Mathematics')
with open("mathematics.txt", "w") as f:
    for i in mathematics_students:
        string = str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[9])
        print(string)
        f.write(string)
        f.write('\n')
print()
print('Physics')
with open("physics.txt", "w") as f:
    for i in physics_students:
        string = str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[9])
        print(string)
        f.write(string)
        f.write('\n')
