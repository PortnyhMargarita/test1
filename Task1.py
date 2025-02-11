import json
import os

def calculate_weighted_average() -> float:
    filename = "input.json"

    # Проверяем, существует ли файл
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не найден.")
        return 0.0

    with open(filename) as json_file:  # открываем файл
        json_data = json.load(json_file)  # десериализует строку в формате JSON в объект Python

    # Вычисляем взвешенную сумму оценок
    weighted_sum = sum([element["score"] * element["weight"] for element in json_data])
    total_weight = sum([element["weight"] for element in json_data])

    # Возвращаем округленное значение
    return round(weighted_sum / total_weight, 3) if total_weight > 0 else 0.0

print(calculate_weighted_average())