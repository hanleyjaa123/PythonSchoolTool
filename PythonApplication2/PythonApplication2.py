import math
import data
#import random




#takes users number of problems correct and how many problems there  was and will calcuate their score. 
def gradecal(grade, total):
   multi = int(grade) / int(total) 
   awnsr = multi * 100
   return awnsr



 # takes the total problems in a test and your desired grade for the test, then calcuates how many questions you need to get correct to receive the grade you want. 
def required_grade(total, wgrade):
     sum = int(wgrade) * int(total)
     aws = sum / 100
     return aws
 
 
# Main menu, user selection of tools  
print("School Tools")
print("1. Grade Cal - takes users number of problems they got correct and how many problems there were total and will calcuate their score. ")
print("2. Required Grade - takes the total problems in a test and your desired grade for the test, then calcuates how many questions you need to get correct to receive the grade you want. ")

userinput = input("What would you like to do?")





if userinput == "1":
        grade = input("How many problems did you get correct?")

        total = input("How many problems total?")
        print(gradecal(grade, total))
elif userinput == "2":
    wgrade = input("what is your desired grade?")
    total = input("How many problems total?")
    print(required_grade(total, wgrade))
else:
    print("that is not an option")








