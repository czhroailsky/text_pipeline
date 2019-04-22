import pandas as pd
import json
from bunny import bunny
import json
import os


source = ['notigodinez', 'vanguardia', 'heraldo_mexico']

dates = ['2019-04-17', '2019-04-17', '2019-04-17']

title = ['Ahora el “periodista” Pedro Ferriz Hijar critica a AMLO… por los zapatos que utiliza', 
	'Dan pena: Pedro Ferriz critica zapatos de AMLO y redes sociales no lo perdonan', 
	'Pedro Ferriz critica zapatos sucios de López Obrador; lo exhibe en redes']

text = ["""El “periodista” Pedro Ferriz Hijar, engendro del también “comunicador” y simpatizante panista Pedro Ferriz de Con, fue objeto de repudio en las redes sociales luego de criticar el calzado de Andrés Manuel López Obrador, presidente de la República.
	Ferriz Hijar, recordado por protagonizar en 2014 un aparatoso accidente automovilístico y haber huido del lugar de los hechos, publicó un mensaje en la red social Twitter con dos fotografías adjuntas del tabasqueño. Una de ellas muestra un acercamiento del calzado del presidente, apreciándose claramente que sus zapatos no están boleados y tienen la suela muy gastada.
	“Es una pena que alguien así; represente al Presidente de una nación” [sic], consideró el junior Ferriz en su mal redactado mensaje, que inmediatamente desató una lluvia de críticas en su contra.
	La indignación de cientos de usuarios en las redes sociales no se hizo esperar, calificando a Ferriz de “fifí”, “clasista” y otras críticas acordes con la banalidad del mensaje que el sujeto mantiene publicado en su perfil de Twitter.
	Más tarde, el hijo de Ferriz intentó victimizarse acusando un “linchamiento” en su contra y aclarando que no criticaba la “marca” de los zapatos, sino que estuvieran sucios y que López Obrador no contratase los servicios de un “sastre”.
	No obstante, su “aclaración” sólo desató más repudio y críticas en su contra.
	""",

	"""El periodista, Pedro Ferriz Hijar compartió en redes sociales una fotografía de los zapatos de Andrés Manuel López Obrador y aseveró sentir pena que 'alguien así' represente al presidente de una nación.
	Posteriormente, arrivó una 'ola' de críticas que lo clasificaron de clasista, por lo que el presentador de Estrella TV compartió otro 'tuit':
	Sin embargo, su comentario encendió las redes sociales y los usuarios no tardaron en responderle, por lo que Ferriz compartió otro tuit para 'aclarar' su comentario anterior, pero fue de igual manera fuertemente criticado por los internautas.
	""",

	"""
	El periodista lamentó que "alguien así represente a una nación"
	El comunicador Pedro Ferriz Hijar difundió en sus redes sociales este martes una fotografía de Andrés Manuel López Obrador en la que muestra que el presidente porta un par de zapatos negros sucios y desgastados de las puntas.
	Tras su mensaje, las opiniones no tardaron en llegar.
	En redes aparecieron quienes coinciden con él y creen que el presidente debe lucir impecable, hasta los que defendieron al mandatario afirmando que trae los zapatos así debido a que recorre a pie el país.
	Luego de la respuesta negativa que recibió su mensaje, el periodista volvió a publicar la fotografía seguida de un mensaje a manera de justificación por su crítica.
	Cabe recordar que apenas el 26 de marzo, el periodista y el mandatario tuvieron un encontronazo durante la conferencia matutina.
	Ese día, Ferriz Hijar pidió a López Obrador “dejar de confrontarnos entre fifís y no fifís y trabajar juntos por México”, en alusión a la frase “prensa fifí” con la que el presidente suele referirse a los medios de comunicación “conservadores”.

	"""]

author = ['', '', '']

url = ['https://notigodinez.com/ahora-el-periodista-pedro-ferriz-hijar-critica-a-amlo-por-los-zapatos-que-utiliza/', 
	'https://vanguardia.com.mx/articulo/pedro-ferriz-critica-zapatos-de-amlo-y-redes-sociales-no-lo-perdonan', 
	'https://heraldodemexico.com.mx/tendencias/pedro-ferriz-critica-zapatos-sucios-de-lopez-obrador-lo-exhibe-en-redes/']

PATH = './get_raw_data/'

all_files = os.listdir(PATH)

filename = 'manual_news_01.json'

if filename in all_files:

	before = pd.read_json(PATH + filename)

	dict_ = {'id': [], 'source': [], 'date': [], 'title': [], 'text': [], 'author': [], 'url': []}

	id_ = max(list(before['id'].unique())) + 1
	for i in range(len(source)):
		dict_['id'].append(id_)
		dict_['source'].append(source[i])
		dict_['date'].append(dates[i])
		dict_['title'].append(title[i])
		dict_['text'].append(text[i])
		dict_['author'].append(author[i])
		dict_['url'].append(url[i])

		id_ += 1

	new = pd.DataFrame(dict_)
	
	after = pd.concat([before, new])

	after.to_json(PATH + filename, orient='records')

else:
	dict_ = {'id': [], 'source': [], 'date': [], 'title': [], 'text': [], 'author': [], 'url': []}

	id_ = 0
	for i in range(len(source)):
		dict_['id'].append(id_)
		dict_['source'].append(source[i])
		dict_['date'].append(dates[i])
		dict_['title'].append(title[i])
		dict_['text'].append(text[i])
		dict_['author'].append(author[i])
		dict_['url'].append(url[i])

		id_ += 1

	with open(PATH + filename, 'w') as fp:
		json.dump(dict_, fp)