импорт csv
импорт json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

задача def() -> Нет:

    открыть с помощью(INPUT_FILENAME, новая строка='') как csv-файл:
        csv = reader.DictReader(csv-файл)
        = данные [строка для строки в читателе]

    открыть с помощью(OUTPUT_FILENAME, 'w') как файл JSON:
        json.dump(данные, json-файл, отступ=4)

'__main__' == __name__ if:
    задача()
    открыть с помощью(OUTPUT_FILENAME) в качестве output_f:
        output_f в строке для:
            вывести на печать (строку, конец="")