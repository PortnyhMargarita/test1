import csv
import json
import os

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def convert_csv_to_json() -> None:
    # Проверяем, существует ли CSV-файл
    if not os.path.exists(INPUT_FILENAME):
        print(f"Файл '{INPUT_FILENAME}' не найден.")
        return

    # Читаем данные из CSV-файла
    with open(INPUT_FILENAME, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    # Записываем данные в JSON-файл
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    convert_csv_to_json()
    if os.path.exists(OUTPUT_FILENAME):
        with open(OUTPUT_FILENAME) as output_f:
            for line in output_f:
                print(line, end="")