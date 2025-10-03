import pickle
from student import students
import os
file_name="data.pkl"
def std_data(student):
    students=[]
    if os.path.exists(file_name):
        with open("data.pkl","rb")as file:
            students=pickle.load(file)
    students.append(student)
    
    with open("data.pkl","wb")as file:
        pickle.dump(students,file)

def load_data(return_data=False):
    if not os.path.exists(file_name):
        if return_data:
            return []
        else:
            print("No data found.")
            return
    
    with open(file_name, "rb") as file:
        data = pickle.load(file)
    
    if return_data:
        return data
    
    for student in data:
        print(student.display())



