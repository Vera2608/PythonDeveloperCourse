import csv

class TaskModel:
    @staticmethod
    def get_tasks():
        csv_file = open('data/taken.csv', newline= '')
        reader = csv.reader(csv_file)
        tasks = list(reader)
        return tasks
