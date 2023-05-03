import csv
import os

def add_row_to_csv(filename, row):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)

def delete_row_from_csv(filename, index):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i, row in enumerate(rows):
            if i != index:
                writer.writerow(row)

def test_add_row_to_csv():
    # створюємо тимчасовий csv-файл для тестування
    filename = 'test.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerow(['John', 30])

    # додаємо третій рядок до csv-файлу
    add_row_to_csv(filename, ['Jane', 25])

    # перевіряємо, чи був доданий рядок до csv-файлу
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        assert rows == [['Name', 'Age'], ['John', '30'], ['Jane', '25']]

    # видаляємо тимчасовий csv-файл
    os.remove(filename)

def test_delete_row_from_csv():
    # створюємо тимчасовий csv-файл для тестування
    filename = 'test.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerow(['John', 30])
        writer.writerow(['Jane', 25])

    # видаляємо другий рядок з csv-файлу
    delete_row_from_csv(filename, 1)

    # перевіряємо, чи був видалений рядок з csv-файлу
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        assert rows == [['Name', 'Age'], ['Jane', '25']]

    # видаляємо тимчасовий csv-файл
    os.remove(filename)
