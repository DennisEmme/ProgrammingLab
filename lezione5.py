class CSVFile():
    def  __init__(self, file_name):
        self.name=file_name

    def get_data(self):
        file_list = []   
        openedfile = open(self.name, 'r')
        for line in openedfile:
            elements = line.split(',')
            if elements[0] != "Date":
                lineElements = line.split (',')
                lineElements [1] = lineElements [1].strip()
                file_list.append(lineElements)
        return file_list 

shampooFile = CSVFile('Shampoo_sales.csv')
shampooList = shampooFile.get_data()

try:
    openedfile = open(Giga, 'r')

except Exception as e:
    print('non posso aprire il file "Giga"!')
    print('ho avuto un errore generico: "{}".'.format(e))


for line in shampooList:
    print(line)

