from Applicatie_todo.controller.taskcontroller import TaskController


class TaskView:
    @staticmethod
    def show_menu ():
        print("Menu")
        print("1. Add task")
        print("2. Show task")

    @staticmethod
    def menu_choice():
        choise = int(input("Choose an option: "))
        if choise == 1:
            # add task
            pass
        elif choise == 2:
            # show tasks
            TaskView.show_tasks()

    @staticmethod
    def show_tasks():
        taken = TaskController.get_tasks()
        print("Tasks:")
        print(taken)