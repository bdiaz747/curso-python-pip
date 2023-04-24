# python app_1/main.py
# Modulos llamadando las funciones declaradas en orto módulo
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  list_continents = ['Africa','Asia','Europe','North America','Oceania','South America']
  print(list_continents)
  continent = input('Escriba un de los continentes => ')
  data = list(filter(lambda item  : item['Continent'] == continent, data)) 
  countries = list(map(lambda x: x['Country/Territory'],data))
  percentages  = list(map(lambda x: x['World Population Percentage'],data))
  charts.generater_pie_chart(countries,percentages)
  
  country= input('Type country => ')
  result = utils.population_by_continent(data, continent)

  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generater_bar_chart(country['Country/Territory'],labels, values)
  
# conifigurando main.py para que pueda ser ejecutado desde la terminal
if __name__ == '__main__':
  run()

