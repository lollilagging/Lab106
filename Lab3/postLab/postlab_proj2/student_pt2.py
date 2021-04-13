"""
* Author's Name: Jemuel Dane K. Martinez, Seth T. Dayao
* Group No.: 11
* Date: 3/25/2021
* Filename: MP2_Group11.py
* Program Description: This problem assumes that you have completed Problem 1. Place several Student objects 
                       into a list and shuffle it. Then run the sort method with this list and display all of the 
                       students’ information.

"""
import random

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
 
    # def __str__(self):
    #     """Returns the string representation of the student."""
    #     return "Name: " + self.name  + "\nScores: " + \
    #            " ".join(map(str, self.scores))

    def __str__(self):
        return '(' + self.name + ', ' + self.scores + ')'

    def __eq__(self, other):
        return self.name == other.name

    def __ge__(self, other):
        return self.name >= other.name
        
    def __lt__(self, other):
        return self.name < other.name

def main():
    student = [
        Student("Carlo", 5),
        Student("James", 7),
        Student("Jemuel", 2),
        Student("Seth", 4)
        ]
    random.shuffle(student)
    print ("Student info shuffled!")
    for i in range(len(student)):
        print ("Student name:", student[i].getName())
        print ("Scores: ")
        for count, value in enumerate(student[i].scores):
            print (count, value)
        print("")
    
    list.sort(student)
    print ("Student info sorted!")
    for i in range(len(student)):
        print ("Student name: ", student[i].getName())
        print ("Scores: ")
        for count, value in enumerate(student[i].scores):
            print (count, value)
        print ("")

    
if __name__ == "__main__":
    main()




