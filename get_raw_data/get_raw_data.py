import pandas as pd
import json
from bunny import bunny
import json
import os


title = ["""Empresa vetada por AMLO de licitaciones de medicamentos consigue amparo""",
	"""AMLO buscará proveedores extranjeros para garantizar abasto de medicamentos para VIH""",
	"""Amparan a empresa por 'veto' de AMLO""",
	"""'Veto' a proveedoras daña competencia.-Coparmex""",
	"""AMLO quita veto a empresas que surten antirretrovirales""",
	"""Sector salud está infestado de corrupción; pero ya estamos limpiando: AMLO | Entérate""",
	"""Descubren 60 mil recetas falsas, las usaban para 'huachicoleo' de medicamentos""",
	"""Se indagará hasta saber si hubo influyentismo o corrupción en venta de medicamentos: AMLO""",
	"""Desabasto de medicinas para VIH obedece a que empresa sancionada tiene monopolio: AMLO | Entérate""",
	"""‘No al huachicol de medicinas’: la iniciativa para denunciar el desabasto""",
	"""Desabasto de medicamentos; recomendaciones de la OCDE, y más en columnas financieras de este 03/05/19""",
	"""El 10% de los medicamentos proviene del mercado negro, denuncian ONG""",
	"""ISSSTE, en riesgo de quiebra financiera; en julio tendrá problemas para operar: Zenteno""",
	"""¡Alerta! Estos son los padecimientos que el Ibuprofeno puede agravar""",
	"""Cuarta transformación acabará con ‘monstruosa’ desigualdad: AMLO""",
	"""Decomisan 60,000 recetas falsas para robar fármacos en el IMSS""",
	"""Policía Federal en la ruina: debe alrededor de 2 mil 500 millones""",
	"""Decepciona que con AMLO no se vea un cambio en la política de drogas: Kazatchkine""",
	"""De las promesas a las metas medibles: las claves del plan de seguridad de AMLO"""
	]

text = ["""
	Luego de que AMLO instruyó a la Oficial Mayor de la Secretaría de Hacienda impedir que tres empresas sigan –supuestamente– acaparando todas las ventas al IMSS y al ISSSTE (es decir, descansarlas de las licitaciones), una de ellas acudió ante las autoridades y ahora logró un amparo contra el mandato del Ejecutivo.

	De acuerdo con Reforma, la empresa Grupo Fármacos Especializados (Grufesa) no se quedó tan conforme con eso de ya no poder participar en la licitación para la compra de medicamentos que alista el gobierno federal y por ello solicitó un amparo… el cual ya le fue concedido por el juez Décimo de Distrito en Materia Administrativa, Francisco Migoni Goslinga.

	Con dicho amparo, queda suspendido el impedimento impuesto a la farmacéutica Grufesa para competir por contratos del gobierno, el cual le había sido aplicado el pasado 20 de marzo por el mismísimo presidente de México, Andrés Manuel López Obrador… que, aunque pesado en cuanto a poder en el país, pues no tiene facultades para aplicar una sanción que compete a otras instancias…

	“Con los documentos que anexó a su demanda, la empresa acredita que no ha sido sancionada, ni por la SFP, ni por la Comisión Federal de Competencia Económica (Cofece)“, señalan las fuentes judiciales… y es sólo el inicio, ya que la suspensión es provisional: el próximo 23 de abril se decide si se trata de una suspensión definitiva, lo que implicaría que Grufesa continuará participando en licitaciones por varios meses.

	En marzo pasado, AMLO instruyó a Raquel Buenrostro, oficial mayor de Hacienda, impedir que Grufesa, Maypo y Distribuidora Internacional de Medicamentos y Equipo Médico participen en licitaciones de contratos del gobierno relacionados con la compra de medicamentos.

	Esto debido a que consideró que dichas empresas violaron el artículo 28 Constitucional al concentrar el 62.4% de las ventas al IMSS y al ISSSTE. Peeeeeero, dicha sanción la aplicó –aparentemente– sin muchas pruebas, ya que indicó que ésta duraría “hasta que sepamos, a ciencia cierta, si no hubo en esas operaciones corrupción y tráfico de influencias“.

	Y, como ya se comentó, pues muy el presidente, pero AMLO no tiene los pelos de la burra en la mano en cuanto a materia de prácticas monopólicas. Es la Cofece la que decide sobre ese asunto… además de que para sacar del juego a cualquier empresa, es necesario un procedimiento administrativo ante la Secretaría de la Función Pública.
	""",
	"""
	Tras la manifestación de ciudadanos y asociaciones civiles como el Movimiento Nacional de Lucha contra el VIH (Virus de Inmunodeficiencia Humana) por la escasez de antirretrovirales y otros medicamentos controlados para pacientes con el virus, en la conferencia mañanera de este viernes 3 de mayo, AMLO prometió que habrá medicamentos para los pacientes y, además, el gobierno buscará otras opciones de proveedores en el extranjero —todo con la ayuda de los propios civiles.

	De acuerdo con AMLO, el único proveedor que lleva la concesión para estos medicamentos impone un par de condiciones para su venta, por lo que lo exhortó para que no jueguen “a las vencidas”: “Porque no van a faltar los medicamentos, los vamos a comprar en cualquier país del mundo“.

	Aunque el mandatario no dio un nombre en específico, sí se refirió a una de las tres empresas que vendía al IMSS (Instituto Mexicano del Seguro Social) y el ISSSTE (Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado). La venta estaba por 35 mil millones de pesos en medicamentos. Y ante la escasez de los medicamentos y las demandas de los pacientes, el gobierno se mantendrá en contacto con esta empresa.

	En el centro de la ciudad, integrantes del Movimiento Nacional de Lucha contra el VIH se manifestaron el día de ayer en la Estela de Luz, en las inmediaciones de la Secretaría de Salud, precisamente por la escasez de antirretrovirales en distintos estados del país como Oaxaca, Chihuahua, Tabasco, Veracruz y Baja California.

	Y mientras esto sucedía, el IMSS denunció el robo de medicamentos antirretrovirales para VIH, en el Hospital General de Zona 29 del IMSS (Instituto Mexicano del Seguro Social), acentuando la gravedad de este caso.
	""",
	"""
	NaN
	""",
	"""
	NaN
	""",
	"""
	AMLO hará una excepción en la compra de medicamentos para pacientes con VIH, con el fin de solucionar el desabasto.

	El desabasto de medicamentos mantienen en total incertidumbre a las personas portadoras de Virus de Inmunodeficiencia Humana (VIH). El sector salud no cuenta con suficientes reservas para atender a dichos pacientes. Este viernes el presidente Andrés Manuel López Obrador (AMLO) anunció que se hará una excepción en la compra de medicamentos antirretrovirales para pacientes con VIH del sector sanitario público, para solucionar el desabasto.

	La empresa que surte esas medicinas al Gobierno es una de las tres que fueron vetadas porque se descubrió que prácticamente monopolizaron el mercado para el Instituto Mexicano del Seguro Social (IMSS) y el Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado (ISSSTE).

	"Me plantearon de que una de las empresas que abastecía más al Gobierno es de las que tienen la concesión para vender esos medicamentos. Como se trata de un asunto delicadísmo, humano, se hizo una excepción, pero al mismo tiempo estamos buscando en el extranjero (…) una de las empresas, las tres que dijimos, que hasta que no se investigara cómo es que tres empresas le vendían al Seguro y al ISSSTE 35 mil millones de pesos de medicamentos, tres, y tenemos que investigar si no hubo corrupción o influyentismo. -AMLO-."

	El mandatario advirtió que el problema del desabasto de antirretrovirales ya se está resolviendo, destacó que cuando le plantearon que los medicamentos para pacientes con VHI los vendía una de las tres empresas que centralizaba la adquisición de fármacos y que fue vetada para ser investigada por corrupción, hizo una excepción para volver adquirir con ellos debido a que "es un asunto humanitario", refiere. 

	El presidente también declaró respecto a la compra de medicamentos en general y señaló que las empresas no quieren venderlas al Gobierno y exhortó a los proveedores a actuar con honestidad, “que no estén queriendo jugar a las vencidas”, les dijo, porque comprarán las medicinas “en cualquier país del mundo”.

	El pasado jueves, el IMSS dio a conocer el robo de antirretrovirales contra el VIH y medicamentos controlados.

	A través de un comunicado, se explicó que el hurto ocurrió en el Hospital General de Zona número 29, en la Ciudad de México. El nosocomio está ubicado en la alcaldía Gustavo A. Madero.

	"Los hechos fueron notificados esta mañana por la trabajadora encargada de la farmacia de dicha unidad médica, quien encontró violados los portacandados de tres refrigeradores y de la gaveta donde se resguardaban tanto fármacos como antirretrovirales, para el tratamiento del Virus de Inmunodeficiencia Adquirida (VIH)", señaló la institución.
	""",
	"""
	NaN
	""",
	"""
	Porque el huachicoleo no es exclusivo de la gasolina: en Torreón descubrieron 60 mil recetas falsas del IMSS que usaban para 'ordeñar' medicamentos.

	En México, los tentáculos de la corrupción siguen tocando todos los rincones. A pesar de los esfuerzos del nuevo gobierno por derrocarla –AMLO la considera como la peor amenaza para la democracia–, los sobornos, las falsificaciones y el encubrimiento permean en todas las instituciones y sistemas. 

	Ejemplo de ello es el Instituto Mexicano del Seguro Social, donde se falsifican recetas médicas para ordeñar cientos de medicinas. El pasado 25 de abril en Torreón, Coahuila, el IMSS halló, en el Hospital General de Zona 16, cuarenta cajas con blocs con 60 mil recetas presuntamente falsas, las cuales ya fueron aseguradas por el instituto, reveló un reportaje de Diego Enrique Osorno en Milenio. Estas se usarían para "ordeñar" medicamentos de todo tipo. 

	Estos recetarios son elaborados por la empresa Formularios de México SA de CV para luego ser entregados en Ciudad de México a la Dirección de Prestaciones Médicas del IMSS, desde donde se distribuyen a las distintas delegaciones estatales del país, donde son recibidas por una figura oficial llamada Controlador Delegacional de Recetarios e Incapacidades, la cual tiene la función de distribuir en los diversos hospitales de su delegación los blocs de los recetarios.

	Estos blocs de recetas falsas son finalmente recibidos por los departamentos de Abastecimiento y Almacén de cada hospital del IMSS, quienes están encargados de repartirlos a los médicos que laboran en la institución para que puedan atender a los pacientes que tienen seguridad social, por lo que deben recibir medicamentos de forma gratuita.

	Pero antes de ser enviados a los médicos, los recetarios son reemplazados por otros falsos, que aunque son muy similares a los originales, e incluso tienen el mismo número de folio, "tras un análisis hecho por peritos especializados en documentoscopía se establecieron alteraciones en tipografía, color, diseño y tintas".

	"os recetarios originales son usados para robar los medicamentos, entre los que destacan los necesarios para atender la diabetes, así como el material oncológico de quimioterapias de las personas que padecen cáncer o los antirretrovirales de pacientes con VIH. Mientras tanto, los médicos generales expiden —la mayoría de las veces sin saberlo— los recetarios apócrifos suplantados de manera previa por las redes de corrupción, de tal forma que cuando los pacientes llegan a las farmacias a solicitar sus medicamentos, estos ya no se encuentran disponibles a causa del huachicoleo."

	El propio AMLO ha reconocido que el robo de medicinas también es "huachicoleo" y advirtió que trabajarían en ese problema. Sin embargo, en los pocos meses que lleva de administración parece que los esfuerzos solo se han concentrado en conferencias mañaneras tediosas.
	""",
	"""
	Las investigaciones iniciadas por el gobierno federal en torno a la forma como se otorgaron los contratos para la venta de medicinas y equipo médico a tres empresas, que el sexenio pasado concentraron más de 65 por ciento del total de adquisiciones gubernamentales, llegarán hasta el esclarecimiento del posible influyentismo y corrupción que haya rodeado estas operaciones, reiteró el presidente Andrés Manuel López Obrador.

	En su conferencia matutina, López Obrador aseveró que ese fue un procedimiento "a todas luces irregular", pues de los 4 mil millones de dólares de medicinas que adquirió el gobierno, 60 por ciento provienen de tres empresas. "No podemos acusar que hay corrupción o influyentismo porque se están haciendo investigaciones", situación que están tratando la Oficialía Mayor de Hacienda, encargada actual de las compras, y la Secretaría de la Función Pública.

	¿Hasta dónde llega la investigación? Es conocido que estas empresas tenían padrinos políticos; ahí están nombres que están circulando, como Beltrones, Gamboa. ¿Hasta dónde llegará la investigación?

	Hasta saber por qué les daban estos contratos jugosos y quiénes protegían estas empresas, si había o no influyentismo. Saber todo.

	Señaló que transparentar las cosas ayuda al gobierno a combatir la corrupción, y citó que el dueño de una de las empresas vetadas de las licitaciones para la adquisición de medicinas este año fue organizadora de los foros sobre salud en el periodo de transición.

	"Ventilar estas cosas ayuda a que todos participemos, porque son como la humedad: se meten por todos lados y estamos en un tiempo en que lo viejo no acaba de morir y lo nuevo no acaba de nacer. Es un proceso de transición".
	""",
	"""
	NaN
	""",
	"""
	En estos días, organizaciones civiles se han manifestado ante el desabasto de medicinas en el IMSS (Instituto Mexicano del Seguro Social) o el ISSSTE (Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado) —tal como lo hicieron los ciudadanos en CDMX al denunciar la escasez de antirretrovirales para pacientes con VIH (Virus de Inmunodeficiencia Humana). En este contexto, surgió la iniciativa No al #HuachicolDeMedicinas para reportar el desabasto de medicamentos e insumos de salud, denunciar la demora en la entrega de fármacos y medicinas —porque el problema no es sólo cuestión de la gasolina, también el sector salud cuenta con sus deficiencias y su impacto negativo entre los pacientes.

	Y para poder llevar a cabo la denuncia ciudadana, surgió la plataforma huachicoldemedicinas.org, donde se podrán denunciar los problemas de desabasto de medicamentos —en un sitio que reúne la voz de organizaciones civiles para denunciar los problemas, de acuerdo con Mauricio Merino, coordinador general de Nosotrxs.

	La plataforma no es nueva, desde el 1 de marzo pasado se activó el portal y en la cuenta hasta el 7 de mayo, las organizaciones civiles han registrado casi 143 denuncias de desabasto de medicamentos. Entre los datos están:


    CDMX con 29 denuncias.
    Sonora con 20.
    Jalisco con 18.
    Puebla con 10.

    El objetivo, además de ser un canal para las denuncias, es que estas lleguen a las autoridades, en este caso a la Secretaría de Salud mediante el ISSSTE y el IMSS para que se tomen cartas en el asunto y que se resuelva el problema del huachicol de medicinas en México, debido a que la corrupción dejó las puertas abiertas para el desvío de los medicamentos y la ineficacia de las compras.

    Ahora, reto será de esta administración —el gobierno de AMLO— que si bien con esta no comenzó el desabasto y el desvío de los medicamentos, tendrá que hacer ajustes a la estructura para monitorearlo —tal como lo hacen con las tomas clandestinas de los ductos de Pemex— y erradicar poco a poco el problema, eso sí, con la participación de la sociedad.
	""",
	"""
	NaN
	""",
	"""
	Al igual que en las demás partes de la administración, el gobierno federal pretende que la Secretaría de Hacienda y Crédito Público (SHCP) concentre las compras de medicinas, lo que ya generó un desabasto de algunos insumos como los antirretrovirales, deploró Luis Adrián Quiroz, director de Derechohabientes Viviendo con VIH/SIDA del IMSS (DVVIMSS).

	“Raquel Buenrostro (la oficial mayor de la SHCP) va a ser la súpercompradora y es preocupante, la semana pasada, por ejemplo, se anunció que habrá retrasos en la compra de libros de texto”, deploró el activista, quien recordó que “en un hecho histórico, tuvimos que volver a salir a las calles después de 15 años y exigir que las medicinas estén disponibles”.

	El plan de combate a la corrupción en el sector salud, que lanzó el presidente Andrés Manuel López Obrador –consistió, entre otros, en vetar a tres de los proveedores farmacéuticos más importantes del gobierno federal–, atrasó las convocatorias para comprar tratamientos de enfermedades crónicas y degenerativas, como lo documentó Proceso esta semana.

	El académico Mauricio Merino aplaudió la voluntad de AMLO de acabar con la corrupción, pero sostuvo que “el objetivo final de la política pública es que las medicinas lleguen a los pacientes; cualquier decisión que ponga en riesgo la vida de las personas debe ser muy cuestionada”.

	“Lo que pasó con el huachicol de gasolina, no queremos que pase con las medicinas: se cortó de tajo”, lamentó Quiroz, y abundó: “Nos dijeron que pagáramos nosotros las medicinas, que nos reembolsarían, pero un antirretroviral puede costar hasta 17 mil 500 pesos mensuales”.

	Según activistas, el “huachicol” de medicinas en el sistema de salud público ocurre en cada etapa de este mercado de alrededor de 135 mil millones de pesos anuales: desde el proceso de compra-venta con sobreprecios pactados entre empresas farmacéuticas e instituciones, hasta el robo hormiga en los centros de salud, pasando por los desvíos de insumos en las cadenas de abasto.

	“El 10% de los medicamentos totales proviene del mercado negro, que representa entre 13 y 30 mil millones de pesos de ganancias y pone en riesgo el derecho a la vida”, resaltó Luis Fernando Fernández, el director ejecutivo de la organización política NosotrXs, que presentó hoy una plataforma para que los pacientes, familiares y médicos denuncien en tiempo real el desabasto de medicinas en el sistema de salud pública.

	“Detrás de estas cadenas de corrupción hay vidas”, resaltó Merino. En las instituciones de salud, añadió, “los inventarios están en orden en el papel, pero luego descubrimos que las medicinas están en venta en la farmacia particular que está a la vuelta”.

	“No es un problema nuevo. No es un problema que nació en el gobierno actual. Es un problema muy antiguo que ha venido afectando sistemáticamente los derechos de las personas”, insistió el investigador del Centro de Investigación y Docencia Económicas (CIDE).

	“Para una persona con cáncer, recibir su tratamiento a tiempo hace la diferencia entre la vida y la muerte”, dijo Brenda Ponce, directora de la Asociación Mexicana de Lucha contra el Cáncer.

	Según la activista, los pacientes son los primeros testigos y los principales afectados por el robo de medicinas, pero prefieren “no denunciar, por temor a ser cancelado su tratamiento o que el medico mismo les niegue su tratamiento”.
	""",
	"""
	El funcionario del Instituto, Mario Zenteno, expuso que los pasivos que dejaron administraciones anteriores llegan a los 19 mil millones de pesos.

	El Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado (ISSSTE) está en riesgo de quiebra financiera y tendrá problemas para operar en julio, advirtió el director de Normatividad de Administración y Finanzas del Instituto, Mario Zenteno.

	“Es la quiebra que tenemos y prácticamente vamos a tener problemas para operar en julio si no hay ampliación líquida, si no nos pagan los estados y las secretarías lo que nos deben. Estamos operando en austeridad a todo lo que da. En el Instituto pagamos alrededor de mil millones por año de pasivo“, puntualizó durante su comparecencia ante la Comisión de Salud del Senado.

	Asimismo, Zenteno Santaella dio a conocer que la nueva administración del ISSSTE encontró desorden y falta de apego a las normas en el ejercicio presupuestal, lo que provocó 17 mil 488 juicios laborales en curso.

	Además, expuso que los pasivos que dejaron administraciones anteriores llegan a los 19 mil millones de pesos, de los cuales 10 mil millones se incrementaron solo en el último año.

	Denunció que se compraron medicamentos a sobreprecio, lo cual rebasó mil por ciento del costo real.

	Sin embargo, dijo que pese a la mala situación en que han encontrado la institución aún es tiempo de rescatarla.

	El encargado de Administración y Finanzas de la Secretaría de Salud, Pedro Flores Jiménez, dijo a los senadores que en los hospitales de alta especialidad, organismos públicos y descentralizados la demanda de recursos humanos y materiales asciende a 10 mil millones de pesos y todos los días los servicios crecen.

	Señaló que el caso de los médicos residentes se reclama una figura jurídica, pues ellos ejercen una labor fundamental en institutos y hospitales en favor de la salud en México.

	En tanto, el director de Administración del Instituto Mexicano del Seguro Social, Flavio Cienfuegos, explicó que en  2018, 43 por ciento de las personas afiliadas gastó 24 mil 300 millones de pesos en servicios privados, por atraso y deficiencia en la atención y tratamiento a los derechohabientes y sus familias.

	Esto no solo contribuye al deterioro de la salud de los derechohabientes, sino que significa tiempo y gasto para su recuperación.

	Al hablar de la adquisición de medicamentos, Cienfuegos Valencia afirmó que 69 por ciento el IMSS los compraba a cinco proveedores, que entre 2013 y 2019 vendieron al instituto 151 mil 243 millones de pesos.

	Al respecto, Cienfuegos Valencia dijo que las condiciones actuales en los contratos son insuficientes para exigir que se cumpla con la entrega de medicamentos e imponer sanciones proporcionales al impacto que ocasionan.
	""",
	"""
	Según un estudio el Ibuprofeno, puede agravar anginas, rinofaringitis, otitis, tos. Las complicaciones se observaron en tratamientos breves.

	La agencia francesa del medicamento (ANSM) lanzó una advertencia a médicos y pacientes por los riesgos que ha constatado por el uso del ibuprofeno y del ketoprofeno, que pueden agravar infecciones que se pretenden tratar, y como medida de protección ha pedido una investigación sobre esos medicamentos en todo Europa.

	De acuerdo con el diario Excélsior, la Agencia Nacional de Seguridad del Medicamento y de los Productos Sanitarios (ANSM) que en junio pasado había lanzado una investigación farmacológica encargada a sus centros de Tours y Marsella, emitió el pasado jueves una serie de recomendaciones, en primer lugar, privilegiar el paracetamol al ibuprofeno y el ketoprofeno en caso de dolor o fiebre. Sobre todo cuando se trate de una infección como anginas, rinofaringitis, otitis, tos, infección pulmonar, así como para una lesión cutánea o varicela.

	Un portavoz de la ANSM explicó el pasado viernes a EFE que "a petición francesa" se va a llevar a cabo un análisis colegial con sus homólogos europeos.

	El portavoz de ANSM recordó que las autorizaciones de los medicamentos se hacen para toda Europa, no sólo para Francia, y que es en esa escala en la que se tiene que hacer una reevaluación de la relación riesgo-beneficio de esos productos.

	La ANSM han dado unas reglas de buen uso de estos dos antiinflamatorios, empezando la de utilizar "la dosis mínima eficaz, durante la duración más corta", detener el tratamiento en cuanto desaparecen los síntomas, no prolongarlo más de tres días en caso de fiebre, ni más de cinco si hay dolor.

	Las recomendaciones derivan de un estudio que había encargado en junio de 2018 a sus centros regionales de Tours y Marsella, que concluyeron que hay una serie de infecciones, en particular por estreptococo, que podrían empeorar por la toma de estos dos medicamentos.

	Esas complicaciones se observaron al cabo de periodos de tratamiento muy breves (de dos a tres días) cuando el ibuprofeno o el ketoprofeno se habían recetado (o utilizado en automedicación) para fiebre, problemas cutáneos benignos de aspecto inflamatorio, respiratorios o del sistema otorrinolaringológico.

	En los casos estudiados, que se remontan a un periodo prolongado iniciado el año 2000, los investigadores franceses analizaron 337 de complicaciones infecciosas con ibuprofeno y 49 con ketoprofeno que tuvieron un carácter severo y estuvieron en el origen de hospitalizaciones, secuelas e incluso muertes.
	""",
	"""
	En la conmemoración del 157 aniversario de la Batalla de Puebla, el presidente explicó que eso significa desterrar la corrupción, terminar con la impunidad y los privilegios.

	El presidente Andrés Manuel López Obrador reconoció hoy que existe una «monstruosa desigualdad» económica y social, por lo que ahora, desde abajo, entre todos y de manera pacífica, sin violencia, llevaremos a cabo la Cuarta Transformación de la vida pública de México.

	En la conmemoración del 157 aniversario de la Batalla de Puebla, explicó que eso significa desterrar la corrupción, terminar con la impunidad y los privilegios, pues «no puede haber gobierno rico con pueblo pobre».

	En su mensaje, el mandatario federal hizo un recorrido histórico por lo que llama las tres primeras transformaciones del país: la independencia, la reforma y la revolución.

	Recordó que José María Morelos y Pavón defendió la justicia «porque hasta la fecha, por desgracia, hay una monstruosa desigualdad económica y social, unos cuantos lo tienen todo y la mayoría carece hasta de lo más indispensable».

	 Dijo que Francisco I. Madero afimaba que el pueblo de México tiene hambre y sed de justicia, y «va a ser saciada su hambre y su sed en la Cuarta Transformación».

	«Vamos a atender a todos, vamos a escuchar a todos, vamos a respetar a todos, pero le vamos a dar preferencia a la gente humilde. Por el bien de todos, primero los pobres», subrayó.

	Dijo que su gobierno ya empezó con acciones como dar el doble de pensión a adultos mayores, es decir, dos mil 550 pesos, y se dará una suma igual a todas las niñas y niños con discapacidad.

	Además, este año se entregarán alrededor de 10 millones de becas para estudiantes de escasos recursos económicos de primaria, secundaria y preparatoria, y aquellos que cursen una carrera universitaria o de nivel superior serán apoyados con 2,400 pesos mensuales para que terminen sus estudios.

	Señaló que los pasados gobiernos nunca hicieron nada por los jóvenes desempleados y sólo los etiquetaron como «ninis», porque ni estudian ni trabajan, mientras que ahora van a ser contratados como aprendices y su administración les dará un sueldo de 3,600 pesos mensuales mientras se capacitan.

	Añadió que resolverá los problemas en educación y salud, garantizará el derecho del pueblo a la atención médica y medicamentos gratuitos, mediante el Instituto de Salud para el Bienestar, «no eso que llaman Seguro Popular, que ni es seguro ni es popular».

	Hizo el compromiso de que en una semana vendrá el director del Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado (ISSSTE), Luis Antonio Ramírez Pineda, para que se termine el hospital que esta a punto de empezar a operar.
	""",
	"""
	La investigación detectó que antes de ser enviadas a los médicos, las recetas son reemplazadas por las apócrifas que mantienen un amplio parecido en lo general e incluso tienen el mismo número de folio. 

	Un reporte interno del Instituto Mexicano del Seguro Social (IMSS) encontró en el Hospital General de Zona 16 en Torreón, Coahuila 40 cajas con 60,000 recetas presuntamente apócrifas.

	La investigación detectó que antes de ser enviadas a los médicos, las recetas son reemplazadas por las apócrifas que mantienen un amplio parecido en lo general e incluso tienen el mismo número de folio.

	Tras un análisis hecho por peritos especializados en documentoscopía se establecieron alteraciones en tipografía, color, diseño y tintas, de acuerdo con el diario Milenio.

	“Tras la suplantación, los recetarios originales son usados para robar los medicamentos, entre los que destacan los necesarios para atender la diabetes, así como el material oncológico de quimioterapias de las personas que padecen cáncer o los antirretrovirales de pacientes con VIH”, dice la investigación No. COA237/2019.

	En ese sentido, los médicos generales expiden —la mayoría de las veces sin saberlo— los recetarios apócrifos suplantados de manera previa por las redes de corrupción de tal forma que cuando los pacientes llegan a las farmacias a solicitar sus medicamentos, estos ya no se encuentran disponibles.
	""",
	"""
	La Policía Federal reconoce que debe alrededor de 2 mil 500 millones y no cuenta con dinero suficiente para pagar.

	La corporación de la Policía Federal, está a punto de desaparecer y ya se ha anunciado que será gradualmente desplazada por la nueva Guardia Nacional y a pocos meses de ello ocurra, el portal Animal Político obtuvo documentos que acreditan que la corporación tiene un adeudo de casi 2 mil 500 millones de pesos por pagos pendientes en múltiples conceptos, desde gasolina para sus coches, pasando por viáticos y hospedajes, hasta indemnizaciones para sus elementos.

	Y de acuerdo con el portal la dependencia reconoce que no cuenta con dinero suficiente para pagar dichos adeudos que van en ascenso. Sus recursos apenas le alcanzan para mantener su operación.

	Animal Político obtuvo vía transparencia datos oficiales que evidencian el tamaño de la crisis económica que tiene la corporación.

	En el oficio número PF/OCG/DGE/1309/2019, la Policía Federal detalla que tiene un adeudo total, con corte a febrero pasado, de 2 mil 460 millones 248 mil 776 pesos con 24 centavos. Dicha cantidad es resultado de la falta de pago por bienes y servicios en 14 rubros distintos.


	El adeudo más elevado es de 1 mil 308 millones de pesos y corresponde a servicios de traslado y viáticos no cubiertos. En diversas ocasiones en los últimos años este problema ha quedado al descubierto con el reclamo de hoteleros que han hospedado a elementos de la corporación sin recibir el pago pactado, lo que a su vez ha provocado que la Policía Federal tenga incluso que dejar a sus efectivos en campamentos improvisados.
	
	El segundo adeudo más alto es de casi 533 millones de pesos por servicios básicos no cubiertos, entre ellos pagos de agua y de luz. Le sigue una deuda de 234 millones 283 mil pesos por concepto de vestuario, blancos y prendas de protección; y otra de 92 millones 635 mil pesos por pagos adeudados a personas que prestaron diversos servicios profesionales, técnicos, entre otros.

	Además, también tienen adeudos por  adeudos de 64 millones 645 mil pesos en alimentos y utensilios; de 28 millones 667 mil pesos en medicamentos y productos químicos; de 24 millones 982 mil pesos en servicios financieros, bancarios y comerciales; de 23 millones 400 mil pesos en diversos materiales de administración; y de más de 13 millones 724 mil pesos en pago de diversos arrendamientos.

	La Policía Federal también registra un adeudo de 4 millones 861 mil pesos en la partida destinada al pago de combustibles, lubricantes y aditivos.

	Incluso se tiene registrado un adeudo de más de 450 mil pesos por servicios de publicidad y comunicación social; y de 409 mil pesos en herramientas y refacciones menores.

	Finalmente registra una deuda de casi 200 mil pesos, derivado de resoluciones judiciales adversas, pago de indemnizaciones y liquidaciones, así como pérdidas en el erario.
	""",
	"""
	En México es urgente un cambio radical con respecto a la política de drogas , sin embargo, en lo que va de la administración del presidente Andrés Manuel López Obrador , no se ha visto voluntad para llevar a cabo este cambio, dijo en entrevista con Proceso Michel Kazatchkine director ejecutivo del Fondo Mundial de Lucha contra el SIDA, la Tuberculosis y la Malaria y representante de la Comisión Global para Política de Drogas.

	“Es tiempo de cambiar radicalmente la política de drogas en México”, afirmó Kazatchkine en el marco del congreso sobre reducción de daños por las drogas HR19 organizado por Harm Reduction International y que tuvo lugar en Oporto, Portugal.

	“Pero en lo que va de esta administración no hemos visto una fuerte determinación para cambiar”, lamentó.

	Consideró que no se obtendrá un resultado diferente al de sexenios anteriores si se quiere seguir con la misma política de guerra contra las drogas , “que como se ha visto ya se ha perdido” y ha causado la muerte por asesinatos dolosos de unas 241, 232 personas desde 2006 a la fecha, además de un clima de violencia en todo el país y un número indeterminado de personas encarceladas en el contexto del combate contra el narco emprendido por el gobierno de Felipe Calderón y continuado por el de Enrique Peña Nieto.

	“Tiene que haber un cambio de dirección que sea diferente a los gobiernos anteriores si realmente se quiere afrontar el problema”, argumentó el experto francés.

	A su modo de ver, cualquier intento para frenar los índices de violencia como es la creación de la Guardia Nacional, no tendrá éxito si no se acompaña con un cambio de paradigma dirigido hacia la salud pública y la reducción de daños para quienes consumen drogas.

	“Se tiene que ver a los usuarios de drogas desde un punto de vista de salud pública y no desde una perspectiva criminal”, remarcó.

	“La Guardia Nacional no será efectiva si no va acompañada de un cambio en las políticas sobre consumo de drogas y en la percepción que se tiene”, argumentó

	“La guerra contra las drogas ha fracasado”, dijo al abrir el congreso la Alta Comisionada de la ONU para Derechos Humanos Michelle Bachelet quien detalló que entre 2000 y 2015 ha habido un aumento del 60% en muertes relacionadas a las drogas a nivel mundial: 450 mil muertes sólo en 2015.

	Kazatchkine asistió a la cumbre HR19 (28 de abril al 1de mayo) en representación de la Comisión Global para Política de Drogas fundada por varios expresidentes latinoamericanos como Ernesto Zedillo (México), Fernando Henrique Cardoso (Brasil) y César Gaviria (Colombia). Hizo hincapié en lo absurdo que han sido las políticas en México que han dado como resultado un sin fin de arrestos por esta causa.

	“Hemos discutido extensamente la situación en México porque la situación es realmente trágica, y al mismo tiempo, en términos de políticas es absurda”, lamenta.

	Cuenta que es inconcebible seguir con el mismo modelo pues el consumo de drogas en México es menor que el de los niveles de consumo en otros países. “Es una paradoja, que en un país con bajo consumo, las políticas han traído las tragedias que estamos viendo”, subraya.

	“Es realmente absurdo”, lanza Kazatchkine, quien considera que es fundamentalmente incorrecto involucrar al ejército en el cumplimiento de la ley sobre drogas.

	Detalla que ha habido un sin fin de arrestos por esta causa y que las cifras han aumentado, al menos 50 mil personas al año enfrentan a la justicia criminal por posesión y de ellos entre el 60% y 70% es solamente por posesión para consumo personal.

	“La base de esta política es ridícula”, sentenció Kazatchkine quien habló sobre la urgencia de que exista en México un cambio profundo de paradigma en la comprensión y enfrentamiento del problema de las drogas.

	A pesar de la ley adoptada en México en 2009 en la que se despenalizó el consumo personal de drogas en México, la situación en el terreno es diferente. Los policías, el ejército, el sistema judicial no aplican la ley e incluso la desconocen.

	La ley de 2009 estipula como dosis para consumo personal e inmediato 2 gramos de opio, 50 miligramos de heroína, 5 gramos de marihuana, 500 miligramos de cocaína, 40 miligramos de metanfetamina y 0,015 miligramos de LSD.

	“Y además la cantidad establecida por la ley para el consumo personal es muy pequeña, es ridícula”, criticó por su parte Ann Fordham directora ejecutiva del Consorcio Internacional sobre Política de Drogas (IDPC por siglas en inglés).

	Para Fordham lo que es imperativo es tener muy claro que si se quiere reducir la prevalencia del consumo, la represión no es la salida. Es la reducción de daños, la perspectiva de derechos humanos y de salud pública lo que reduce la violencia y a la larga reduce el consumo.

	“La ley es liberal en teoría, pero en la realidad no se refleja en las calles ”, dijo a su vez Jaime Arredondo doctor en Salud Pública de la Universidad de San Diego, California y Profesor Investigador del programa de política de Drogas del CIDE Aguascalientes, quien consideró que no basta sólo con cambiar la ley, sino que la normativa debe ser dada a conocer a todos los involucrados en el sistema judicial, incluyendo además a los policías y encargados de guardar el orden.

	La cantidad permitida es “increíblemente ridícula” y otra cosa que ocurre es que se ponen multas a los consumidores y a veces son tan desproporcionadas que la gente no puede pagarlas y terminan en el sistema criminal de justicia, dijo.

	“La reforma a la ley es fallida. No está funcionando, se sigue llevando a la estación de policía a quienes consumen, aunque tengan en su posesión una cantidad acorde a la ley”, deploró Arredondo.

	¿Y la amnistía para mujeres condenadas por delitos menores relacionados a las drogas?

	En opinión de Kazatchkine es trágico ver cómo tantas personas van a la cárcel por esta razón, especialmente las mujeres. Relató que durante su estancia en México el pasado septiembre visitó una cárcel para mujeres en dónde se entrevistó con varias internas, lo que calificó de una de las experiencias “más conmovedoras” que ha tenido.

	Mencionó el caso de una de ellas que atravesaba por una situación económica muy difícil pues tenía que mantener a sus dos hijos y se prestó a trasladar droga. “En su primer viaje la detuvieron y fue sentenciada a 25 años de cárcel, ahora cumple su doceavo año de condena, tiene 37 años y fue muy impresionante hablar con ella”.

	“Son encarcelamientos absolutamente inútiles”, sostiene el experto francés, quién se preguntó qué pasó con la promesa de la Secretaria de Gobernación Olga Sánchez Cordero en el sentido de amnistiar a miles de mujeres, especialmente indígenas, que están presas en circunstancias similares por delitos de microtráfico o faltas menores relacionadas a la cadena de la droga.

	Esta administración prometió durante su campaña electoral dar amnistía a estas mujeres, pero el tema ha estado completamente ausente de la agenda del presidente López Obrador, criticó Fordham.

	“Tenemos esperanzas en que Sánchez Cordero traiga una nueva dinámica sobre el tema”, continuó Kazatchkine.

	“Además hay muchas cosas interesantes sucediendo ahora que también nos trae esperanzas como es la Ley sobre consumo de Cannabis”, agregó.

	“Esperamos la despenalización del uso, de la posesión y el esfuerzo de apoyar a personas que quieren sembrar la planta, hasta cierto límite, para consumo personal, así como la creación del Instituto de Cannabis para evitar riesgos de comercialización y que trabajará sobre cómo proteger a la gente y a los productores pequeños”, esbozó.

	“Esta es la fotografía y es tiempo para México de poner fin a esta especie de bola de nieve cargada de violencia, criminalización, más violencia, más muertes, más penalización”, remarcó.

	“La regulación de la Cannabis debe ser el primer paso”, dijo el experto quien consideró que México debe ir más allá y dirigirse a la despenalización en general de todas las drogas e implementar políticas dirigidas hacia la salud y los derechos humanos.

	Comenta que, sumado a todo lo anterior, no ha cesado la guerra contra las drogas que disparó el número de asesinatos en el país en los sexenios anteriores y “que por lo que vemos no ha cambiado en los primeros meses del gobierno del presidente Andrés Manuel López Obrador y las muertes violentas siguen aumentando”.

	Para Kazatchkine “las políticas prohibicionistas basadas en la represión de la producción, la distribución, así como la criminalización del consumo, no han producido los resultados esperados”.

	“Estamos más lejos que nunca del objetivo proclamado de erradicación de las drogas”, sostuvo Kazatchkine, mencionando informes que indican que América Latina sigue siendo el mayor exportador mundial de cocaína y mariguana, se ha convertido en creciente productor de opio y heroína, y se inicia la producción de drogas sintéticas.

	“Si México da el paso hacia la regulación del Cannabis, y creo que sigue siendo el plan, tendrá un efecto muy interesante en Estados Unidos ya que de un lado de la frontera está Canadá que ya lo legalizó y en la frontera sur estaría México”, opinó Fordham.

	A su modo de ver “Además de Canadá y Uruguay a nivel mundial la tendencia es a la legalización, hemos visto muchos signos a nivel global en este sentido, y el sistema internacional terminará por absorber la regulación de la mariguana”.

	“Además, agregó el experto francés, el gobierno de México podría convertir el mercado de Cannabis en uno de los proveedores del sector médico. La paradoja es que México compra algunas de estos medicamentos en el extranjero cuando se puede destinar algunas cosechas a este mercado médico que está creciendo gracias a las propiedades curativas de la planta”.

	No obstante, el médico francés expresó su temor de que después de legalizar la Cannabis, la comunidad internacional cierre las puertas hacia otras drogas, “cuando es fundamental eliminar la prohibición en general”.

	“Mientras la prohibición siga ahí, el mercado ilegal seguirá ahí, y mientras siga la prohibición continuará la vigilancia del cumplimiento de la ley, y las políticas que provocan un daño tremendo”, argumentó Kazatchkine.

	En su opinión la demanda de drogas seguirá existiendo y si no se encuentra de forma legal, será en el mercado ilegal, con todas sus malas consecuencias: adulteración, mafias, epidemias de VIH, hepatitis, corrupción, violencia e inseguridad. El comisionado insistió en la necesidad de legalizar todos los estupefacientes: “Los gobiernos deberían apostar por un uso seguro de estas sustancias. Hay que enfrentarse al mundo tal como es, y uno libre de drogas no existe”.

	Confía en que si México legaliza la Cannabis “será fundamental para la región y para el mundo, pero, desafortunadamente esto está muy alejado de ser el final de la historia”.

	Es imperativo “acabar con la prohibición de todas las drogas para que el Estado esté en control, para que la gente sepa qué es lo que está comprando y consumiendo”.

	“Esto va a requerir de cambios mayores, requerirá también que el gobierno sea muy muy valiente, debido a las fuerzas internas que se mueven en México y para ser honestos, viendo los primeros meses de esta administración no nos sentimos muy animados de que las cosas vayan a cambiar”, admitió.

	“Lopez Obrador tiene una gran oportunidad de cambiar las cosas, gracias al apoyo que tiene de la gente y, sobre todo, habló mucho sobre el tema durante su campaña”, recordó Kazatchkine de la Comisión Global sobre Política de Drogas.

	“No creo que López Obrador tenga idea de lo que quiere hacer en política de drogas, si lo escuchas es muy conservador en el tema. Para AMLO la solución al problema es hacer una gran campaña de publicidad y solamente decir no a las drogas”, remató Arredondo, doctor en Salud Pública.

	""",
	"""
	Levantar prohibición a drogas ilícitas y reorientar recursos a reinserción, amnistía, sanciones por incumplimiento de recomendaciones de CNDH, y abatir crecimiento delictivo son algunas de las promesas. 

	El gobierno del presidente Andrés Manuel López Obrador ha prometido en varias ocasiones que restablecerá la paz en el país y acabará con la violencia. Pero ¿cómo planea hacerlo?

	El Plan Nacional de Desarrollo (PND) 2019 – 2024 enviado esta semana al Congreso expone la estrategia del el gobierno federal y la define como un  “un cambio del paradigma” de seguridad para alcanzar la paz.

	Primero se prometen una serie de acciones que se llevarán a cabo en el sexenio y que van desde el levantamiento de la prohibición de algunas sustancias y el fin de la “guerra contra las drogas”, hasta un plan de justicia transicional que permita amnistía en algunos casos,  y penalizar el incumplimiento de recomendaciones a derechos humanos.

	Y después, el plan define un grupo de metas e indicadores que deberán alcanzarse para 2024, aunque sin estar directamente vinculados con las promesas planteadas en un inicio.

	A continuación Animal Político presenta los puntos clave de ambos apartados relacionados con la estrategia de seguridad.

	Entre el cúmulo de acciones que se prometen en el Plan Nacional de Desarrollo 2019 – 2024,  sin identificar plazos ni indicadores que permiten medir su cumplimiento, se encuentra lo siguiente: Fin a la guerra contra las drogas y política prohibicionista

	El PND sostiene que la denominada “guerra contra las drogas” impulsada en los dos sexenios anteriores no disminuyó el consumo y, por el contrario, convirtió un problema de salud pública en una crisis de seguridad nacional. 

	Para ello se plantea acabar con esta estrategia y “levantar la prohibición de drogas actualmente ilícitas”, así como reorientar recursos que hoy se utilizan para combatir el tráfico a programas de desintoxicación y reinserción.

	Oportunidades alternas a la economía ilícita

	El plan señala que el gobierno impulsará un “desarrollo alternativo” que genere opciones de ingreso para las familias cuya economía depende de lo que hoy perciben por el cultivo de drogas, la venta de hidrocarburos robados, entre otros.

	Justicia transicional y amnistía

	Como el gobierno ya había adelantado un componente de su estrategia para restaurar la paz es la llamada “justicia transicional” que permitirá, según el documento, pacificar el país con “medios no violentos” y desarmar a grupos infractores. Para ello se contempla, entre otras cosas, revisar expedientes de personas acusadas o sentenciadas y analizar si pueden ser objeto de amnistías o indultos.

	Se contempla en este mismo sentido el establecimiento del denominado “Consejo para la Construcción de la Paz”, con la participación de la CNDH y de Naciones Unidas.

	Castigo por incumplimiento de recomendaciones

	El plan sostiene que se impulsarán reformas orientadas a convertir en una obligación legal el cumplimiento de las recomendaciones que genere la Comisión Nacional de los Derechos Humanos y sus homologas estatales, y plantea sanciones para las autoridades que no lleven a cabo el referido cumplimiento.

	Debilitar base social del crimen

	Una de las principales acciones que el plan sostiene como recurso para combatir a la violencia es el impulso de programas sociales, de oportunidades de trabajo y de proyectos de desarrollo que generen bienestar entre la población y que, por ende, debiliten “la base social” desde la cual se nutre el crimen.

	En síntesis, generar más oportunidades y condiciones favorables para que las personas no se vean en la necesidad de unirse a la delincuencia en búsqueda de recursos.

	Como ejemplos para materializar esto, el plan subraya la puesta en marcha del programa Jóvenes Construyendo el Futuro, la construcción de las Universidades Benito Juárez, el desarrollo de las comunidades sustentables Sembrando Vida”, y hasta la construcción del Tren Maya y del Aeropuerto “Felipe Ángeles” 

	Combate a delitos fiscales y de hidrocarburos, y baja de homicidios

	El plan promete la “erradicación” de delitos que han crecido al amparo de la impunidad y corrupción, destacando el lavado de dinero, el tráfico de armas, el robo de hidrocarburos y la evasión fiscal. Además promete que para el último año del sexenio habrá una reducción en delitos de alto impacto como homicidios y robos de 50%.
	
	Acabar con brecha salarial en aparato de seguridad

	El plan considera indispensable disminuir las brechas salariales que existen ente policías, agentes del Ministerio Público y jueces por lo menos a nivel federal para favorecer la operación del sistema de justicia.

	Fuerzas armadas y Guardia Nacional

	El plan retoma lo ya planteado en diversas ocasiones respecto a la constitución y puesta en marcha de la Guardia Nacional como la nueva policía de proximidad del país. Se plantea contar con un estado de fuerza de 140 mil elementos al acabar el sexenio, y que sea desplegada en las 266 regiones consideradas como prioritarias.
	
	A la par de ello se subraya el apoyo que podrán dar las Fuerzas Armadas de forma ya legalizada durante los próximos cinco años, mientras se conforma la Guardia Nacional.

	Lo medible

	Entre las acciones que el Plan Nacional de Desarrollo identifica con objetivos e indicadores medibles se encuentra lo siguiente:

	Disminuir incidencia delictiva 15%

	El plan establece como meta que la tasa de 39 mil 369 delitos por cada 100 mil habitantes registrada en 2017, descienda a 33 mil 219 delitos en 2024, lo que equivaldría a una reducción de más del 15%.

	Cabe señalar que este indicador no corresponde con la baja en 50% en delitos como homicidio que se promete en la primera parte del PND ni se incluye un indicador respecto a esta promesa en específico.

	Abatir percepción de inseguridad

	El documento  plantea como objetivo disminuir la percepción de la población que se siente insegura y que en 2018 fue casi el 80% de todos los encuestados. La meta es que para 2024 la proporción sea de 39.4%.

	Elevar cumplimiento de recomendaciones

	El plan propone elevar la proporción de cumplimiento de los puntos recomendatorios que emita la CNDH. El objetivo es pasar del 81% que actualmente registra el gobierno a un nivel de cumplimiento de al menos 90% en 2024.

	Mejorar Índice de Estado de Derecho

	El gobierno plantea generar las condiciones necesarias para que México mejore su calificación en el Índice de Estado de Derecho elaborado por la organización “World Justice Project”, el cual evalúa las capacidades de los países en distintos rubros como justicia civil y penal, orden y seguridad, límites al poder gubernamental, entre otros.

	Se busca avanzar del 0.45 con el que se figura actualmente a un índice de 0.60 para el 2024.
	"""
	]


PATH = './H1_sentiment_polarity/'

all_files = os.listdir(PATH)

filename = 'q_AMLO_medicamentos_text.json'

if filename in all_files:

	before = pd.read_json(PATH + filename)

	dict_ = {'title': [], 'text': []}

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
	print(len(title))
	print(len(text))
	dict_ = {'id': [], 'title': [], 'text': []}

	id_ = 0
	for i in range(len(title)):
		dict_['id'].append(id_)
		dict_['title'].append(title[i])
		dict_['text'].append(text[i])

		id_ += 1

	with open(PATH + filename, 'w') as fp:
		json.dump(dict_, fp)