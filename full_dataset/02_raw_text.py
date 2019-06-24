import pandas as pd 
import json

PATH = './full_dataset/'

title = [
"""
Microbios comedores de plástico: una nueva arma en la batalla contra la contaminación
"""
]

text = [
"""
Un nuevo estudio analiza las bacterias que se unen de forma natural al plástico vertido en el mar y observa los factores necesarios para mejorar su eficacia.
Hace unos días el cocinero Dabiz Muñoz publicaba en su cuenta de Twitter un vídeo en el que se puede ver cómo limpian un pescado en cuyo interior se encuentran varios tapones, algunos trozos de plástico e incluso un peine.
La publicación, con 1’2 millones de reproducciones, alcanzó alrededor de 30.000 retweets y me gustas y hasta el momento ha generado más de 500 comentarios. No es para menos, pues en ella se puede ver una realidad que ya conocemos, pero que se hace aterradoramente más clara con imágenes como estas. Por desgracia, el plástico comienza a convertirse en un rasgo excesivamente frecuente de los ecosistemas marinos, hasta el punto de llegar de vuelta hasta nosotros con el consumo de productos como el pescado, el marisco o la sal.
Lógicamente, el principal paso para evitar este problema debería ser reducir el uso de este material, así como reciclarlo y desecharlo en lugares adecuados, para evitar su llegada a entornos acuáticos. ¿Pero qué pasa si “el mal ya está hecho”? ¿Hay soluciones para los plásticos que se desechan en el lugar incorrecto? Estas preguntas han preocupado a científicos de todo el mundo en los últimos años, dando lugar al desarrollo de estudios dedicados a buscar herramientas que ayuden a eliminarlos. Uno de los más recientes es el que acaba de publicar en Journal of Hazardous Materials un equipo internacional de investigadores, tras analizar cómo se puede potenciar la acción de ciertas bacterias que ya degradan de forma natural los plásticos presentes en el mar.
En 2016, un equipo de científicos japoneses descubrió una bacteria capaz de descomponer la molécula de uno de los plásticos más empleados, el tereftalato de polietileno (PET). Dos años después, otro grupo de investigadores, esta vez estadounidenses, logró modificar una enzima generada por esa bacteria, obteniendo una herramienta de gran utilidad para degradar este material.
Si esta enzima se introduce en bacterias termófilas, capaces de resistir temperaturas por encima de los 70ºC, se podría utilizar para degradar el PET caliente, en un estado más viscoso, de modo que el proceso fuese más rápido. Aunque aún falta mucho por investigar en este camino, aquel hallazgo planteaba un método muy interesante para eliminar el sobrante de PET generado en la industria, pero también los objetos fabricados con él que terminen desechándose en los vertederos.
Ahora, los autores de este nuevo estudio emplean un enfoque diferente, buscando directamente en el lugar del problema. En este caso, han centrado su investigación en las comunidades microbianas que se acumulan en torno a los plásticos depositados en el océano. Estos son el segundo paso de un proceso de degradación natural que tiene lugar siempre sobre estos residuos contaminantes.

"""
]

if __name__ == '__main__':

	news = 'plástico_mar.json'
	folder = 'news_csv/'
	file = PATH + folder + news

	data = pd.read_json(file)

	n = 1
	for index, row in data.iterrows():
		print((' ' + str(n) + ' ') * 30)
		print(row['title'])
		print(row['url'])
		n += 1

	"""raw_text = PATH + folder + news.split('.')[0] + '_text.json'  

	dict_ = {'id': [], 'title': [], 'text': []}

	id_ = 0
	for i in range(len(title)):
		dict_['id'].append(id_)
		dict_['title'].append(title[i])
		dict_['text'].append(text[i])

		id_ += 1

	with open(raw_text, 'w') as fp:
		json.dump(dict_, fp)"""

	"""print(data.shape)
	print(len(title))
	print(len(text))"""