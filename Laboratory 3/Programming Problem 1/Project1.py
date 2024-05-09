''' 
File: student.py

* Program Description: For Project 1, three new methods were added to this class:
 (1)To test for equality, (2) To test for less than, and (3)To test for greater
 than or equal to. Moreover, a main function was added to test all the said opeartors.

''' 

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

    print("\nChecking if student1 is equal to student2")
    print(student.__eq__(student2))

    print("\nChecking if student1 is less than student2")
    print(student.__lt__(student2))

    print("\nChecking if student1 is greater than or equal to student2")
    print(student.__ge__(student2))

    print("\nChecking if student1 is equal to student3")
    print(student.__eq__(student3))

    print("\nChecking if student1 is less than student3")
    print(student.__lt__(student3))

    print("\nChecking if student1 is greater than or equal to student3")
    print(student.__ge__(student3))

if __name__ == "__main__":
    main()



