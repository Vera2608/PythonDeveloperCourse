#Dit run je als de applicatie start
from view.taskview import TaskView


def main():
    TaskView.show_menu()
    TaskView.menu_choice()


if __name__ == '__main__':
    main()
