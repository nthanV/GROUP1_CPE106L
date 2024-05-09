''' 
File: student.py

* Program Description: For Project 2, using the code from program 1, 
we place several objects of the 'Student' class and place it in
a list. The list is then shuffled before being sorted. A print 
function is added before and after the sorting process to ensure that
the program did not use any fixed variables for the sorting process.

''' 
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
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    """METHOD 1"""
    def __eq__(self, student):
        return self.name == student.name

    """METHOD 2"""
    def __lt__(self, student):
        return self.name < student.name

    """METHOD 3"""
    def __ge__(self, student):
        return self.name >= student.name

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    print("\nFirst Student")
    student = Student("Kennrick", 5)

    for i in range(1, 6):
        student.setScore(i, 100-i)
    print(student)

    print("\nSecond Student")
    student2 = Student("Andrew", 5)

    for j in range(1, 6):
        student2.setScore(j, 95-j)
    print(student2)

    print("\nThird Student")
    student3 = Student("Ven", 5)

    for k in range(1, 6):
        student3.setScore(k, 90-k)
    print(student3)

    print("\nFourth Student")
    student4 = Student("Lance", 5)

    for l in range (1, 6):
        student4.setScore(l, 95-l)
    print(student4)

    print("\nFifth Student")
    student5 = Student("Stephen", 5)

    for m in range (1, 6):
        student5.setScore(m, 80-m)
    print(student5)
    
    
    s1 = student
    s2 = student2
    s3 = student3
    s4 = student4
    s5 = student5

    studentList = [s1, s2, s3, s4, s5]
    random.shuffle(studentList)
    print("\n\nBefore Sorting:")
    for i in range(0, len(studentList)):
        print(studentList[i], "\n")
    
    studentList.sort()
    print("\n\nAfter Sorting:")
    for i in range(0, len(studentList)):
        print(studentList[i], "\n")

if __name__ == "__main__":
    main()



