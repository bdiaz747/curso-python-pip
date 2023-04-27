# python app_1/main.py
# Modulos llamadando las funciones declaradas en orto módulo
import utils
import read_csv
import charts
import pandas as pd

def run():
  ''' 
  data = list(filter(lambda item  : item['Continent'] == continent, data)) 
  countries = list(map(lambda x: x['Country/Territory'],data))
  percentages  = list(map(lambda x: x['World Population Percentage'],data))
  charts.generater_pie_chart(countries,percentages)
  '''
  df = pd.read_csv('data.csv')  # df = dataframe , leemos el csv con pandas
  list_continent = df['Continent'].values # lista los continentes
  print(list_continent)
  continent = input('Escriba uno de los continentes => ')
  df = df[df['Continent'] == continent] # filtra el csv por el continente digitado
  list_countries = df['Country/Territory'].values # lista los paises del continente selecionado
  print(list_countries)
  country= input('Type country => ')
  
  countries = df['Country/Territory'].values 
  percentages = df['World Population Percentage'].values 
  charts.generater_pie_chart(countries,percentages)
  data = read_csv.read_csv('data.csv')
  
  result = utils.population_by_country(data, country)

  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generater_bar_chart(country['Country/Territory'],labels, values)
  
# conifigurando main.py para que pueda ser ejecutado desde la terminal
if __name__ == '__main__':
  run()

