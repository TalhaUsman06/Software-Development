# Unit 6 Consolidate Task

# Task Management syatem using Lists and functions in python

tasks=[]

# Function implementation and defination
def add_task():
    task= input("\nWhat you want to do?\n")
    tasks.append(task)
    print("\n*** Task Added!! ***")
    
def show_tasks():
    print("\n*** Your To-Do Lisk ***\n")
    number=1 #Tasks Counter
    for task in tasks:
        print(number, ".", task)
        number =+1
        
def mark_as_done():
    show_tasks()
    #Ask user aboout how many tasks he has done already
    choice= int(input("\nEnter the task number that are finshed: "))
    
    index= choice-1
    tasks[index] = tasks[index]+ "Already DONE"
    print("\n*** Task Marked as DONE!!***")
    
while True:
    print("\n*** TO-DO list Manager ***\n")
    print("Press 1 to Add Task")
    print("Press 2 to View Task")
    print("Press 3 to Mark Task as Done")
    print("Press 4 to Exit")
    
    choice= input("\nEnter your choice: ")
    
    if choice == "1":
        add_task()
        
    elif choice == "2":
        show_tasks()
    
    elif choice == "3":
        mark_as_done()
        
    elif choice == "4":
        print("*** EXITING!!!!!!!!! ***")
    
    else:
        print("Invalid Choice")
