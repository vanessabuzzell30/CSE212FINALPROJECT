
def group(group1, student_turnedin_assignments):
    # find out what students are in  group1 turned in there  assinments
    pass


def notgroup(students, group1, student_turnedin_assignments):
    # find out what students are not in  group1 but also did not turn in assinments.
    pass


def found(student_turnedin_assignments, name):
  # if a student has turned in there  assinment print it is found!
    pass


students = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
s = students
group1 = ['April', 'John', 'Corey']
g = group1
student_turnedin_assignments = ['Judy', 'Corey', 'Steven', 'Jane', 'April']
sta = student_turnedin_assignments
print("----------")
print(group(g, sta))  # {'April', 'Corey'}
print("----------")
print(notgroup(s,  g, sta))  # {'Jim', 'Jenn'}
print("----------")
print(found(sta, "Corey"))  # Found!
print("----------")
# O(n) for list
# O(1) for a set
