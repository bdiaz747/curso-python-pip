# python app_1/example.py
# Modulos propios, normalmete son funciones

print ('Llamando la variable data')
print ('desde el example.py que esta en main.py data =>')
# llamando la variable A del módulo utils.py desde el módulo main.py
import main
print(main.data)
print('_' * 40)
print ('ejecuntando main.py desde example.py =>')
main.run()
