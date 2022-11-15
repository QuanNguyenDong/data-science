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

# number of students who took 0,1,2,3...subjects
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]
average = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
  count = 0
  total = 0
  for i in range(11):
    if s[i+5] != "-1":
      total += float(s[i+5])
      count += 1

  num_of_exam_taken[count] += 1
  average[count] += total/count

for i in range(12):
  if num_of_exam_taken[i] != 0:
    average[i] = round(average[i]/num_of_exam_taken[i], 2)

# plot barchart
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.arange(12)

fig, axis = plt.subplots()
plt.bar(x, average)

# set limit
axis.set_ylim(0, 10)

# label for column x
plt.xticks(x, y)

axis.set_ylabel('Average score')

rects = axis.patches

labels = average

for rect, label in zip(rects, labels):
  height = rect.get_height()
  axis.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

# show the plot
plt.show()