# encoding:utf-8

from random import choice
# Context_processors sirve para unsar datos de manera global en
# todas las plantillas. Hay que configurarlo en Settings.py
saludo = ['Hola mi gente!', 'Welcome my cousin!', 'Accogliere mio fratello',
			'Saluto vos extollatur', 'Olá meu povo']
def ejemplo(request):
	return {'saludo': choice(saludo)}