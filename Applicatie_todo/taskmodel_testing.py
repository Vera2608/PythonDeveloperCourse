from Applicatie_todo.model.taskmodel import TaskModel

print(TaskModel.get_tasks())
TaskModel.add_task("test")
print(TaskModel.get_tasks())
TaskModel.delete_task("test")
print(TaskModel.get_tasks())
