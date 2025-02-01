# a higher order function is a function that takes one or more functions as arguments or returns a function as a result.
# a lambda function is an anonymous function that can take any number of arguments and return any type of value.

from calendar import c
import math

x = lambda a,b,c : a+b+c
res= x(5,6,7)
# print(res)



def myfunc(n):
    return lambda a: a*n

double = myfunc(2)

# print(double(11))


numbers =[1,2,3,4]
squared = list(map(lambda x:x**2, numbers))    
# print(squared)

filtered  = list(filter(lambda x:x%2 ==0, numbers))
# print(filtered)

data = {
    'Alice': 25,
    'Bob': 30,
    'Charlie': 35,
    'Diana': 28,
    'Ethan': 22
}


filteredUsers = list(filter(lambda item:data[item] > 25,data.keys())) 

multiplyAge = list(map(lambda item:data[item]*2,data.keys()))
# print(multiplyAge)

# print(filteredUsers)

# print(data.keys())


students_scores = {
    'Alice': {'math': 100, 'science': 90, 'english': 100},
    'Bob': {'math': 70, 'science': 82, 'english': 88},
    'Charlie': {'math': 95, 'science': 92, 'english': 91},
    'Diana': {'math': 60, 'science': 75, 'english': 80},
    'Ethan': {'math': 88, 'science': 85, 'english': 90}
}



# # Task 1: Calculate average scores
average_scores = {name: (lambda scores: sum(scores.values()) / len(scores))(scores) for name, scores in students_scores.items()}
# print(average_scores)
# # Task 2: Filter students with average scores greater than 80
filtered_students = {name: avg for name, avg in average_scores.items() if avg > 80}

# print(filtered_students)

# average = list(map(lambda stud: ()))

# res = list(map(lambda score: sum(students_scores.keys()[score]), students_scores.keys()))
# print(res)
# print(students_scores.items())
# print(average)
sum_of_students_result = list(map(lambda score:students_scores.keys(), students_scores.keys()))

# print(sum_of_students_result)

average_stud_list={}

for stud in students_scores.keys():
    for stud in students_scores.keys():
      average=sum(students_scores[stud].values())/ len(students_scores[stud].keys())
      average_stud_list[stud]=average

print(average_stud_list)
filtereStudes = list(filter(lambda stud: average_stud_list[stud] > 80,average_stud_list.keys()))

print(filtereStudes)