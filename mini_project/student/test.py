import pickle
with open ("data.pkl","rb")as file:
    students=pickle.load(file)
print(students[0].display())
print(students[1].display())