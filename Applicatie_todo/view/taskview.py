from Applicatie_todo.controller.taskcontroller import TaskController


class TaskView:
    @staticmethod
    def show_menu ():
        print("Menu")
        print("1. Add task")
        print("2. Delete task")
        print("3. Show task")
        print("4. Exit")

    @staticmethod
    def menu_choice():
        choice = int(input("Choose an option: "))
        if choice == 1:
            TaskView.add_task()
        elif choice == 2:
            #delete task
            TaskView.delete_task()
        elif choice == 3:
            # show tasks
            TaskView.show_tasks()
        elif choice == 4:
            exit()

    @staticmethod
    def show_tasks():
        taken = TaskController.get_tasks()
        print("Tasks:")
        print(taken)

    @staticmethod
    def add_task():
        task = input("Enter taak om toe te voegen: ")
        TaskController.add_task(task)

    @staticmethod
    def delete_task():
        task = input("Enter taak om te verwijderen: ")
        TaskController.delete_task(task)