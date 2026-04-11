todo = []

while True:
    print("\n========================================")
    print("Welcome  to the to do list pick an option:")
    print("1 to  add  a task to the list")
    print("2 to delete a task")
    print("3  to  show all of the task")
    print("4 to exit the program")
    print("========================================")
    option = int(input("Enter a Number: "))

    if option == 1:
        print("----------------------------------------")
        addtask = input("Add a task: ")
        try:
            todo.append(addtask)
        except: 
            print("An error occured")
        else : 
            print(addtask, "task added")

    elif option == 2:
        if len(todo) == 0:
            print("Your list is empty! you must have atleast 1 task to delete")
        else:
            print("----------------------------------------")
            for index,task in enumerate(todo,start=1):
                print(f"{index}. {task}")
            print("----------------------------------------")
            deletetask =  int(input("delete a task:"))
            try:
                todo.pop(deletetask - 1)
            except:
                print("an error  occured")
            else:
                print("task sucessfully deleted")

    elif option == 3:
        if len(todo) == 0:
            print("Your list is empty!")
        else:
            print("----------------------------------------")
            for index,task in enumerate(todo,start=1):
                print(f"{index}. {task}")
            print("----------------------------------------")

    elif option == 4:
        print("----------------------------------------")
        print("Thank you for using the program")
        print("========================================\n")
        break

    else:
        print("----------------------------------------")
        print("input Unknown,Try Again")

    

