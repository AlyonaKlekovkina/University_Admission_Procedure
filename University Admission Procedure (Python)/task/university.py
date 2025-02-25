# write your code here


def get_students_list():
    file = open('applicants.txt', 'r')
    students = []
    for student in file:
        student = student.split()
        student = student[0:2] + [float(student[2])] + [float(student[3])] + [float(student[4])] + [float(student[5])] + student[6:]
        students.append(student)
    file.close()
    return students


def sort_by_scores(list_of_students, number_to_accept, priority_iteration, biotech, chemistry, engineering, mathematics, physics):
    sorted_students = sorted(list_of_students, key=lambda x: (-x[2], x[0], x[1]))
    to_remove = []
    for i in sorted_students:
        if i[priority_iteration] == 'Physics' and len(physics) < number_to_accept:
            physics.append(i)
            to_remove.append(i)

    sorted_students = sorted(list_of_students, key=lambda x: (-x[3], x[0], x[1]))
    for i in sorted_students:
        if i[priority_iteration] == 'Chemistry' and len(chemistry) < number_to_accept:
            chemistry.append(i)
            to_remove.append(i)

    sorted_students = sorted(list_of_students, key=lambda x: (-x[4], x[0], x[1]))
    for i in sorted_students:
        if i[priority_iteration] == 'Mathematics' and len(mathematics) < number_to_accept:
            mathematics.append(i)
            to_remove.append(i)

    sorted_students = sorted(list_of_students, key=lambda x: (-x[5], x[0], x[1]))
    for i in sorted_students:
        if i[priority_iteration] == 'Engineering' and len(engineering) < number_to_accept:
            engineering.append(i)
            to_remove.append(i)

    sorted_students = sorted(list_of_students, key=lambda x: (-x[3], x[0], x[1]))
    for i in sorted_students:
        if i[priority_iteration] == 'Biotech' and len(biotech) < number_to_accept:
            biotech.append(i)
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
    for i in range(6, 9):
        interative_sort = sort_by_scores(sorted_students, n_students, i, biotech, chemistry, engineering, mathematics, physics)
        students_to_remove = interative_sort[5]
        sorted_students = remove_accepted_students(sorted_students, students_to_remove)
    return biotech, chemistry, engineering, mathematics, physics


n_students = int(input())
sorted_students = get_students_list()
accepted_students = form_a_list(n_students)
biotech_students = sorted(accepted_students[0], key=lambda x: (-x[3], x[0], x[1]))
chemistry_students = sorted(accepted_students[1], key=lambda x: (-x[3], x[0], x[1]))
engineering_students = sorted(accepted_students[2], key=lambda x: (-x[5], x[0], x[1]))
mathematics_students = sorted(accepted_students[3], key=lambda x: (-x[4], x[0], x[1]))
physics_students = sorted(accepted_students[4], key=lambda x: (-x[2], x[0], x[1]))

print('Biotech')
for i in biotech_students:
    print(i[0], i[1], i[3])
print()
print('Chemistry')
for i in chemistry_students:
    print(i[0], i[1], i[3])
print()
print('Engineering')
for i in engineering_students:
    print(i[0], i[1], i[5])
print()
print('Mathematics')
for i in mathematics_students:
    print(i[0], i[1], i[4])
print()
print('Physics')
for i in physics_students:
    print(i[0], i[1], i[2])
