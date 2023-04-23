# python app/read_csv.py
import csv

def read_csv(path):
  # leemos el archivo con open() solo lectura r
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    # optenemos el título de las columnas
    header = next(reader)
    data = []
    # lo recorremos fila por fila (row)
    for row in reader:
      # itilizamos zip() para unir las dos listas en tuplas
      iterable = zip(header, row)     
      # utilizamos la lista que esta en tuplas y generamos un lista en 
      # forma de diccionarios con comprehesition
      country_dict = {key: value for key, value, in iterable}
      data.append(country_dict)
    return  data 

      
# lo definimos como script      
if __name__ == '__main__':
  # llama la función
  data= read_csv('./data.csv')
  
  