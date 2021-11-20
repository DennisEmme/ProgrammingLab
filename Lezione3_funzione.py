def somma_valori_file(my_file):
    values=[]
    for line in my_file:
        elements=line.split(",")
        if (elements[0]!="Date"): 
            numero=elements[1]                 
            values.append(float(numero))
    my_file.close()
    return round((sum(values)), 1)
my_file_Shampoo=open("Shampoo_sales.txt","r")
print(somma_valori_file(my_file_Shampoo))