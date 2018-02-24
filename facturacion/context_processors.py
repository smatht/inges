# encoding:utf-8

from random import choice
# Context_processors sirve para usar datos de manera global en
# todas las plantillas. Hay que configurarlo en Settings.py
saludo = ['Hola Inges!', 'Welcome my cousin!', 'Accogliere mio fratello',
			'Saluto vos extollatur', 'Olá meu povo']
def ejemplo(request):
    print('SALUDICOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
    print(choice(saludo))
    return {'saludo': choice(saludo)}