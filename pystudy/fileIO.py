"""
Part 1: Read file and create dictionary
Write a function named create_grades_dict that accepts a string as the name of a file.
Assuming that the file is a text file which includes name and grades of students,
your function should read the file and return a dictionary with the exact format as shown below:

The format of the input file is:
Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
....

An example of the input file is shown below.
Sample Input
Assuming that the input file "student_grades.txt" contains the following text:
1000123456, Rubble, Test_3,  80, Test_4 , 80
1000123459, Chipmunk, Test_4, 96, Test_1, 86 , Quiz_1 , 88

Notes:
1)Items are separated by comma and one or more spaces may exist between the items.
2)The "ID" of each student is unique. Two students may have the same Name (but IDs will be different);
3)The "Name" of each student will only include a last name with no punctuation. Maximum of 15 characters.
4)There will be an integer grade for each test (0-100)
5)There are only four valid tests, i.e. Test_1, Test_2, Test_3, Test_4.
There may be other grades in the file and you should ignore those grades.
6)Each student may have missing grade(s) for the tests.A missing grades should be considered as 0.
7)Grades may not be in order i.e. Test_3 may appear before Test_1.

Your function should read the input file, calculate the average test grade for each student and
return a dictionary with the following format:
{'Student_ID':[Last_name,Test_1_grade,Test_2_grade,Test_3_grade,Test_4_grade,average], ...}

For example in the case of sample input file shown above,your function should return the following dictionary:
{'1000123456': ['Rubble', 0, 0, 80, 80, 40.0],
'1000123459': ['Chipmunk', 86, 0, 0, 96, 45.5]}
"""


# Type your code here
def create_grades_dict(filename):
    file = open(filename, "r")
    stu_dict ={}
    student = file.readline().strip()
    while student:
        student = student.replace(" ","")
        stu_list = student.split(",")
        stu_dict[stu_list[0]]=[stu_list[1]]
        for i in range(1,5,1):
            test = "Test_"+str(i)
            if  test in stu_list:
                index = stu_list.index(test)+1
                stu_dict[stu_list[0]].append(int(stu_list[index]))
            else:
                stu_dict[stu_list[0]].append(0)
        student = file.readline().strip()
    for (key, value) in stu_dict.items():
        sum = 0
        for i in range(1, len(value), 1):
            sum += value[i]
        avg = sum / 4
        stu_dict[key].append(avg)
    return stu_dict

print(create_grades_dict("name_grade.txt"))


def print_grades(filename):
    stu_dic = create_grades_dict(filename)
    print(
        " " * 4 + "ID" + " " * 4 + " | " + " " * 6 + "Name" + " " * 6 + " | " + "Test_1" + " | " + "Test_2" + " | " + "Test_3" + " | " + "Test_4" + " | " + " Avg. " + " | ")
    ID = []
    for key in stu_dic:
        ID.append(int(key))
    ID.sort()
    for i in ID:
        i = str(i)
        print(i + " | " + stu_dic[i][0].ljust(16)+" | "+str(stu_dic[i][1]).rjust(6)+ " | " + str(stu_dic[i][2]).rjust(6)+ " | " + str(stu_dic[i][3]).rjust(6)+ " | " + str(stu_dic[i][4]).rjust(6)+" | " + str(stu_dic[i][5]).rjust(6)+" | ")


print_grades("name_grade.txt")