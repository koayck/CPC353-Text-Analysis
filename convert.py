# extract 2 column from csv, and convert to txt file
import csv
import os

for file in os.listdir('./data'):
    file_name = file.split('.')[0]
    with open(f'./data/{file_name}.csv', 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        with open(f'./txt/{file_name}.txt', 'w', encoding="utf-8") as txt_file:
            next(csv_reader)  # skip the header
            for line in csv_reader:
                txt_file.write(f'{line[2]}: {line[3]}\n') # specify the column to extract

print('Done!')
