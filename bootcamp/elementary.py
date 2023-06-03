# elementary python knowledge

# indexing
"""
var = "hello"

print(varr[1:3]) #this will print values in index 1 and 2 and ignore 3
NB: negative indexing
"""

#lists
# update list
"""
list = ["a", "b", "c", "d", "e"]
print(list)
list[2] ="z"
print(list)
"""
#tuple()
# cannot be changed but can be deleted as a whole.

#stacks follow a rule of first in last out or last in first out
#queue follow a rule of first in first out or last in last out

# list manipulation
# merging lists
"""
import random
list = ["a", "b", "c", "d", "e"]
list2 = [1,2,3,4,5,6,7,8,9,10]

merged_list = []
merged_list.extend(list)
merged_list.extend(list2)

print(merged_list)
"""

#dictionaries
"""
vehicle = {
    "car" : "BMW",
    "model" : "2020"
}
print("original",vehicle)

#updating a dictionary
vehicle2 = {
    "car" : "ford"
}
vehicle.update(vehicle2)

print("update", vehicle)
# Can merging two dictionaries using updates
# to delete elements, use 
del vehicle["ford"]
# to clear dictionary, use
vehicle.clear()
# to delete dictionary, use
del vehicle
"""

#exceptions & errors
"""
name error - calling an undefined variable
EOF - empty input
ValueError - invalid input for particular data type
IndexError - invalid index position
zeroDevisionError  - divide by zero
"""

#handling exceptions

try:
    text  = input("Enter anything ... \n: ")
except EOFError :
    print("\nEOFError, you didn't enter anything")
except KeyboardInterrupt:
    print("KeyboardInterrupt, you cancelled the program")
except ValueError:
    print("ValueError, wrong data type for this field")
else:
    print("You entered",format(text))