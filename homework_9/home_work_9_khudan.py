import csv

# task_1
rows = [
    ['Name', 'Age', 'Gender'],
    ['John', '30', 'Male'],
    ['Jane', '25', 'Female'],
    ['Bob', '45', 'Male']
]
def write_to_csv_file(file_name, rows):
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)


write_to_csv_file('my_file.csv' , rows)


def read_csv(file_name):
    new_list = []
    with open("my_file.csv" , 'r') as examp:
        reader_csv = csv.reader(examp, delimiter=',')
        for row in reader_csv:
            new_list.append(row)
    return new_list


data = read_csv('my_file.csv')
print(data)

new_rows = [
    ['Sergii','37','Male'],
    ['Andrii','24','Male']
]
for row in new_rows:
    data.append(row)

print(data)


with open("../new_file.csv" , mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)


# task_2
def squares():
    counter = 0
    while counter < 100000:
        yield counter ** 2
        counter += 1

square = squares()
for item in square:
    print(item)



