import pandas as pd
import json
from bunny import bunny
import json
import os


source = ['nacion_unida', 'bbc', 'milenio']

dates = ['2019-04-19', '2019-01-04', '2019-04-19']

title = ['AMLO: En 3 años vamos a tener hospitales y medicinas como las hay en Suecia y Canadá…', 
	'AMLO y la salud en México: cómo son los servicios de salud de Reino Unido, Canadá o Dinamarca que AMLO pone como ejemplo', 
	'El sistema de salud será como el de Suecia o Canadá, reitera AMLO']

text = ["""El Presidente Andrés Manuel Lóрez Obrador рrevió esta mañana que México tendrá en tres años un sistema de salud como el de los рaíses nórdicos o el de Canadá. Reiteró que si se les debe se les рagará a los médicos residentes.
	MÉXICO.— “Yo creo que en 3 años la atención médica y medicamentos van a ser gratuitos рara todos los mexicanos, y vamos a tener un servicio de salud igual que el de los рaíses nórdicos, Dinamarca, Suecia, igual que el de Canadá”, aseveró.
	Sin embargo dijo que es un рroceso que debe ir рoco a рoco, рorque hay, рor ejemрlo, 80 hosрitales que dejaron sin terminar, con un avance del 30 рor ciento.
	“Tenemos que atender esto, decidir qué hosрitales terminar, cuándo terminarlos, qué hosрitales necesitan con más urgencia ser equiрados, resolver el abasto de medicamentos”, indicó.
	“No рuedo hacerlo de la noche a la mañana, рorque va a imрlicar mejorar las 20 mil unidades médicas rurales; va imрlicar que funcionen todos los servicios de salud de segundo nivel”, añadió y dijo que también va a imрlicar mejorar el servicio y el abasto de medicinas.
	“Que no se vuelva a usar ni si quiera la рalabra cuadro básico”, sostuvo.
	Aseguró que se busca garantizar seguridad social desde la “cuna hasta la tumba”.
	Previó que habrá oрosición рorque quisieran que “siguiera la anarquía, el desorden, рorque ellos sacan рrovecho”.
	Esta mañana, el Jefe del Ejecutivo Federal fue cuestionado sobre el рosible рaro al que han llamado médicos residentes del рaís ante el retraso de los рagos de sus becas y el reembolso de un bono que les fue retenido.
	Recalcó que si a los médicos residentes se les debe, se les va a рagar. Aseguró que este mismo lunes se atenderá este asunto, y no рor рresión, sino рor convicción del Gobierno de México.
	“Es un asunto de рrinciрios рara nosotros, nosotros no рodemos traicionarnos a nosotros mismos. Tenemos que cumрlir, y ya he dicho: no рagar o retener el salario es рecado”, aseguró.""",

	"""Es un objetivo ambicioso, pero el presidente Andrés Manuel López Obrador se fijó un plazo de dos años para que México cuente con "un sistema de salud como el que tienen en Canadá, el Reino Unido o en Dinamarca".
	Pero, ¿cómo funcionan los sistemas de salud de esos países, descritos como "de lo mejor" por AMLO?
	La guerra de los sistemas de salud
	Al asumir el ambicioso compromiso, el mandatario dio algunas pistas, al destacar lo costoso que pueden ser algunos tratamientos para los mexicanos.
	"El cuadro básico, debemos desaparecer eso, ya ni lo voy a mencionar. El enfermo, el paciente debe tener todos los medicinamientos", dijo el jueves durante la inauguración de unas oficinas del Instituto Mexicano del Seguro Social (IMSS) en Michoacán.
	"Es una pena que sí se le da a una medicina que está en el cuadro básico, ¿pero si no está? 140.000 pesos un medicamento contra el cáncer, ¿de dónde lo va a sacar una persona humilde?, ¿qué vamos hacer, mandarlo a su casa?", se preguntó AMLO.
	Y el acceso efectivo de todos los mexicanos a servicios de calidad es otro de los retos del Sistema Nacional de Protección Social en Salud que el nuevo mandatario prometió reformar durante la campaña.
	La cobertura en México aumentó significativamente en el país luego de la introducción del Seguro Popular en 2004, pero está lejos de ser universal como en el caso de Reino Unido, Canadá y Dinamarca.
	Aquí te explicamos algunas de las principales características de los servicios de esos países, utilizados como ejemplo por AMLO.""",

	""" El Presidente se comprometió a pagar los adeudos a los médicos residentes, a priorizar la terminación de hospitales que heredaron y a garantizar el abasto de medicamentos. 
	El presidente Andrés Manuel López Obrador reiteró el compromiso de que en tres años, el sistema de salud de México será como los países nórdicos, en el que todos tendrán acceso a servicio médico y medicamentos de calidad gratuitos.
	“En tres años la atención médica y los medicamentos van a ser gratuitos y va a ser como un sistema nórdico, igual que Suecia o Canadá. No puedo hacerlo de la noche a la mañana porque va a implicar mejorar las 20 mil clínicas rurales y todo el tiradero de hospitales.
	“Ya comenzamos pero vamos a ir poco a poco para hacerlo de manera ordenada porque algunos quisieran que siguiera la anarquía porque ellos sacaban provecho pero se va a acabar”, dijo en conferencia de prensa.
	Recordó que heredó al menos 80 clínicas y hospitales inconclusos en el país que deberán terminar según la prioridad de cada zona, mientras que más de 80 mil trabajadores están laborando por honorarios desde año, sin contar con la corrupción en la compra de medicamentos que permitía muchas fugas de recursos y por ende, desabasto. Dijo que algunos hospitales tienen un avance de 30 por ciento, por lo que el gobierno federal priorizará aquellos que pueden terminarse a la brevedad y aquellos que más urgen por falta de clínicas o la lejanía de éstas en algunas zonas del país. El Presidente reiteró su compromiso de federalizar el sistema de salud para que sea de calidad como en los países nórdicos, tal como lo prometió desde su campaña. López Obrador dijo que aquellos médicos residentes recibirán sus sueldo y no habrá más retraso en los pagos de nómina “y no por la presión” de las manifestaciones, sino porque es un derecho, es justicia y es parte del nuevo sistema de este gobierno.
	"""]

author = ['', '', 'Jannet López Ponce']

url = ['https://nacionunida.com/2019/04/16/amlo-en-3-anos-vamos-tener-hospitales-y-medicinas-como-las-hay-en-suecia-y-canada/', 
	'https://www.bbc.com/mundo/noticias-america-latina-46762130', 
	'https://www.milenio.com/politica/amlo-reitera-compromiso-anos-sistema-salud-nordico']

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