'''
* Author's Name: Kyle Kenshin Morales  
* Group No.: 10
* Date: March 23, 2021
* Filename: MP_01.py
* Program Description:  Add three methods to the Student class that compare two Student objects. 
                        One method should test for equality. A second method should test for less 
                        than. The third method should test for greater than or equal to. In each 
                        case, the method returns the result of the comparison of the two students’ 
                        names. Include a main function that tests all of the comparison operators. 
''' 

"""
From File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self): 
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other): #FUNCTION 1
        """Returns the == Comparison of two student."""
        '''if (self.getAverage() == other.getAverage()) :
            print("Both Students Has The Same Average")
        else:
            print("Students' average grades are not equal")'''
        return self.name.lower() == other.name.lower()

    def __lt__(self, other): #FUNCTION 2
        """Returns the < Comparison of two student."""
        '''if (self.getAverage() < other.getAverage()) :
            print(self.getName() + " got lower average than " + other.getName())
        else:
            print(self.getName() + " did not get a lower average " + other.getName())'''   
        return self.name.lower() < other.name.lower()
    
    def __ge__(self, other):
        '''if (self.getAverage() >= other.getAverage()) :
            print(other.getName() + " did not get a higher average than " + self.getName())  
        else:
             print(other.getName() + " got a higehr average " + self.getName())'''  
        return self.name.lower() >= other.name.lower()


def main():
    """A simple test."""
    amount = int(input("Please Enter Amount of Scores to be Inputted: "))
    student1 = Student(input("Please Enter Student 1 Name: "), amount)
    student2 = Student(input("Please Enter Student 2 Name: "), amount)

    print("Student 1 and 2 created with default values")
    print(student1)
    print(student2)

    for i in range(amount):
        student1.setScore(i+1, int(input("Please enter " + student1.getName() + "'s score " + str(i+1) + ": ")))
    for i in range(amount):
        student2.setScore(i+1, int(input("Please enter " + student2.getName() + "'s score " + str(i+1) + ": ")))
        
    print("Names Are The Same:", student1 == student2)
    print("S2 goes later than S1: ", student1 < student2)
    print("S2 doesn't go later than S1: ", student1 >= student2)

if __name__ == "__main__":
    main()


