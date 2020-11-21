class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, testscores):
        super().__init__(firstName, lastName, idNumber)
        self.testscores = testscores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        totalscore = 0
        
        for testscore in self.testscores:
            totalscore += testscore
        averagescore = totalscore/len(self.testscores)
        
        if 90 <= averagescore <= 100:
            return 'O'
        elif 80 <= averagescore < 90:
            return 'E'
        elif 70 <= averagescore < 80:
            return 'A'
        elif 55 <= averagescore < 70:
            return 'P'
        elif 40 <= averagescore < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
