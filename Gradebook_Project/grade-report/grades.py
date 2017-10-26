"""Gradebook File."""
import classroom
import student

def main():
    """Start all the functions that are needed in the program."""
    print("Hello Professor, let's make a new classroom!")
    classroom.Classroom.createClassroom()
    classroom.Classroom.showClassMenu()

main()
