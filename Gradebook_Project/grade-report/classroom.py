"""Classroom Class."""
import student

class Classroom(object):
    """The Classroom Object."""

    classObj = {}

    def __init__(self, name, meetingTime):
        """Take a name(String) and a meetingTime(Dictionary)."""
        self.name = name
        self.meetingTime = meetingTime
        self.roster = []
        self.assignmentNames = []
        Classroom.classObj = self

    def createClassroom():
        """Create a new Classroom for the Professor to work with."""
        name = input("What is the name of your classroom: ")
        print("What times does your class meet at? (ex: hh:mm(am/pm) or "
              "<n> for no class)")
        timeDic = {}
        timeDic['m'] = input("Monday: ")
        timeDic['t'] = input("Tuesday: ")
        timeDic['w'] = input("Wednesday: ")
        timeDic['th'] = input("Thursday: ")
        timeDic['f'] = input("Friday: ")
        newClass = Classroom(name, timeDic)

    def showRoster():
        """Get Students of the Class."""
        for studentName in Classroom.classObj.roster:
            print(studentName)

    def addAssignment():
        """Add an assignment to the class."""
        nameRes = input("What is the name of your assignment: ")
        Classroom.classObj.assignmentNames.append(nameRes)
        student.Student.addAssToEachStudent(nameRes)

    def removeAssignment():
        """Remove an assignment from a class."""
        for i, name in enumerate(Classroom.classObj.assignmentNames):
            print(str(i)+". " + name)
        removeRes = input("Select an Assignment to remove:")
        student.Student.removeAssToEachStud(Classroom.classObj.assignmentNames[int(removeRes)])
        Classroom.classObj.assignmentNames.pop(int(removeRes))

    def assignGrades():
        for i, assName in enumerate(Classroom.classObj.assignmentNames):
            print(str(i) + ". " + assName)
        assNameRes = input("Select an Assignment to Grade: ")
        print("====" + Classroom.classObj.assignmentNames[int(assNameRes)] + "====")
        print("Grade from 0-100")
        for thisStudent in student.Student.students:
            gradeRes = (input(thisStudent.name + ": "))
            thisStudent.assignments[Classroom.classObj.assignmentNames[int(assNameRes)]] = gradeRes

    def makeLetterGrade(gradeNum):
        if not gradeNum == "Not Graded":
            if int(gradeNum) >= 90:
                return "A"
            elif int(gradeNum) >= 80:
                return "B"
            elif int(gradeNum) >= 70:
                return "C"
            elif int(gradeNum) >= 60:
                return "D"
            else:
                return "F"
        else:
            return "N/A"

    def getAverageGrade(assName):
        sum = 0
        for thisStudent in student.Student.students:
                if not thisStudent.assignments[assName] == "Not Graded":
                    sum = sum + int(thisStudent.assignments[assName])
                else:
                    sum = sum + 0
        return sum / len(student.Student.students)

    def viewGrades():
        for i, assName in enumerate(Classroom.classObj.assignmentNames):
            print(str(i) + ". " + assName)
        assNameRes = input("Select an Assignment to View Grades for: ")
        selectedAssName = Classroom.classObj.assignmentNames[int(assNameRes)]
        print("Grades for " + selectedAssName + ": ")
        for thisStudent in student.Student.students:
            print(thisStudent.name + " : " + Classroom.makeLetterGrade(thisStudent.assignments[selectedAssName]))
        print("Average Grade: " + str(Classroom.getAverageGrade(selectedAssName)) + " | " + Classroom.makeLetterGrade(Classroom.getAverageGrade(selectedAssName)))

    def showClassMenu():
        """Show Options for the Chosen Classroom."""
        menuShow = True
        while(menuShow):
            print("\n")
            print("===="+Classroom.classObj.name+"====")
            print("1. Add Student")
            print("2. Add Assignment")
            print("3. Remove Student")
            print("4. Remove Assignment")
            print("5. View Roster")
            print("6. Assign Grades")
            print("7. View Grades")
            print("<x> Exit "+Classroom.classObj.name)
            print("\n")
            commandNotEntered = True
            while(commandNotEntered):
                classMenuRes = input("Enter Command: ").lower()
                # Add Student
                if(classMenuRes == "1"):
                    commandNotEntered = False
                    student.Student.createStudent()
                # Add Assignment
                elif(classMenuRes == "2"):
                    commandNotEntered = False
                    Classroom.addAssignment()
                # Remove Student
                elif(classMenuRes == "3"):
                    commandNotEntered = False
                    student.Student.removeStudent()
                # Remove Assignment
                elif(classMenuRes == "4"):
                    commandNotEntered = False
                    Classroom.removeAssignment()
                # Show Roster
                elif(classMenuRes == "5"):
                    commandNotEntered = False
                    Classroom.showRoster()
                # Assign Grades to Students
                elif(classMenuRes == "6"):
                    commandNotEntered = False
                    Classroom.assignGrades()
                elif(classMenuRes == "7"):
                    commandNotEntered = False
                    Classroom.viewGrades()
                # Exit Classroom
                elif(classMenuRes == "x"):
                    print("Have a good day, Professor!")
                    return 0
