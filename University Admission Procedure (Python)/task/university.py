# write your code here


def get_students_list():
    file = open('applicants.txt', 'r')
    students = []
    for student in file:
        student = student.split()
        student = student[0:2] + [float(student[2])] + student[3:]
        students.append(student)
    file.close()
    return sorted(students, key=lambda x: (-x[2], x[0]))


def first_priority(list_of_students, number_to_accept, priority_iteration, biotech, chemistry, engineering, mathematics, physics):
    to_remove = []
    for i in list_of_students:
        priority = i[priority_iteration]
        if priority == 'Biotech' and len(biotech) < number_to_accept:
            biotech.append(i)
            to_remove.append(i)
        if priority == 'Chemistry' and len(chemistry) < number_to_accept:
            chemistry.append(i)
            to_remove.append(i)
        if priority == 'Engineering' and len(engineering) < number_to_accept:
            engineering.append(i)
            to_remove.append(i)
        if priority == 'Mathematics' and len(mathematics) < number_to_accept:
            mathematics.append(i)
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
    global sorted_students
    biotech = []
    chemistry = []
    engineering = []
    mathematics = []
    physics = []
    for i in range(3, 6):
        first_priority_sort = first_priority(sorted_students, n_students, i, biotech, chemistry, engineering, mathematics, physics)
        students_to_remove = first_priority_sort[5]
        sorted_students = remove_accepted_students(sorted_students, students_to_remove)
    return biotech, chemistry, engineering, mathematics, physics


n_students = int(input())
sorted_students = get_students_list()
accepted_students = form_a_list(n_students)
biotech_students = sorted(accepted_students[0], key=lambda x: (-x[2], x[0]))
chemistry_students = sorted(accepted_students[1], key=lambda x: (-x[2], x[0]))
engineering_students = sorted(accepted_students[2], key=lambda x: (-x[2], x[0]))
mathematics_students = sorted(accepted_students[3], key=lambda x: (-x[2], x[0]))
physics_students = sorted(accepted_students[4], key=lambda x: (-x[2], x[0]))

print('Biotech')
for i in biotech_students:
    print(i[0], i[1], i[2])
print()
print('Chemistry')
for i in chemistry_students:
    print(i[0], i[1], i[2])
print()
print('Engineering')
for i in engineering_students:
    print(i[0], i[1], i[2])
print()
print('Mathematics')
for i in mathematics_students:
    print(i[0], i[1], i[2])
print()
print('Physics')
for i in physics_students:
    print(i[0], i[1], i[2])
