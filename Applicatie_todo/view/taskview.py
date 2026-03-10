from Applicatie_todo.controller.taskcontroller import TaskController


class TaskView:
    @staticmethod
    def show_menu ():
        print("Menu")
        print("1. Add task")
        print("2. Show task")
        print("3. Exit")

    @staticmethod
    def menu_choice():
        choice = int(input("Choose an option: "))
        if choice == 1:
            TaskView.add_task()
        elif choice == 2:
            # show tasks
            TaskView.show_tasks()
        elif choice == 3:
            exit()

    @staticmethod
    def show_tasks():
        taken = TaskController.get_tasks()
        print("Tasks:")
        print(taken)

    @staticmethod
    def add_task():
        task = input("Enter task: ")
        TaskController.add_task(task)