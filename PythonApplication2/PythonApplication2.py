import math
import data
import random




#takes users number of problems correct and how many problems there were and will calcuate their score. 
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







#wgrade = input("what is your desired grade?")


#total = input("How many problems total?")

#print(required_grade(total, wgrade))


# Quick sort algorithm takes piviot point in a list, and sorts by creating a new list and one by 
# one checks to see if the following number is larger or smaller than pivot point
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []
     
    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort(data.data_finder()))
#print(type(data.data_finder()))
#def random_gen(int):
    
 #   randomlist = random.sample(range(1, 99), 50)
  #  return randomlist

#ammount_numbers = input("how many random numbers would you like?")
#int(ammount_numbers)

#print(random_gen(ammount_numbers))



#def interfaces():
   
  #  list = {"john": 4, "ammy": 2}
  #  return list[1]





#print(interfaces)