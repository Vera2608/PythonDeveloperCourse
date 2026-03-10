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

    @staticmethod
    def delete_task(task):

        column = "taak"
        input_file = "data/taken.csv"

        with open(input_file, newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            rows = list(reader)

        #delete the row using a filter:
        rows = [row for row in rows if row[column] != task]


        with open(input_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
