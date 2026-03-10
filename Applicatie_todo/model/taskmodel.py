import csv

class TaskModel:
    @staticmethod
    def get_tasks():
        csv_file = open('data/taken.csv', newline= '')
        reader = csv.reader(csv_file)
        tasks = list(reader)
        return tasks

    @staticmethod
    def add_task(task):
        csv_file = open('data/taken.csv', 'a', newline= '')
        writer = csv.writer(csv_file)
        writer.writerow([task])