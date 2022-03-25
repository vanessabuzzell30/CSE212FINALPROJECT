def group(group1, student_turnedin_assignments):
    # find out what students are in  group1 turned in there  assinments
    result = set(group1).intersection(student_turnedin_assignments)
    print(result)


def notgroup(students, group1, student_turnedin_assignments):
    # find out what students are not in  group1 but also did not turn in assinments.
    result = set(students).difference(group1, student_turnedin_assignments)
    print(result)


def found(student_turnedin_assignments, name):
  # if a student has turned in there  assinment print it is found!
    if name in student_turnedin_assignments:
        print('Found!')


students = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
s = students
group1 = ['April', 'John', 'Corey']
g = group1
student_turnedin_assignments = ['Judy', 'Corey', 'Steven', 'Jane', 'April']
sta = student_turnedin_assignments
print("----------")
print(group(g, sta))
print("----------")
print(notgroup(s,  g, sta))
print("----------")
print(found(sta, "Corey"))
print("----------")
# O(n) for list
# O(1) for a set
