# Python vs VBA - no need for Dim!
name = "Ade" # String
age = 30 # Integer
salary = 45000.50 # Float
is_employed = True # Boolean

# Print (like Debug.Print in VBA)
print(f"Name: {name}, Age: {age}, Salary: {salary}")

# Type checking
print("Data type for age: ", type(age)) # Shows <class 'int'>
print("Data type for salary: ", type(salary)) # Shows <class 'float'>

# Creating lists (like arrays in VBA)
employees = ["John", "Sarah", "Mike"]
numbers = [1, 2, 3, 4, 5]

# Accessing items (0-indexed, unlike VBA's 1-indexed)
print("First employee:", employees[0])
print("Last employee:", employees[-1])
print("Second number:", numbers[1])

# Adding items to a list
employees.append("Lisa")
employees.insert(0, "Boss") # Insert Boss at the beginning
print("Updated employees list:", employees)
print (len(employees)) # Length
print ("Sarah" in employees) # Check if Sarah is in the list