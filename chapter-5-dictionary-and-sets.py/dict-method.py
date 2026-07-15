marks = {
    "harry" : 100,
    "yash" : 100,
    "rohan" : 40
} 

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry": 102 , "naina": 95}) 
print(marks)    

print(marks.get("harry2"))  # This will print none because the key "harry2" does not exist in the dictionary
# print(marks["harry2"])  # This will raise a KeyError because the key "harry2" does not exist in the dictionary

# this is the difference between get and [] operator. get will return None if the key does not exist, while [] operator will raise a KeyError.

# this is the clear method in dictionary. It will remove all the items from the dictionary.

student = {"name": "harry", "age": 30}
student.clear()

print(student)

#this is the copy method in dictionary. It will create a shallow copy of the dictionary.

student = {"name": "Alice", "age": 20}
new_student = student.copy()

print(new_student)