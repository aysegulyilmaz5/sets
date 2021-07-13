#sets automatic ordered
#we cannot change an existing data int the list

studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)

for student in studentsSet:

  print(student)

print("Derin" in studentsSet)

if "Derin" in studentsSet:
  print("List has the value")

studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Merve","Ceyda","Beste"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Ali")
print(len(studentsSet))

studentsSet.discard("Mert")
print(len(studentsSet))

x = studentsSet.pop()
print(len(studentsSet))
print(studentsSet)

x = studentsSet.clear()
print(studentsSet)





