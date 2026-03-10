from Applicatie_todo.model.taskmodel import TaskModel

class TaskController:
    @staticmethod
    def get_tasks():
        taken = TaskModel.get_tasks()
        return taken

    @staticmethod
    def add_task(task):
        TaskModel.add_task(task)

    @staticmethod
    def delete_task(task):
        TaskModel.delete_task(task)