import numpy as np
#5 students,4 subjects.marks out of 100
marks=np.array([
    [78,85,92,88],
    [65,70,68,72],
    [90,88,95,91],
    [55,60,58,62],
    [82,70,85,80],
])
students = ["Ali",'sarah','john','Ana', "Mike"]
subject = ["math","science","english","history"]

#add bonus +5 marks
marks = marks+5
print("After Bonus", marks)

#not more than 100 marks locking 100
marks=np.clip(marks,0,100)

#finding average per student
avg_per_student =np.mean(marks,axis=1)
for name ,avg in zip(students,avg_per_student):
    print(f"{name} : {avg: 2f} avg")

# find the average pER subject
avg_per_subject =np.mean(marks,axis=0)
for name ,avg in zip(subject,avg_per_subject):
    print(f"{subject} : {avg: 2f} avg")


#highest and lowest marks per student
highest = np.max (marks)
print("highest Score:", highest)
lowest = np.min (marks)
print("Lowest Score:", lowest)

highest_per_student = np.max(marks, axis=1)

#students who scored above 70
#using Boolean masking

above_70 = avg_per_student > 70
top_students = np.array(students)[above_70]

print("\n student above 70 average")
for name in top_students:
    print(name)

