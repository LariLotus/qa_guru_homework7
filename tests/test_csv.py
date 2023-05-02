import csv
import os
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
resources = os.path.join(PROJECT_ROOT_PATH, '../resources')

def test_csv():
    csv_path = os.path.join(resources, 'eggs.csv')
    with open('../resources/eggs.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)
        csv_read_list = []
        for row in csvreader:
            print(row)
            csv_read_list.append(row)
    assert csv_read_list[1] == ['Alex', 'Serj', 'Yana']
