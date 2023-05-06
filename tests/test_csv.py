import csv
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
from constants import RESOURCES_PATH


def test_csv():
    csv_path = os.path.join(RESOURCES_PATH, 'eggs.csv')
    with open(csv_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)
        csv_read_list = []
        for row in csvreader:
            print(row)
            csv_read_list.append(row)
    # assert csv_read_list[0] == ['Anna', 'Pavel', 'Peter']
    assert csv_read_list[1] == ['Alex', 'Serj', 'Yana']
