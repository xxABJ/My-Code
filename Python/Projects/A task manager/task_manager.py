import json

file_name = "all_tasks.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            if file:
                print(f"File name: '{file_name}' has been loaded successfully.\n")
                return json.load(file)
    
    except:
        print("\nNo file located.")
        print(f"Creating a new file called: {file_name}\n")
        template = {"tasks": []}

        with open(file_name, "x") as file:
            if file:
                print(f"\nFile name: '{file_name}' has been created successfully.")
                json.dump(template, file)

        with open(file_name, "r") as file:
            if file:
                print(f"File name: '{file_name}' has been loaded successfully.\n")
                return json.load(file)

def save_tasks(tasks1):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks1, file)

    except:
        print(f"\nFailed to save filename: {file_name}")

def view_tasks(tasks1):
    print("\nTo-do list:")

    if len(tasks1["tasks"]) > 0:
        for index, task in enumerate(tasks1["tasks"]):
            description = task["description"]

            if task["status"]:
                print(f"{index + 1}. {description} | Completed")
            else:
                print(f"{index + 1}. {description} | Pending")
    else:
        print("No tasks recorded.\n")

def add_tasks(tasks1):
    while True:
        print("\nPlease enter a task description.")
        description = input("-> ").strip()

        if description:
            tasks1["tasks"].append({"description": description, "status": False})
            save_tasks(tasks1)
            return print("\nNew task has been added!\n")
        else:
            print("Task description can not be empty.")

def delete_tasks(tasks1):
    view_tasks(tasks1)

    while True:
        print("\nWhich task would you like to delete?")
        delete = input("-> ")

        try:
            delete = int(delete)
            if 1 <= delete <= len(tasks1["tasks"]):

                for index, task in enumerate(tasks1["tasks"]):
                    if index == delete-1:
                        tasks1["tasks"].pop(index)
                        save_tasks(tasks1)
                        return print("\nTask has been removed!")
            else:
                print("No task with that number.")

        except:
            print("Invalid answer.")

def complete_task(tasks1):
    view_tasks(tasks1)

    while True:
        print("\nPlease select a task to mark as completed.")
        complete = input("-> ").strip()

        try:
            complete = int(complete)
            if 1 <= complete <= len(tasks1["tasks"]):

                for index, task in enumerate(tasks1["tasks"]):
                    if index == complete-1:
                        if task["status"] == True:
                            return print("\nTask is alreading completed.\n")
                        else:
                            task["status"] = True
                            save_tasks(tasks1)
                            return print("\nTask has been marked as 'Completed'.\n")
            else:
                print("No task with that number.")
                
        except:
            print("Invalid answer.")

def revert_status(tasks1):
    view_tasks(tasks1)

    while True:
        print("\nPlease select a task to mark as pending.")
        pending = input("-> ")

        try:
            pending = int(pending)
            if 1 <= pending <= len(tasks1["tasks"]):

                for index, task in enumerate(tasks1["tasks"]):
                    if index == pending-1:
                        if task["status"] == False:
                            return print("\nTask is alreading pending.\n")
                        else:
                            task["status"] = False
                            save_tasks(tasks1)
                            return print("\nTask has been marked as 'Pending'.\n")
            else:
                print("No task with that number.")

        except:    
            print("Invalid answer.")

def reprint_main(self):
    if self > 0 and self % 2 == 0:
        main_ui()
        return self+1
    else:
        return self+1

def main_ui():
    print("\nTask Manager Program:")
    print("1. View tasks.")
    print("2. Add a new task.")
    print("3. Complete a task.")
    print("4. Revert a task.")
    print("5. Delete a task.")
    print("6. Exit.\n")

def main():
    tasks1 = load_tasks()
    
    main_ui()

    reprint = 1

    while True:
        command = input("-> ").strip()

        if command == "1":
            view_tasks(tasks1)
            input("Please any key to return.")
            main_ui()
        elif command == "2":
            add_tasks(tasks1)
            reprint = reprint_main(reprint)
        elif command == "3":
            complete_task(tasks1)
            reprint = reprint_main(reprint)
        elif command == "4":
            revert_status(tasks1)
            reprint = reprint_main(reprint)
        elif command == "5":
            delete_tasks(tasks1)
            reprint = reprint_main(reprint)
        elif command == "6":
            print("Exiting . . .\n")
            break
        else:
            print("Can't not execute.\n")
            reprint = reprint_main(reprint)

main()