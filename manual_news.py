import pandas as pd
import json
from bunny import bunny
import json
import os


source = ['quinto_poder', 'sol_de_mexico', 'vanguardia']
dates = ['2019-04-06', '2019-04-06', '2019-04-06']
title = ['“Yo no trago de sus impuestos”, así arremete diputada del PES contra ciudadanos', 
	'Diputada del PES dice que no "traga" de los impuestos de los mexicanos', 
	'Diputada del PES se defiende en redes sociales: Yo no trago de sus impuestos, sino de mi marido']
text = ["""La diputada del PES, Nay Salvatori, causó controversia en Twitter luego de que asegurara que “no traga de los impuestos de los ciudadanos, ya que su trabajo lo hace por amor a México. 
	Salvatori es conocida porque sus mensajes en redes sociales suelen desatar el debate y esta vez no fue la excepción. “No se confundan, yo no ‘trago’ como dicen ustedes de sus impuestos, yo ‘trago’ de mi marido, afortunadamente trabajo por amor a mi país no por necesidad”, escribió.
	Desde luego que su mensaje provocó toda clase de reacciones en redes sociales, la mayoría fueron críticas. En los últimos días, Salvatori también trae pelito con Javier Lozano, a quien lo llamó “burro”, después de que el exlegislador publicara un cartón que hacía referencia a las contrataciones del gobierno actual.
	¿Qué opinas del comentarios de la diputada del Partido Encuentro Social?""",
	"""La diputada abrió la polémica al ofrecerse a pagar la deuda de una actriz. 
	A pesar de ganar 74 mil 548 pesos mensuales que provienen de recursos públicos, Nayeli Salvatori Bojalil, diputada federal del Partido Encuentro Social (PES), aseguró que no “traga” de los impuestos de los mexicanos sino del dinero que proviene de su marido.
	Dicha aseveración la hizo a través de su cuenta de twitter tras responder a sus comentarios de ofrecerse a pagar la deuda que supuestamente tiene la actriz Laisha Wilkins con un carpintero.
	No se confundan, yo no “trago” como dicen ustedes de sus impuestos, yo “trago” de mi marido –Mario Montero Rosano, hijo de Mario Montero, ex secretario de Gobernación estatal en el sexenio priista de Mario Marín-, afortunadamente trabajo por amor a mi país no por necesidad”, expuso en uno de los mensajes difundidos en redes sociales la mañana de este sábado.
	En consecuencia, surgieron expresiones de usuarios que en su mayoría la criticaron: “Entonces renuncie a su sueldo, diputada. ¡A ver si tanto amor”, “¡O que lo done a gente que necesita ayuda, si viene a presumirnos que su esposo lo mantiene y el sueldo que recibe del país le es indiferente, pues que haga algo bueno con él, al fin que dinero le sobra”, “¡Ya quítenle el celular a esta pseudeodiputada, cada vez se hunde más!”.
	Mensualmente percibe 74 mil 500 pesos mensuales desde su ingreso a la Cámara de Diputados en septiembre de 2018.""",
	"""En varios tuits, sus seguidores le exigieron respeto, porque ellos son sus patrones y sus jefes y con sus impuestos se paga su salario.
	Una vez más la diputada federal de Encuentro Social, Nay Salvatori, está envuelta en la polémica cuando a través de su cuenta en la red social de Twitter, les dijo a sus opositores que no se confundieran, pues ella no "traga" de sus impuestos, sino "traga" de su marido.
	En un mensaje que subió este sábado, la legisladora por el estado de Puebla, agregó que ella afortunadamente trabaja por amor a su país, y no por necesidad.
	"No se confundan, yo no 'trago' como dicen ustedes de sus impuestos, yo 'trago' de mi marido, afortunadamente trabajo por amor a mi país no por necesidad", describió.
	Esto después de que en varios tuits, sus seguidores le exigieron respeto, porque ellos son sus patrones y sus jefes y con sus impuestos se paga su salario.
	Antes, en otro mensaje, dijo que ella se debe a los electores del Distrito 10, pues ellos sí votaron por ella y obtuvo la votación más alta del estado, y de ellos sí es empleada.
	"Yo me debo al Distrito 10 que fue el que me votó y por cierto con la votación más alta en el Estado, de ellos si soy empleada si no perteneces a dicho distrito #Telocico", dijo."""]
author = ['', 'Marco A. Mirón', '']
url = ['https://quinto-poder.mx/trendy/yo-no-trago-de-sus-impuestos-asi-arremete-diputada-del-pes-contra-ciudadanos/', 
	'https://www.elsoldemexico.com.mx/doble-via/virales/asegura-nay-salvatori-que-no-traga-de-los-impuestos-de-los-mexicanos-laisha-wilkins-mario-marin-mario-montero-rosano-don-filiberto-puebla-diputada-3286583.html', 
	'https://vanguardia.com.mx/articulo/diputada-del-pes-se-defiende-en-redes-sociales-yo-no-trago-de-sus-impuestos-sino-de-mi']

all_files = os.listdir('./')

if 'manual_news.json' in all_files:

	before = pd.read_json('./manual_news.json')

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

	after.to_json('./manual_news.json', orient='records')

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

	with open('manual_news.json', 'w') as fp:
		json.dump(dict_, fp)