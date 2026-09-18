def main ():
    tasks = []
    command = ""


    while True:

        print(f"Taks to do: {len(tasks)}")
        print(tasks)
        command= input("What do you want to do?(add, complete,exit):")

        if command == "exit":
            break

        elif command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif command == "complete":
            complete_task = input("Task completed: ")
            tasks.remove(complete_task)






if __name__== "__main__":
    main()
