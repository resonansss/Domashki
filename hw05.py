#zadacha 2
import csv
with open(r'C:\Users\Acer\Desktop\программульки\Maths.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    c = 0
    for row in reader:
        c += 1
        print(', '.join(row))
        if c >= 5:
            break
print(''' 
      --------------------------
      ''')

data = []
with open(r'C:\Users\Acer\Desktop\программульки\Maths.csv') as csvfile:
    reader = csv.reader(csvfile) 
    for row in reader:
        data.append(row)

data_kol = data[:1][0]
for elem in data_kol:
    print(elem)