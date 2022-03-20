

import pytest
import Professor
import System
import Staff
import Student
import TA
import User

profUser = 'goggins'
profPass = 'augurrox'
profUser2 = 'saab'
username = 'akend3'
username2 = 'hdjsr7'
assignment = 'assignment1'
assignment2 = 'assignment2'
course = 'comp_sci'
course2 = 'cloud_computing'
submission = 'Sheeeesh'

#pass
def test_login(grading_system):
    users = grading_system.users
    grading_system.login(profUser,profPass)
    grading_system.__init__()
    if users[profUser]['role'] != 'professor':
        assert False
#pass
def test_check_password(grading_system):
    test = grading_system.check_password(profUser,profPass)
    test2 = grading_system.check_password(profUser,'#yeet')
    test3 = grading_system.check_password(profUser,'#YEET')
    if test == test2 or test == test3:
        assert False
    if test != test2:
        assert True

#fail
def test_change_grade(grading_system):
    grade = 90
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser,users,courses)
    professor.change_grade(username, course, assignment, grade)

    if users[username]['courses'][course][assignment]['grade'] != grade:
        assert False
#pass
def test_create_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser, users, courses)
    professor.create_assignment('assignment4', '04/09/20', 'databases')


    if courses['databases']['assignments']['assignment4']['due_date'] != '04/09/20':
        assert False
#fail
def test_add_student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser,users,courses)
    professor.add_student(username, 'software_engineering')

    for key in users:
        if users[username]['courses'][course] != 'software_engineering':
            assert False

#pass
def test_drop_student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser2, users, courses)
    professor.drop_student(username, 'comp_sci')
    student = users[username]['courses']
    if 'comp_sci'  in student:
        assert False
#fail
def test_submit_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username, users, courses)
    student.submit_assignment(course, assignment,submission, '3/3/22')

    for key in users:
        if users[username]['courses'][course][assignment]['submission'] == submission:
            assert True
#fail
def test_check_ontime(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username, users, courses)
    
    if student.check_ontime('01/10/20', '01/07/20') or not student.check_ontime('01/06/20', '01/07/20'):
        assert False
# fail this fails because the value should be 23 and we are checking to see if the value stored is correct by checking if the value is 44
# so it should fail. 
def test_check_grades(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username, users, courses)
    grade = student.check_grades('databases')

    if grade[0] != ['assignment1', 44]:
        assert False
#pass
def test_view_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username, users, courses)
    assignments = student.view_assignments('databases')

    if assignments[0] == ['assignment1', '1/5/20']:
        assert True
# Fail this fails because the student is not enrolled in comp_sci class so he/she should not be able to view
# grades for that class they are not a part of.
def test_check_grade_extra1(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username2, users, courses)
    grade = student.check_grades('comp_sci')

    if grade[0] != ['assignment1',44]:
        assert False
# Fail this student is not in comp_sci class and shouldnt be able to view an assignment from a comp_sci class
def test_view_assignment_extra2(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student =Student.Student(username2, users, courses)
    assignments = student.view_assignments('comp_sci')
    if assignments[0] != ['assignment1', '1/5/20']:
        assert False

# Fail this Student is not in comp_sci so the professor should not be able to drop the student which it shows that because it failed
# meaning the professor cannot drop the student 
def test_drop_student_extra3(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser2, users, courses)
    professor.drop_student(username2, 'comp_sci')
    student = users[username2]['courses']
    if 'comp_sci'  in student:
        assert False

# Fail the password for this user is correct but there is whitespace in the front which shows
# that it handles that issue.
def test_check_passwordextra4(grading_system):
    proftest = grading_system.check_password(profUser,'  augurrox')
    if not proftest:
        assert False
# Fail this fails because it shows that the professor is not in the comp_sci course meaning he should not be able to access anything related to that course. 
def test_check_professor_teaching_extra5(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser, users, courses)
    
    if courses['comp_sci'] not in professor.courses:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


    