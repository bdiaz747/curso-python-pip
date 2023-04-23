# python app_1/utils.py
# Modulos propios, normalmete son funciones

def get_population(country_dict):
  population_dict = {
    '2022' : int(country_dict['2022 Population']),
    '2020' : int(country_dict['2020 Population']),
    '2015' : int(country_dict['2015 Population']),
    '2010' : int(country_dict['2010 Population']),
    '2000' : int(country_dict['2000 Population']),
    '1990' : int(country_dict['1990 Population']),
    '1980' : int(country_dict['1980 Population']),
    '1970' : int(country_dict['1970 Population'])   
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values
  
def continents(list_continents):
  result = {}
  for item in list_continents:
    if item not in result:
        result.append(item)      
  return result
  
  
# funcion para recibir y recorrer una lista, retornando la busqueda
def population_by_continent(data,continent):
  result =  list(filter(lambda item: item['Continent'] == continent, data))
  
  return result
  
# funcion para recibir y recorrer una lista, retornando la busqueda  
def population_by_country(data, country):
  result =  list(filter(lambda item: item['Country/Territory'] == country, data))
  return result


