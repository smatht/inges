from django.test import TestCase
#from .models import Factura_recibida
#from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
# reverse para no repetir codigo, usamos en test_views


class SimpleTest(TestCase):
	def setUp(self):
		# Metodo que se ejecutasiempre al iniciar test para poder tener
		# siempre un objeto categoria y un usuario para usar
		'''
		categoria = Categoria.objects.create(titulo='Categoria de prueba')
    	usuario = User.objects.create_user(username='smatht', password='papa')
    	'''

    def test_un_metodo(self):
    	# Prueba de un metododentro deun modelo

    	# Creamos los objetos que se mapean a la base de datos
    	'''
    		categoria = Categoria.objects.create(titulo='Categoria de prueba')
    		# metodo create_user es un metodo especial para crear un objeto de usuario
    		usuario = User.objects.create_user(username='smatht', password='papa')
    		enlace = Enlace.objects.create(titulo='titulo deprueba', categoria=categoria...etc)

    		# hacemos las pruebas del estado del objeto
    		self.assertEqual(enlace.votos, 0)
    		self.assertFalse(enlace.es_popuar())

    		# cambiamos el estado
    		enlace.votos = 20
    		enlace.save()

    		self.assertEqual(enlace.votos, 20)
    		self.assertTrue(enlace.es_popuar())
    	'''

    def test_view(self):
    	'''
    	# prueba de que una pagina se presente correctamente
    	res = self.client.get(reverse('home'))
    	self.assertEqual(res.status_code, 200)

    	# prueba de que una pagina se presente correctamente con user required
    	self.assertTrue(self.client.login(username='smatht', password='papa'))
    	res = self.client.get(reverse('home_login'))
    	self.assertEqual(res.status_code, 200)
    	'''

    def test_form(self):
        '''
    	self.assertTrue(Enlace.objects.count(), 0)
    	#creamos un diccionario
    	data = {}
    	data['titulo'] = 'Un titulo'
    	data['votos'] = '0'
    	self.assertTrue(self.client.login(username='smatht', password='papa'))
    	res = self.client.post(reverse('add'), data)
    	self.assertEqual(res.status_code, 302) #prueba si retorna un redirect
    	self.assertTrue(Enlace.objects.count(), 1)# prueba si hay un enlace en la base de datos

    	enlace = Enlace.objects.all()[0]
    	self.assertEqual(enlace.titulo, data['titulo'])# prueba si es el que agregamos
        '''
