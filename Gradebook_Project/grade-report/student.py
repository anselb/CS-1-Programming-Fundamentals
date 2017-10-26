"""Students Object File."""
import classroom

class Student(object):
    """The Student Object."""

    students = []

    def __init__(self, name):
        """Take a name(String)"""
        self.name = name
        self.assignments = {}
        Student.students.append(self)
        classroom.Classroom.classObj.roster.append(self.name)

    def createStudent():
        addAnother = ""
        while not addAnother == 'n':
            studentName = input("What is the New Student's Name: ")
            newStudent = Student(studentName)
            addAnother = input("Would you like to add another student(y/n): ")

    def removeStudent():
        """Remove a Student from the Classroom."""
        for i, studentName in enumerate(classroom.Classroom.classObj.roster):
            print(str(i) + ". " + studentName)
        studentRes = input("Select a Student to Remove: ")
        classroom.Classroom.classObj.roster.pop(int(studentRes))
        Student.students.pop(int(studentRes))

    def addAssToEachStudent(name):
        """Add the Assignment to each student."""
        for student in Student.students:
            student.assignments[name] = "Not Graded"
            print(student.assignments[name])

    def removeAssToEachStud(name):
        """Remove the Assignment from each Student."""
        for student in Student.students:
            del student.assignments[name]
