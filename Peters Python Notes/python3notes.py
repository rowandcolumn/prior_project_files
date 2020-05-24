# PETER HENRY'S PYTHON 3 EXPERIMENTS & NOTES WHILE LEARNING (2013)

# ---------------------------------------------------------------------------------------------
# PRINT STATEMENTS
# ---------------------------------------------------------------------------------------------
weight = 0.2
animal = "newt"
print(weight, "kg is the weight of the", animal)
print("{} kg is the weight of the {}".format(weight, animal))
print("{0} kg is the weight of the {1}".format(weight, animal))
print("{weight} kg is the weight of the {animal}".format(weight = 500000, animal = "spider"))

# ---------------------------------------------------------------------------------------------
# FINDING IN STRINGS
# ---------------------------------------------------------------------------------------------
phrase = "the surprise is in here somewhere"
print(phrase.find("surprise"))
print(phrase.replace("surprise", "head"))
print(phrase)

# ---------------------------------------------------------------------------------------------
# CLASSES
# ---------------------------------------------------------------------------------------------
class Name:
    # constructor methods (creates an instance of a class)
    # self refers to the current instance of a class
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last
        # creating a to-string method (allows us to examine the current state of a class object
        def __str__(self):
            return self.first, self.middle, self.last
aName = Name("Peter", "Gordon", "Henry")
result = str(aName)
print(result)

# ---------------------------------------------------------------------------------------------
# CLASSES NO. 2 (PROBABLY BETTER EXPLANATION BUT DOES NOT INCLUDE THE INIT METHOD)
# ---------------------------------------------------------------------------------------------
# Class of Car
class car:
    # Create Attributes/Variables
    manufacturer = ""
    model = ""
    color = "white"
    age = 0
    # Create Identification Method
    def identify(self):
        # Prints out Identification of New Object of Car Class
        print("I am a {} year old {} {} {}".format(self.age, self.color, self.manufacturer, self.model))
    # Create a new Object called "petersCar" of the Car Class
petersCar = car()
# Set the Attributes/Variables for the petersCar object
petersCar.manufacturer = "Toyota"
petersCar.model = "Rav4"
petersCar.color = "Black"
petersCar.age = 5
# Call the Method identify on the object "petersCar"
petersCar.identify()
# Output => I am a 5 year old Black Toyota Rav4

# ---------------------------------------------------------------------------------------------
# PASSWORD & USERNAME CHECK IN PYTHON
# ---------------------------------------------------------------------------------------------
# AUTHOR PH

# Username & Pass Set (need initial setup by user)
userName = "pgh"
passWord = "helpme"

# Ask User for their Username
usersName = input("Please enter your username: ")

# While Loop Username
while(usersName != userName):
    usersName = input("The username you entered is incorrect, please re-enter it: ")

# Confirm to User that Username was correct
print("----------------------------")
print("Password Correct")
print("----------------------------")

# Ask User for their Password
usersPass = input("Please enter your password: ")

# While Loop Password
while(usersPass != passWord):
    usersPass = input("The password you entered is incorrect, please re-enter it: ")

# Once Correct Details are Input, User is Greeted
print("-------------------------------")
print("Welcome back {}".format(userName))
print("-------------------------------")

# ---------------------------------------------------------------------------------------------
# CLASS INHERITANCE EXAMPLE
# ---------------------------------------------------------------------------------------------
class pet:
    number_of_legs = 0
    def sleep(self):
        print("zzz")
    def count_legs(self):
        print("I have {} legs".format(self.number_of_legs))

# Dog Class Inherrits all methods and variables from Pet Class
class dog(pet):
    def bark(self):
        print("woof")

betsy = dog()
betsy.number_of_legs = 4
betsy.bark()
betsy.sleep()
betsy.count_legs()
print(betsy.number_of_legs)

# Output =>
#   woof
#   zzz
#   I have 4 legs
#   4

# ---------------------------------------------------------------------------------------------
# PERSONAL ATTEMPT AT USING OOP TO CREATE MY OWN TASK MANAGEMENT SYST AT THE COMMAND LINE (WORK IN PROGRESS
# ---------------------------------------------------------------------------------------------
# PETER'S TASK MANAGEMENT PROGRAM IN PYTHON 3
# Task Class Creation
class Task():
    # Class Constructor/Initializer (Called when a new instance is created)
    def __init__(self, priority = 0, title = "", notes = ""):
        self.priority = priority
        self.title = title
        self.notes = notes
        print("Priority: {}, Title: {}, Notes: {}".format(self.priority, self.title, self.notes))

    # Class Method to edit task instances/objects
    def edit(self):
        self.priority = input("What is the new priority?: ")
        self.title = input("What is the new title?: ")
        self.notes = input("what are the new notes?: ")
        print("Task has been edited")

    # Class Method to identify a particular task's Variables/Properties/Attributes
    def identify(self):
        print("Priority: {}, Title: {}, Notes: {}".format(self.priority, self.title, self.notes))

# Start for User Interaction
# Ask User what they want to do
print("Welcome to Peter's Task Manager")
userAction = int(input(print("What do you want to do? 1 = add a task, 2 = see all tasks, 3 = edit a task?: ")))

# Decision & Consequences of User Action
if(userAction == 1):
    taskPriority = int(input("What is the priority of the task 0 to 5 (0 is lowest priority): "))
    taskTitle = input("What is the title of the task?: ")
    taskNotes = input("Please write a one sentence description of the task: ")
    taskObject = taskTitle
    taskTitle = Task(taskPriority, taskTitle, taskNotes)
    print("Task has been created:")
elif(userAction == 2):
    # NEED TO FIND OUT HOW TO PRINT OUT ALL INSTANCES OF THE CLASS "TASK" (IS THERE A BUILT IN?)
    print("Show All Tasks --- Work in Progress")
elif(userAction == 3):
    taskToEdit = input("What is the Title of the task you want to edit?: ")
    taskToEdit.edit()

# ---------------------------------------------------------------------------------------------
#  CLASS CREATION OF A COMPUTER OBJECT USING STANDARD ATTRIBUTES
# ---------------------------------------------------------------------------------------------
class computer:

    def __init__(self, brand = "", model = "", screenSize = "", hardDriveSize = "", memory = "", cpu = ""):
        self.brand = brand
        self.model = model
        self.screenSize = str(screenSize)
        self.hardDriveSize = str(hardDriveSize)
        self.memory = str(memory)
        self.cpu = cpu
        print("------------------")
        print("Object {} Created.".format(self))
        print("------------------")

    def identify(self):
        print("PC Specs: ")
        print("---------")
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Screen Size in Inches: ", self.screenSize)
        print("Hard Drive in Gb: ", self.hardDriveSize)
        print("Memory in Mb: ", self.memory)
        print("CPU: ", self.cpu)

vermit = computer("Asus", "Zenbook", 13, 256, 2, "i5")
vermit.identify()

# ---------------------------------------------------------------------------------------------
#  OTHER
# ---------------------------------------------------------------------------------------------