import csv

class ReadModel:
    input_file = "data/taken.csv"
    fieldnames = None

    @staticmethod
    def read_file(input_file):
        with open(input_file, newline="") as f:
            reader = csv.DictReader(f)
            ReadModel.fieldnames = reader.fieldnames
            rows = list(reader)
            return rows

    def write_file(input_file, rows):
        with open(input_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=ReadModel.fieldnames)
            writer.writeheader()
            writer.writerows(rows)