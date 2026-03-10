from Applicatie_todo.model.taskmodel import TaskModel

class TaskController:
    @staticmethod
    def get_tasks():
        taken = TaskModel.get_tasks()
        return taken