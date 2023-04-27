import requests

def get_categories(): # función para traer las cateorias del web-server
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) # para imprimir el estado de la api
    print(r.text)# para imprimir el resultado
    print(type(r.text))# para imprimir el tipo del text
    categories = r.json() # defino una varible y la igualo con la fincion json
    for category in categories: # recorremos el json
        print(category['name']) # imprimimos el name en cada iteración




