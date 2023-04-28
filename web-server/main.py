import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() # se crea la instancia
@app.get('/')# la ruta por donde se puede ingresar al recurso
def get_list(): # se crea el primer recurso
    return [1,2,3]
    
def run():
    store.get_categories()

@app.get('/contact', response_class=HTMLResponse)# la ruta por donde se puede ingresar
def get_list(): # se crea el primer recurso
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    
def run():
    store.get_categories()

if __name__  == '__main__':
    run()