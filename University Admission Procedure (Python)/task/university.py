# write your code here
n_applicantis = int(input())
m_accepted = int(input())
names = []
while n_applicantis > 0:
    name = input().split()
    name[2] = float(name[2])
    names.append(name)
    n_applicantis -= 1
print('Successful applicants:')
sorted_names = sorted(names, key=lambda x: x[2], reverse = True)
for i in range(m_accepted):
    name = sorted_names[i][0]
    last_name = sorted_names[i][1]
    print(name, last_name)
