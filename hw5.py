#!/usr/bin/env python3
''' Assignment 5

 1. Create a text file called Todo.txt using the following data, one line per row:
Clean House,low
Pay Bills,high

2. When the program starts, load each row of data from the ToDo.txt text file
into a Python list. You can use the readlines() method to import all lines as a list. 
 
3. After you load the data into a list, loop through the list and add each item
as a "key,value" pair a new dictionary. Look back through the lecture notes
at "split" and "indexing".

4. After you have added existing data to the dictionary, use the menu structure
included in the template to allow the user to Add or Remove tasks from the
dictionary using numbered choices.

5. Create your menu by adding a print statement that tells the user which
option to select. Something similar to this: 
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program

6. Save the data from the table into the Todo.txt file when the program exits.

7. For two points, let us know what you would like feedback on and/or have questions about '''

infile = "todo.txt"
# read in ToDo.txt here using readlines

with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()

task_dict = {}
# create empty dictionar to store data as we loop

for line in lines:
       task = line.split(",")[0].strip()
       priority = line.split(",")[1].strip()
       task_dict[task] = priority
# add line to add new key to a dictionary here using task ask key and priority as value

while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print() #adding a new line

# Choice 1 -Show the current items in the table
    if (strChoice.strip() == '1'):
           for key, val in task_dict.items():
                  print(key, val)
# loop through the dictionary here and print items

# Choice 2 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
       new_key = input("Enter the additional task: ")
       new_value = input("Rank the priority from low to high: ")
       task_dict[new_key] = new_value
# add a new key, value pair to the dictionary

# Choice 3 - Remove a new item to the list/Table
    elif (strChoice == '3'):
       remove_key = input("Enter the task name to remove: ")
       if remove_key in task_dict.keys():
              del task_dict[remove_key]
       else:
              input("Your task is not in the dictionary, please check spelling and try again: ")
# locate key and delete it using del function

# Choice 4 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
           with open(infile, 'w') as fh:
                  # fh.writelines(task_dict)
                  for key, value in task_dict.items():
                         fh.write('{},{}\n'.format(key, value))
# open a file handle
# loop through key, value and write to file

    # Chocie 5- end the program
    elif (strChoice == '5'):
          print("Goodbye!")
          break #and Exit the program

       
