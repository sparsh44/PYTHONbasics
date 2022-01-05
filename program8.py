marks=[99,100,89,94]
print(marks)

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print("*******")
print(marks[-2])#piche se ginti shuru
print(marks[-1])
print("*******")
print(marks[0:3])#0 1 2
print(marks[1:4])#1 2 3
print(marks[1:2])#1
print("*********")
for score in marks:
    print(score)
print("*********")
marks.append(33)
print(marks)
print("*********")
marks.insert(2,43)
print(marks)
print("*********")
print(99 in marks)
print(54 in marks)
print("*********")

print(len(marks))
print("*********")

marks.clear()
print(marks)