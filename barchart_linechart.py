# read file
with open("clean_data.csv", encoding="utf-8") as file:
  data = file.read().split("\n")

header = data[0]
header = header.replace("social-science", "ss")
header = header.replace("natural-science", "ns")

students = data[1:]

# split header
header = header.split(",")
subjects = header[5:]

# turn each student to a list
for i in range(len(students)):
  students[i] = students[i].split(",")

# remove last student (empty student)
students.pop()

# get number of student per age group
# 2003 2002 2001 2000 .. 1994 <= 1993
# 17 18 19 .. 26 >= 27
num_of_student_per_age_group = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
average_of_student_per_age_group = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in students:
  age = 2020 - int(s[4])
  if age >= 27:
    age = 27
  num_of_student_per_age_group[age - 17] += 1

  sum_score = 0 
  count_score = 0
  for i in range(11):
    if s[i+5] != "-1":
      count_score += 1
      sum_score += float(s[i+5])
  
  average = sum_score / count_score
  average_of_student_per_age_group[age-17] += average

for i in range(11):
  average_of_student_per_age_group[i] = average_of_student_per_age_group[i] / num_of_student_per_age_group[i]

for i in range(11):
  average_of_student_per_age_group[i] = average_of_student_per_age_group[i] * 7000

# plot barchart
import matplotlib.pyplot as plt
import numpy as np

age_label = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, ">26"]
x = np.arange(11)
y = np.arange(11)

fig, axis = plt.subplots()
plt.bar(x, num_of_student_per_age_group)
plt.plot(x, average_of_student_per_age_group, color='red', marker='o')

# set limit
axis.set_ylim(0, 70000)

# label for column x
plt.xticks(x, age_label)

axis.set_ylabel('Students')
axis.set_xlabel('Age')

# right side ticks
ax2 = axis.twinx()
ax2.tick_params('y', colors='r')
ax2.set_ylabel("Average score")
ax2.set_ylim(0, 10)

rects = axis.patches

labels = [2, 66327, 4463, 1396, 767, 384, 300, 223, 177, 109, 296]

for rect, label in zip(rects, labels):
  height = rect.get_height()
  axis.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

plt.title('Average score based on ages')

# show the plot
plt.show()