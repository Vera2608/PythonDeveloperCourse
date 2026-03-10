import csv

class ReadModel:
    input_file = "data/taken.csv"

    @staticmethod
    def read_file(input_file):
        with open(input_file, newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            rows = list(reader)
            return rows
