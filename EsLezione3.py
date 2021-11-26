values = []

my_file = open('Shampoo_sales.csv', 'r')
for line in my_file:
    elements = line.split(',') 
    if elements[0] != 'Date':
        date = elements[0]
        value = elements[1]
        values.append(float(value))
    sum(values)
print(round((sum(values)), 1))
my_file.close()

