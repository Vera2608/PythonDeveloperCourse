import csv
from Applicatie_todo.model.readmodel import ReadModel


class TaskModel(ReadModel):
    @staticmethod
    def get_tasks():
        csv_file = open('data/taken.csv', newline= '')
        reader = csv.reader(csv_file)
        tasks = list(reader)
        return tasks

    @staticmethod
    def add_task(task):
        rows = ReadModel.read_file(TaskModel.input_file)
        nieuw_id = len(rows) + 1
        csv_file = open('data/taken.csv', 'a', newline= '')
        writer = csv.writer(csv_file)
        writer.writerow([nieuw_id,task])

    @staticmethod
    def delete_task(task):

        column = "taak"

        rows = ReadModel.read_file()

        #delete the row using a filter:
        rows = [row for row in rows if row[column] != task]


        with open(input_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
