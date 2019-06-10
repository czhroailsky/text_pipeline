import pandas as pd 
import json

PATH = './full_dataset/'

title = [
"""
Fitch recorta la calificación crediticia de Pemex
""",
"""
Baja Fitch calificación de Pemex
""",
"""
Amenaza Pemex a finanzas públicas
""",
"""
Fitch Ratings coloca en grado “especulativo” la calificación de Pemex
""",
"""
Conclusión de Fitch es “excesivamente severa”: Pemex
""",
"""
Desafortunado, que penalicen a México.-Gobierno
""",
"""
Reducción adicional de impuestos a Pemex, correcta pero insuficiente: Fitch
""",
"""
Fitch Ratings degrada la calificación crediticia de México
""",
"""
Fitch Ratings: correcta, pero insuficiente la estrategia para Pemex
""",
"""
Pemex descarta riesgos en refinanciamiento de su deuda por baja calificación de Fitch
""",
"""
Yo acuso
""",
"""
Aranceles afectarían negativamente a 20% de empresas calificadas por Fitch Ratings
""",
"""
Ya hay más de 15 bancos para refinanciamiento: Pemex
""",
"""
Fitch degrada calificación de Pemex a ‘bono basura’
""",
"""
Dólar llega a 19.84 pesos tras baja de calificación de Fitch y Moody’s
""",
"""
AMLO arremete contra calificadoras: “No han sido profesionales”
""",
"""
AMLO revira a calificadoras: “No han sido profesionales ni objetivas”
""",
"""
Calificadoras reducen nota y perspectiva de Pemex; estamos en fuerte desacuerdo, responde gobierno
""",
"""
Pemex califica como «excesivamente severa» baja de Fitch
""",
"""
Fitch y Moody’s bajan calificación y perspectiva crediticia para México; dólar brinca a 19.73 pesos
"""
]

text = [
"""
La calificadora ve riesgo creciente para las finanzas públicas a causa del perfil crediticio en deterioro de la petrolera. 
La agencia calificadora Fitch Ratings recortó este jueves la calificación crediticia de Petróleos Mexicanos (Pemex) a BB+ desde BBB-, luego que ayer rebajara la calificación soberana de México. 
La baja en las calificaciones, explicó Fitch, aplica para las emisiones de deuda de Pemex en el mercado por un monto de 80.000 millones de dólares.
Estas acciones se dan un día después de la baja en las calificaciones soberanas de México en escala internacional de largo plazo en moneda extranjera y moneda local a 'BBB' desde 'BBB+', y la revisión de su perspectiva a estable desde negativa.
La baja en las calificaciones se debe, dijo Fitch en un comunicado, al riesgo al alza para las finanzas públicas a causa del perfil crediticio en deterioro de Pemex.
"La compañía (Pemex) continúa sin invertir lo suficiente en su negocio de exploración y producción, lo que puede llevar a una disminución en la producción y las reservas", destacó.
Asimismo, Fitch señaló la debilidad continua de la perspectiva macroeconómica de México, que se ha agravado "por la tensión comercial, cierta incertidumbre de las políticas nacionales y limitaciones fiscales que persisten".
La Secretaría de Hacienda y Crédito Público respondió a Fitch, calificando de "desafortunado" que "penalice doblemente el balance financiero del país".
Hacienda señaló que continuará apoyando a Pemex. "Por el lado soberano, argumentan que los riesgos a las finanzas públicas se han incrementado porque la deuda de Pemex representa pasivos contingentes para el Gobierno Federal, asumiendo así un apoyo inminente a la entidad. Al mismo tiempo, la agencia penaliza la calificación de Pemex por considerar que el respaldo del Gobierno Federal es moderado e insuficiente", se lee en un comunicado.
""",
"""

""",
"""

""",
"""
Las notas crediticias de Petróleos Mexicanos (Pemex) fueron colocadas por Fitch Ratings al grado “especulativo” como consecuencia de la degradación de las notas soberanas del país.
Esta tarde la firma estadunidense decidió degradar la calificación de Pemex a “BB+” desde “BBB-”, con lo que pierde el grado de inversión.
Fitch Ratings argumentó que la medida se determinó después de la baja en las calificaciones soberanas de México en escala internacional de largo plazo en moneda extranjera y moneda local a ‘BBB’ desde ‘BBB+’, y la revisión de su Perspectiva a “Estable” desde “Negativa”, realizadas el 5 de junio de 2019.
Agregó: “La baja en las calificaciones del soberano refleja una combinación del riesgo al alza para las finanzas públicas del soberano a causa del perfil crediticio en deterioro de Pemex, junto a la debilidad continua de la perspectiva macroeconómica, que se ha agravado por amenazas externas por la tensión comercial, cierta incertidumbre de las políticas nacionales y limitaciones fiscales que persisten”.
Según la agencia con sede en Nueva York, la perspectiva “Negativa” de Pemex refleja un deterioro potencial en su perfil crediticio individual por debajo de “CCC”.
Al respecto, señaló que “aunque Pemex ha implementado algunas medidas de recorte de costos y el gobierno mexicano le ha otorgado reducciones en impuestos, la compañía continúa sin invertir lo suficiente en su negocio de exploración y producción, lo que puede llevar a una disminución en la producción y las reservas”.
El monto alto de transferencias de la petrolera al gobierno mexicano sigue presionando la generación de flujo de la compañía y su capacidad para reinvertir, lo cual deteriora su perfil crediticio individual, detalló.
Lo peor aún no llega, ya que, de acuerdo con el reporte, factores futuros podrían llevar, de forma individual o en conjunto, a una acción de calificación negativa para la petrolera, como una disminución en la calificación soberana de México que no se deba a la materialización de pasivos contingentes relacionados con la compañía.
Otro factor es un deterioro sostenido en la flexibilidad financiera, en conjunto con una pasividad por parte del gobierno para apoyar la liquidez de Petróleos Mexicanos. Esto podría resultar de un continuo flujo de fondos libres negativos y/o una reducción importante de caja, líneas de crédito y acceso a mercados de capital.
La calificadora puede ajustar a la baja las notas con un nivel de deuda total ajustada a flujo generado por las operaciones por encima de ocho veces y una razón de deuda total a reservas 1P significativamente mayor de15 dólares por barril.
Además, podría darse un deterioro continuo en la calidad crediticia individual de Pemex en escala internacional por debajo de “CCC”, lo que podría ocurrir si la compañía no lograra estabilizar la producción y continuara con índices de reposición de reservas insostenibles y flujo de fondos libre negativo.
En contraste, Fitch adelantó que no prevé un alza en las calificaciones de la empresa productiva del Estado mexicano en el corto plazo, pero una acción de calificación positiva o la estabilización de la Perspectiva podría resultar de las siguientes situaciones:
En primer lugar, un incremento en la calificación soberana de México, o de una garantía irrevocable por parte del gobierno mexicano hacia Pemex para más de 75% de su deuda.
La agencia también evalúa una inyección relevante de capital para la petrolera, junto a una estrategia de la compañía para permitir inversiones en exploración y producción sostenibles que sean suficientes para mantener una razón de reemplazo de reservas de casi 100% y una producción estable que le permita reportar un flujo de fondos libre de neutro a positivo a través del ciclo.
Por último, un apalancamiento ajustado de flujo generado por las operaciones, menor de cinco veces, también puede echar mano para mejorar sus calificaciones.
""",
"""
La petrolera afirmó que no coincide con la calificadora, ya que durante el primer semestre de este gobierno se ha logrado disminuir el robo de combustibles y estabilizar la producción de petróleo.
Luego de Fitch Ratings modificara a la baja la calificación de Petróleos Mexicanos (Pemex), la empresa consideró  “excesivamente severa” la conclusión de la agencia.
“No coincidimos técnicamente con los supuestos que sustentan la decisión de Fitch Ratings, especialmente porque se da en un contexto de reducción de cuatro niveles en un periodo de tan sólo cinco meses”, señaló en un comunicado.
El jueves Fitch bajó la calificación crediticia de largo plazo, para moneda local y extranjera de Petróleos Mexicanos, de BBB- a BB+, con perspectiva negativa. 
Pemex mostró su inconformidad ante esta decisión, ya que “durante los primeros seis meses de este gobierno hemos materializado logros contundentes“.
La petrolera destacó los resultados positivos de la estrategia contra el robo de combustibles y la estabilidad en la producción de petróleo. 
“Por primera vez en casi 10 años no hemos utilizado la deuda para financiar los proyectos de inversión de la empresa”.
Además, la petrolera apuntó, a partir de un ejercicio transparente del gasto, sin corrupción, estamos bajando los costos de adquisición de los bienes y servicios que la empresa contrata.
“El incremento de inversión de Pemex en exploración y producción, tras cuatro años consecutivos de reducción, potencian nuestro escenario de una recuperación de la producción de petróleo hacia el final de este mismo año y dan certeza de un incremento sostenido de la producción a partir del año 2020″, agregó. 
""",
"""

""",
"""
La calificadora apuntó que ayudará moderadamente a la compañía a reducir su carga fiscal; necesita bajar 50% de impuestos para retener suficiente flujo de efectivo
Si bien la implementación de una reducción adicional de impuestos para Petróleos Mexicanos (Pemex), anunciada el pasado 24 de mayo, es un paso más en la dirección correcta, es insuficiente para estabilizar la calidad crediticia de la empresa, estimó Fitch Ratings.
La calificadora apuntó que las medidas fiscales aprobadas representarían una reducción adicional de 1.1 mil millones de dólares o el equivalente a 3.7 por ciento de las transferencias totales de 2018 al Gobierno de México.
Cuando se agregan a la cantidad anunciada en 2017 de aproximadamente 400 millones de dólares, solo ayudarán moderadamente a la compañía a reducir su carga fiscal, argumentó en un reporte.
La medida nueva solo es aplicable para 2019, ya que Pemex y el gobierno exploran soluciones más permanentes para la carga fiscal alta de la empresa, señaló.
Fitch consideró que Pemex necesitaría que sus impuestos se redujeran en no menos de 50 por ciento para que la empresa pueda retener suficiente flujo de efectivo interno e invertir en su negocio principal o para pagar deuda.
Se espera que el apoyo total del gobierno para Pemex en 2019 ascienda a aproximadamente 5.5 mil millones de dólares que incluyen esta última reducción de impuestos, las exenciones fiscales anunciadas anteriormente, una inyección de capital y la amortización anticipada de los bonos del gobierno otorgados para pagos de pensiones.
Estas estimaciones asumen que Pemex es capaz de aprovechar este año las reducciones de impuestos implementadas en enero sobre 5 por ciento de su producción, señaló la agencia evaluadora de riesgo crediticio.
Tras compensar estas contribuciones de las inversiones en refinación de 50 mil millones de pesos proyectadas para la refinería nueva en 2019, refirió que estas medidas equivalen a aproximadamente una reducción de impuestos de 10 por ciento o dos mil 900 millones de dólares, que se comparan desfavorablemente con unos 27 mil millones de dólares de transferencias al gobierno durante 2018.
Fitch estimó que si Pemex estuviera invirtiendo a un nivel suficiente para estabilizar su producción y reponer las reservas, su déficit de flujo de efectivo sería de entre 12 mil millones a 17 mil millones de dólares.
El pasado 24 de mayo, México firmó un decreto para aumentar los límites de costos que determinan la cantidad de gastos e inversiones que un campo puede deducir de los ingresos gravables para una producción total de líquidos que no exceda de los 250 mil barriles por día.
Aunque la tasa impositiva calculada por el gobierno no cambia en los campos de petróleo y gas elegibles, la calificadora anticipó que los impuestos reales pagados caerán debido a un aumento en el límite de costo permitido de 35 por ciento desde 12.5 por ciento para aguas someras y de 40 por ciento para producción en campos terrestres.
La calificadora internacional comentó que el límite de costo más alto solo puede aplicarse a la producción que es rentable antes de impuestos, pero que genera pérdidas para Pemex bajo el régimen fiscal actual.
Este esquema incluye lo que se le entregó a la compañía en agosto de 2017 para una producción nominal de líquidos que exceda los 150 mil barriles por día, indicó.
En enero de 2019, Fitch bajó las calificaciones en escala nacional de largo plazo de Pemex a ‘AA(mex)’ desde ‘AAA(mex)’ y en escala internacional a ‘BBB-‘ de ‘BBB+’. Fitch mantuvo la perspectiva en “Negativa”. (Ntx)
""",
"""
La agencia calificadora Fitch Ratings decidió degradar las notas crediticias del país de BBB+ a BBB con perspectiva estable.
De acuerdo con la firma con sede en Nueva York, la baja en la calificación se da por una combinación de mayor riesgo para las finanzas públicas de México debido al deterioro del perfil crediticio de Pemex, junto una perspectiva débil para la economía que se ve empeorada por las amenazas externas de las tensiones comerciales y cierta incertidumbre de la política interna.
En la escala de calificaciones, BBB, según la definición de Fitch, indica que existe un riesgo moderado de incumplimiento. Sin embargo, los cambios en circunstancias o condiciones económicas tienen más probabilidades de afectar la capacidad de pago oportuno que en el caso de los compromisos financieros que poseen una calificación más alta.
En su comunicado, la calificadora aseguró que el crecimiento económico continúa por debajo de lo esperado, además de que los riesgos a la baja son magnificados por las amenazas del presidente de Estados Unidos, Donald Trump, de imponer aranceles en México a partir del 10 de junio.
Eso no es todo. Fitch agregó que, si bien espera que el crecimiento acelere en el segundo trimestre del año, sólo alcanzaría un 1% el presente año.
“La menor inflación y los salarios más altos (derivados del aumento del salario mínimo) deberían respaldar el consumo, pero el sector energético, caracterizado por una tendencia a la caída de la producción en Pemex, y niveles de inversión más débiles, que reflejan una menor confianza empresarial, continuarán afectando el crecimiento”.
La otra preocupación que tiene la agencia calificadora es la situación de Petróleos Mexicanos (Pemex).
“Los diferenciales de la deuda de Pemex sobre la deuda soberana aumentaron sustancialmente en el primer trimestre del 2019, lo que llevó al gobierno a aumentar el apoyo. El costo fiscal de ese apoyo hasta la fecha representa el 0.2% del PIB en inyecciones de capital y menores impuestos efectivos, pero a juicio de Fitch no son suficientes para brindar una solución a largo plazo o evitar un deterioro continuo en el perfil crediticio de Pemex”, señaló Fitch Ratings.
Según la firma, Pemex no cuenta con los suficientes recursos para invertir en producción de petróleo y espera que ésta se contraiga un 5% en 2019 y 2020.
Por si fuera poco, advirtió que el apoyo del gobierno de Andrés Manuel López Obrador a Pemex se extenderá en el mediano plazo con menor carga fiscal e inyecciones de capital lo que, a su vez, impactará de forma negativa las finanzas públicas de México.
""",
"""
La agencia internacional calificadora de valores Fitch Ratings sostuvo que las recientes medidas anunciadas por el gobierno para apoyar a Petróleos Mexicanos (Pemex) son un paso en la dirección correcta, pero "muy lejos" de lo que requiere la empresa.
Recordó que el presidente Andrés Manuel López Obrador anunció el lunes pasado medidas para tratar de aliviar las finanzas de la endeudada empresa –que lucha por estabilizar su producción–, incluyendo la renovación de líneas de crédito y la intención de reducir gradualmente su carga tributaria.
Consideró que las medidas propuestas por el gobierno siguen lejos de permitir reducir la carga impositiva y agregó que la "perspectiva negativa para Pemex implica la posibilidad de bajar la calificación en los próximos 12 a 18 meses".
En un reporte dado a conocer ayer, la firma financiera adelantó que la calificación a Pemex podría afectar la calificación de la deuda soberana de México.
Fitch señaló que Pemex necesita flujo de caja neutral o positivo después de impuestos para estabilizar su perfil crediticio y las medidas anunciadas no lo permiten.
Señaló que las medidas tributaria propuestas por el gobierno mexicano siguen lejos de reducir suficientemente la carga impositiva.
Adicionalmente, la firma dijo que las recientes medidas del gobierno mexicano para apoyar a Pemex son un paso adelante en la dirección correcta, pero "muy lejos" de lo que precisa.
El Presidente dijo la semana pasada que Pemex y la secretaría de Energía se harán cargo de la construcción de una planeada refinería con un costo de 8 mil millones de dólares en el puerto de Dos Bocas, en Tabasco, dado que el sector privado no se adaptaba los plazos ni al presupuesto anunciado.
Al primer trimestre de 2019 Pemex ha concretado diversas medidas para sanear sus finanzas como la amortización de deuda por 2 mil 344 millones de dólares, equivalente a unos 45 mil 945 millones de pesos.
Los informes oficiales de la empresa revelan que Pemex incrementó su gasto de inversión presupuestal en 22.7 por ciento en el primer bimestre del año, al pasar de 2 mil 200 millones a 2 mil 700 millones de dólares.
También se logró la estabilización de la plataforma de extracción en un millón 704 mil barriles diarios en promedio.
Dentro de la estrategia de Pemex para este año se impulsa la producción, con el desarrollo de 20 campos nuevos, entre terrestres y marinos. Entre los campos marinos destacan: Xikin, Esah, Cheek, Cahua, Uchbal, Manik, Jaatsul, Suuk, Teekit, Koban, Hok, Mulach, Tlacame, Tetl, ,Pokche y Octl. Por su parte, los campos terrestres son: Xachi, Chocol, Cibix y Valeriana.
""",
"""
La empresa dio a conocer que al 06 de junio ya son más de 15 instituciones bancarias que se han sumado a la operación de refinanciamiento.
Petróleos Mexicanos (Pemex) aseguró que la baja en su calificación por parte de Fitch Ratings “no pone en riesgo su proceso de refinanciamiento de la deuda”. 
En un comunicado, dio a conocer que el pasado jueves funcionarios del área de finanzas presentaron en la ciudad de Nueva York las características de la estructura de la operación de refinanciamiento de la deuda anunciada el pasado 13 de mayo.
Informó que en la reunión convocada por Pemex y celebrada en la sede del banco JP Morgan acudieron representantes de la banca internacional, en lo que fue “una de las sesiones más concurridas de los últimos años”.
Explicó que en la sesión plenaria con los bancos, Pemex presentó el diagnóstico de la empresa y las estrategias que está implementando para solucionar los problemas estructurales que enfrenta, así como los primeros resultados que está logrando en tan solo seis meses de haber iniciado sus trabajos la actual administración.
“La reunión formó parte del proceso de sindicación del refinanciamiento por 8 mil millones de dólares“, expuso.
Asimismo, apuntó, a lo largo del día, el equipo de finanzas de Pemex sostuvo reuniones bilaterales con diversas instituciones financieras.
Si bien reconoció que el efecto de la baja de calificación y pérdida del grado de inversión por parte de Fitch Ratings a Pemex es un evento relevante, “creemos que hay opciones y estrategias que, con el apoyo del gobierno federal, se podrán implementar para mitigar los efectos de la baja de calificación”.
“Es importante mencionar que este evento no pone en riesgo el proceso de refinanciamiento de la deuda que Pemex está cerrando con la banca internacional. Por el contrario, pese a la baja de calificación al cierre del día de ayer se logró sumar a más instituciones financieras al proceso de refinanciamiento de la deuda de la empresa”, aseguró.
Recordó que la operación fue garantizada inicialmente sólo por tres instituciones financieras: JP Morgan, HSBC y Mizuho.
Sin embargo, destacó que al 06 de junio ya son más de 15 instituciones bancarias que se han sumado a la operación de refinanciamiento de la deuda de Pemex.
“Se prevé que el proceso de sindicación del crédito esté concluido a finales del mes de junio”, abundó.
""",
"""
Si se fugaran miles de millones de dólares de México y se produjera una espantosa devaluación del peso, los únicos culpables serían el presidente López Obrador y Carlos Urzúa
El 5 de junio pasado, tanto Moody’s Investors Service, como Fitch Ratings, dos importantes agencias de calificación de riesgos que realizan investigaciones financieras internacionales y practican análisis de las entidades comerciales y gubernamentales, asestaron tremendos golpes a la deuda mexicana. La primera, por su parte, ajustó la perspectiva económica de estable a negativa, en tanto Fitch bajó la calificación al prever un mayor riesgo para las finanzas públicas mexicanas de acuerdo al debilitamiento financiero de Pemex, la única compañía petrolera del mundo que se encuentra quebrada de punta a punta, además de la incertidumbre en relación a las políticas domésticas y a las amenazas comerciales. Si México perdiera el grado de inversión, momento catastrófico que no se anticipa como una decisión inminente, se produciría una pavorosa fuga de capitales golondrinos valuada en decenas de miles de millones de dólares ya que, de acuerdo a sus estatutos, los fondos internacionales no pueden mantener inversiones en países en donde sus bonos colocados en los mercados sean considerados “basura”.
Y por si lo anterior no fuera suficiente, existe la posibilidad que el próximo lunes el presidente Trump imponga un incremento arancelario del 5% a las importaciones globales mexicanas debido a que según él, el Gobierno de AMLO no ha tomado las medidas radicales para contener la migración ilegal proveniente fundamentalmente de Centroamérica, aun cuando lo anterior implique darle un balazo en el pie a millones de consumidores norteamericanos que tal vez podrían castigar en las urnas al Jefe de la Casa Blanca en el 2020 y enfrentarse a su propio partido en el Congreso de Estados Unidos.
Si México llegara a perder el grado de inversión de acuerdo a los criterios de las agencias de calificación de riesgos y se fugaran miles de millones de dólares de México y se produjera una espantosa devaluación del peso mexicano y se detonara una nueva e incontenible espiral inflacionaria y se perdieran empleos y se empobreciera a una nación con un 50% de compatriotas sepultados en la pobreza, entre otros daños colaterales no menos importantes, los únicos culpables serían el presidente López Obrador y Carlos Urzúa, secretario de Hacienda, obviamente corresponsable de las decisiones equivocadas que de nueva cuenta están conduciendo a México a un profundo despeñadero que demuestra nuestra incapacidad de aprender de la historia y nuestra escasa visión para copiar lo que funciona con gran eficiencia en otros países.
AMLO empezó con el proceso de destrucción de la economía al cancelar la construcción del aeropuerto internacional de la Ciudad de México que hubiera representado el 1,5% del PIB, y haber enterrado 15.000 millones de dólares en un país con carencias inadmisibles. Por si fuera poco, canceló el Consejo de Promoción Turística que coadyuvó en los últimos seis años a la captación de 192.000 millones de dólares; canceló las rondas petroleras que implicaban inversiones por más de 200.000 millones de dólares por más que ahora pretendan cambiar dicha política; canceló contratos para producir energía de origen eólico que representaban 20.000 millones de dólares; creó incertidumbre en los inversionistas extranjeros, regaló dinero a manos llenas en lugar de crear empleos por medio de un voluminoso gasto público en infraestructura aliado con la iniciativa privada doméstica; desperdiciará recursos públicos en la construcción de una refinería, en lugar de financiar a un Pemex agónico o de alquilar alguna en Texas, o de evitar la inversión en un Tren Maya sin proyectos ejecutivos de viabilidad, que sangrará aún más las mermadas finanzas públicas.
El secretario Urzúa también será corresponsable del desastre. Pasará a la historia como uno de los causantes de otra devastación social. Todavía se puede dar un golpe de timón, rescatar el aeropuerto, cancelar obras suicidas, reparar los daños causados, volver a instalar lo que funciona, reconstruir la confianza en México, escapar de la recesión que viene por el desplome del crecimiento económico.
México está a tiempo de girar y de evitar la ruta de colisión a la que estamos proyectados dentro de una inercia suicida. Yo acuso a AMLO de la próxima ruina de México si perdemos el grado de inversión de acuerdo a las calificadoras. Él será el principal responsable de una nueva devastación de consecuencias imprevisibles al haberle robado la esperanza a los mexicanos.
""",
"""
La agencia calificadora Fitch Ratings advirtió que la imposición de los aranceles generales en las importaciones de Estados Unidos  de productos mexicanos podría tener un efecto directo negativo sobre los ingresos en 20% de las compañías mexicanas calificadas por Fitch en escala internacional.
Se trata de empresas con exportaciones significativas, directas o indirectas, que incluyen a los proveedores de autopartes Rassini, Metalsa, Nemak  y Grupo Kuo.  Otros exportadores son Grupo Kaltex, Mabe, Becle  y Petróleos Mexicanos (Pemex).
De acuerdo con el reporte de la firma con sede en Nueva York, Grupo Kaltex y Pemex son los más vulnerables, dadas sus estructuras de capital y flujo de efectivo limitado. De hecho, la petrolera, exportó aproximadamente 37% de su producción de crudo a las distintas regiones en América, la mayoría a Estados Unidos.
Según la calificadora, el sector automotriz, industrial, de bebidas alcohólicas y de energía se exponen directamente al riesgo comercial, aun y cuando la capacidad de los emisores de mitigar las potenciales implicaciones crediticias y de flujo de efectivo varía.
“Los proveedores de autopartes podrían verse perjudicados por los aranceles, al igual que los precios de vehículos, potencialmente más altos, que podrían afectar su demanda en la Unión Americana, en la medida en que las tarifas se transfieran hacia los consumidores. No obstante, las estructuras de capital de los proveedores de autopartes generalmente son robustas y las posiciones de liquidez, relativamente fuertes”, explicó Fitch.
La agencia matizó que, no obstante, dependiendo de la duración y el nivel de los aranceles impuestos, también podría haber efectos indirectos en compañías mexicanas, asociados a las consecuencias macroeconómicas amplias por tensiones comerciales mayores.
Fitch Ratings aseguró que en caso de aprobarse el acuerdo comercial anunciado en octubre de 2018, el cual incluye disposiciones acerca de productos lácteos, pollo, huevo, textiles, contenido digital, propiedad intelectual y manufactura automotriz, reduciría en gran medida la incertidumbre comercial para los corporativos mexicanos.
“Se espera que el acuerdo elimine el riesgo de que el Tratado de Libre Comercio de América del Norte (TLCAN) se concluya sin una alternativa en su lugar. Los precios de las materias primas impulsados por el comercio y la volatilidad de los tipos de cambio, efectos adicionales sobre los ingresos, los costos de los insumos reportados, así como la incertidumbre generada por tensiones comerciales respecto a la inversión, también podrían disminuir de aprobarse el T-MEC”.
La firma recordó que por el lado de los corporativos no financieros de México con emisiones internacionales han mostrado a la fecha un nivel de liquidez satisfactorio en perIodos recientes de incertidumbre respecto a los acuerdos comerciales con la Unión Americana
“Para muchos emisores, una porción elevada de ingresos provenientes de monedas fuertes mitiga los efectos de la depreciación del peso mexicano en el balance general, al estar la deuda denominada en dólares estadounidenses”, detalló.
La depreciación de la moneda también podría compensar el costo de los aranceles, al menos al umbral de 5%; no obstante, dicha compensación sería menos probable al llegar el arancel al nivel de 25%, dada la probabilidad de que haya una crisis económica más pronunciada.
""",
"""
Petróleos Mexicanos (Pemex) informó que ya suman más de 15 las instituciones bancarias -incluidas JP Morgan, HSBC y Mizuho–, que se han sumado a la operación de refinanciamiento de la deuda de la empresa productiva del Estado.
El anuncio se dio un día después de que Fitch Ratings degradó la calificación de Pemex a “BB+” desde “BBB-”, con lo que pierde el grado de inversión.
En respuesta, la empresa encabezada por Octavio Romero Oropeza, indicó que esta operación financiera constituye “la mayor realizada en la historia de la empresa y es fiel reflejo de la confianza que le brinda el sector financiero”.
Aunque no reveló el nombre de las otras 12 instituciones involucradas, Pemex prevé que el proceso de sindicación del crédito esté concluido a finales del mes de junio.
El 13 de mayo, el presidente Andrés Manuel López Obrador anunció que concretó la firma de cartas compromiso con tres bancos internacionales – JP Morgan, HSBC y Mizuho-, para renovar líneas de crédito y refinanciar deuda de la petrolera.
El 6 de junio, funcionarios del área de finanzas de Pemex presentaron en Nueva York, Estados Unidos, las características de la estructura de la operación de refinanciamiento.
A la reunión, celebrada en la sede del banco JP Morgan y a la que acudieron representantes de la banca internacional, Pemex presentó el diagnóstico de la empresa y las estrategias que está implementando para solucionar los problemas estructurales que enfrenta, así como los primeros resultados que está logrando en seis meses de gobierno.
“La reunión formó parte del proceso de sindicación del refinanciamiento por 8,000 mil millones de dólares. Asimismo, a lo largo del día, el equipo de finanzas de Pemex sostuvo reuniones bilaterales con diversas instituciones financieras”, señaló la empresa mexicana en un comunicado.
En el tema Fitch Ratings, Pemex apeló que “hay opciones y estrategias que, con el apoyo del gobierno federal, se podrán implementar para mitigar los efectos de la baja de calificación”.
""",
"""
La calificadora de riesgo crediticio degradó la nota de largo plazo a BB+ desde BBB- en moneda local y extranjera.
Fitch degradó la calificación de Petróleos Mexicanos (Pemex) a ‘bono basura’ desde un grado de inversión.
La calificadora de riesgo crediticio degradó la nota de largo plazo a BB+ desde BBB- en moneda local y extranjera.
La medida sigue a la degradación de la calificación soberana de México de BBB desde BBB+, debido a un aumento del riesgo para las finanzas públicas y el deterioro del perfil crediticio de Pemex, acompañado de una debilidad del panorama macroeconómico, detalló la firma en un comunicado.
Fitch dijo que Pemex continua subinvirtiendo en su negocio de exploración y producción de hidrocarburos, lo que puede llevar a una caída mayor de la producción y reservas petroleras.
“El alto nivel de transferencias a Pemex del gobierno mexicano sigue presionando significativamente la generación de flujo de efectivo de Pemex”, agregó.
El cambio negativo aplica a aproximadamente 80,000 millones de dólares en circulación de títulos.
De acuerdo con Fitch, las calificaciones de “BB” indican una vulnerabilidad elevada al riesgo de incumplimiento, especialmente en el caso de cambios adversos en las condiciones económicas o comerciales a lo largo del tiempo; sin embargo, existe flexibilidad comercial o financiera que apoya el servicio de los compromisos financieros.
Un bono con una nota crediticia en grado especulativo (bonos basura) ofrecen a los inversionistas rendimientos más altos que los bonos de compañías financieramente sólidas, detalló la bolsa de valores estadounidense, Nasdaq en un documento.
""",
"""
Este miércoles, las agencias calificadoras Fitch Ratings y Moody’s modificaron las perspectivas de calificación para México, en ambos casos de forma negativa.
¿Las consecuencias?
El pasado martes el Banco de México cerró operaciones con el dólar a 19.51 pesos. La tarde de este miércoles llegamos a 19.84 pesos por dólar y en ventanillas bancarias se vendió hasta en 20.10 pesos por dólar.
En el caso de Fitch, la calificación de México cambió de ‘BBB+’ a ‘BBB’, pero con perspectiva estable. De acuerdo con la calificadora, esto ocurrió por un mayor riesgo para las finanzas públicas de México debido a la baja del perfil crediticio de Pemex.
Además, la perspectiva de economía se ve cada vez peor por las amenazas externas (cof cof Trump) y la incertidumbre de la política interna.
Es más, se espera que el crecimiento se acelere en el segundo trimestre de este año pero solo se alcanzaría un 1% en todo el año.
Por su parte, Moody’s cambió la perspectiva de calificación de la deuda soberana de estable a negativo. Sin embargo, mantuvo la calificación en A3.
""",
"""
El presidente Andrés Manuel López Obrador se lanzó nuevamente contras las calificadoras, como Moody’s y Fitch Ratings, que en días recientes cambiaron a negativa la perspectiva sobre Pemex, por los riesgos que representa para las finanzas públicas que el gobierno invierta en su fortalecimiento.
El mandatario reiteró que la metodología que utiliza es poco profesional y en la mayoría de los casos sin objetividad. 
“No estamos de acuerdo con los dictámenes de las calificadoras. Vuelvo a reiterar están utilizando una metodología caduca. Es la metodología del periodo neoliberal que no incluye la variable de la corrupción, entre otras cosas.
“No han sido profesionales, objetivos”, lanzó López Obrador en conferencia de prensa.
El presidente reprochó que, durante tres años, en los que no hubo inversión en exploración y producción, las corredurías se hayan hecho “de la vista gorda” y hayan calificado bien a la empresa productiva del estado, y ahora que su gobierno apuesta por la inversión, degraden su nota crediticia.
El tabasqueño afirmó que la confianza sobre la recuperación de Pemex es amplia de tal forma que no se ha tenido ningún problema para reestructurar su deuda.
“Sobran ofertas con mejores garantías, ese es el informe que tengo. ¿Por qué razón? Porque en seis meses, algo que no tomaron en cuenta las calificadoras, se está trabajando en la producción de 22 campos petroleros y en tiempo récord se estabilizó la producción en Pemex”.
“Eso lo saben los financieros y por eso no tenemos ningún problema para reestructurar la deuda de Pemex en buenos términos”, aseveró.
Ayer, Moody’s modificó la perspectiva de calificación de Petróleos Mexicanos de estable a negativa, en el marco de un ajuste al panorama económico nacional por un amago de aranceles por parte de Estados Unidos.
La agencia explicó que la inversión de capital por parte del gobierno no será suficiente para que las reservas petroleras se repongan este año y en 2020.
Moody’s también modificó su evaluación de riesgo crediticio base (BCA), que refleja la fortaleza crediticia intrínseca de crédito, a caa1 desde b3.
""",
"""
El presidente Andrés Manuel López Obrador se lanzó nuevamente contras las calificadoras, como Moody’s y Fitch Ratings, que en días recientes cambiaron a negativa la perspectiva sobre Pemex, por los riesgos que representa para las finanzas públicas que el gobierno invierta en su fortalecimiento.
El mandatario reiteró que la metodología que utiliza es poco profesional y en la mayoría de los casos sin objetividad. 
“No estamos de acuerdo con los dictámenes de las calificadoras. Vuelvo a reiterar están utilizando una metodología caduca. Es la metodología del periodo neoliberal que no incluye la variable de la corrupción, entre otras cosas.
“No han sido profesionales, objetivos”, lanzó López Obrador en conferencia de prensa.
El presidente reprochó que, durante tres años, en los que no hubo inversión en exploración y producción, las corredurías se hayan hecho “de la vista gorda” y hayan calificado bien a la empresa productiva del estado, y ahora que su gobierno apuesta por la inversión, degraden su nota crediticia.
El tabasqueño afirmó que la confianza sobre la recuperación de Pemex es amplia de tal forma que no se ha tenido ningún problema para reestructurar su deuda.
“Sobran ofertas con mejores garantías, ese es el informe que tengo. ¿Por qué razón? Porque en seis meses, algo que no tomaron en cuenta las calificadoras, se está trabajando en la producción de 22 campos petroleros y en tiempo récord se estabilizó la producción en Pemex”.
“Eso lo saben los financieros y por eso no tenemos ningún problema para reestructurar la deuda de Pemex en buenos términos”, aseveró.
Ayer, Moody’s modificó la perspectiva de calificación de Petróleos Mexicanos de estable a negativa, en el marco de un ajuste al panorama económico nacional por un amago de aranceles por parte de Estados Unidos.
La agencia explicó que la inversión de capital por parte del gobierno no será suficiente para que las reservas petroleras se repongan este año y en 2020.
Moody’s también modificó su evaluación de riesgo crediticio base (BCA), que refleja la fortaleza crediticia intrínseca de crédito, a caa1 desde b3.
""",
"""
Un día después de que las calificadoras Fitch Ratings y Moody’s recortaron la calificación y perspectiva crediticia de México, respectivamente, ahora también redujeron la de Petróleos Mexicanos (Pemex).
Por un lado, la agencia Fitch bajó la calificación de ‘BBB-‘ a ‘BB +’, con perspectiva negativa. Esto debido al deterioro crediticio de la empresa productiva del Estado.
“Las calificaciones de Pemex están dos escalones por debajo de las del soberano como resultado de la debilidad del perfil crediticio de la compañía y la lenta acción del gobierno para fortalecer la estructura de capital de Pemex. Esto es una indicación de que el gobierno no ha reconocido la viabilidad del perfil financiero de la compañía y/o el papel estratégico que desempeña Pemex para el gobierno y el país”, explicó Fitch Ratings en un comunicado.
La agencia también destacó un “muy fuerte” control del gobierno sobre Pemex, cuya perspectivas “podrían estabilizarse si se le permite a Pemex retener suficiente de su generación de flujo de efectivo interno para estabilizar la producción de manera rentable y reponer las reservas”.
Fitch Ratings también bajó la nota de la Comisión Federal de Electricidad (CFE) ‘BBB+’ a ‘BBB’ con un cambio de perspectiva negativa.
“Las calificaciones de CFE incorporan, además, el establecimiento continuo de subsidios, altas pérdidas técnicas y no técnicas, exposición a variaciones en el tipo de cambio y uso de combustóleo en la generación de electricidad, que limitan la rentabilidad de la empresa”, sostuvo la agencia.
En tanto, Moody’s Investors Service cambió de estable a negativa la perspectiva crediticia de Petróleos Mexicanos, debido “a la extrema importancia de la fortaleza financiera y apoyo del gobierno para las calificaciones de Pemex”.
La calificadora destacó un “debilitamiento del marco de política en dos aspectos clave, con potenciales implicaciones negativas para el crecimiento y la deuda”, como políticas “predecibles” que están afectando la confianza de los inversionistas, junto con cambios en la política energética que introducen riesgos para la perspectiva fiscal a mediano plazo.
Además de las dificultado de Pemex en asunto de exploración y producción de petróleo, Moody’s destacó la construcción de la nueva refinería en Dos Bocas, Tabasco, “con costos y tiempos de terminación inciertos”, así como gastos de mantenimiento para mejorar el desempeño operativo de las otras refinerías en el país.
“Aún con los planes del equipo directivo para la reducción de costos y ganancias de eficiencia, los ahorros contemplados por la disminución del robo de combustible, y el apoyo del gobierno en forma de beneficios fiscales y otras medidas, Moody’s estima que Pemex generará un flujo de efectivo libre negativo considerable en 2019 y 2020”, expresó la agencia, quien también insistió en que Pemex tiene una liquidez débil y es altamente dependiente del soporte del gobierno. 
Tras dos días de cambios negativos en las perspectivas y calificaciones crediticias de México y Pemex, la Secretaría de Hacienda y Crédito Público (SHCP) respondió estar en desacuerdo con el enfoque utilizado por Fitch Ratings.
“Es desafortunado que la agencia Fitch Ratings penalice doblemente el balance financiero del país”, respondió Hacienda quien rechazó que el respaldo del gobierno federal a Pemex sea insuficiente. 
“El gobierno expresa su fuerte desacuerdo con el enfoque aplicado por esta calificadora”, afirmó.
""",
"""
 La empresa petrolera más endeudada del mundo recordó los resultados contra el robo de combustible, la inyección de recursos gubernamentales y la estabilización de su producción.
 Petróleos Mexicanos (Pemex) calificó como una medida severa la degradación de su nota a bono basura por parte de Fitch Ratings.
“No coincidimos técnicamente con los supuestos que sustentan la decisión de Fitch Ratings, especialmente porque se da en un contexto de reducción de cuatro niveles en un periodo de tan sólo cinco meses”, mencionó la empresa que dirige Octavio Romero Oropeza en un comunicado.
Este 6 de junio, la calificadora de riesgo crediticio modifición de largo plazo, para moneda local
y extranjera, de Petróleos Mexicanos de BBB- a BB+ ante el riesgo para las finanzas públicas por el apoyo del gobierno a la firma.
La compañía citó los resultados contra el robo de combustibles, estabilización en la producción de petróleo y por primera vez en casi diez años, no se ha utilizado la deuda para financiar proyectos de inversión de la empresa.
El gobierno de Andrés López Obrador canceló las rondas petroleras pendientes y suspendió las asociaciones de Pemex con empresas privadas.
La compañía enfrenta la deuda financiera más grande del sector petrolero por 106,500 milllones de dólares, al tiempo que su producción se ha estancado en 1.6 millones de barriles de crudo diarios.
""",
"""
Las agencias Fitch Ratings y Moody’s recortaron la calificación y perspectiva crediticia de México, respectivamente, debido a las tensiones comerciales con Estados Unidos, junto con la incertidumbre de la política nacional.
Fitch bajó la nota a ‘BBB’ desde ‘BBB+’, debido también “al deterioro del perfil crediticio de Pemex, junto con la debilidad actual en la perspectiva macroeconómica”, las cuales, señaló, se ven agravadas por las amenazas del gobierno de Donald Trump de aumentar los aranceles, así como las constantes restricciones fiscales del gobierno mexicano.
La calificadora también cuestionó que el apoyo del gobierno de Andrés Manuel López Obrador a las finanzas de Pemex, pues considera que las acciones anunciadas para su rescate “no son suficientes para brindar una solución a largo plazo o evitar un deterioro continuo en el perfil crediticio”.
También destacó como “poco probable” que la suspensión de las rondas de licitación del sector privado como parte de la reforma energética mejoren la confianza de la inversión.
“En opinión de Fitch, cumplir con los objetivos fiscales se volverá más difícil hacia 2020 y podría resultar en una política más estricta que genere un nuevo obstáculo para el crecimiento”, publicó en referencia a la promesa de López Obrador de no aumentar los impuestos antes de 2021.
En tanto,la agencia Moody’s cambió su perspectiva para México de “estable” a “negativa”, sin embargo mantuvo la calificación ‘A3’.
La disminución en un escalón significa que existe una mayor probabilidad de que el gobierno incumpla sus compromisos de pago.
Tras el anuncio de las calificadora, el dólar ganó terreno al cotizarse en 19.73 pesos.
Sin embargo, al momento del anuncio de las agencias, el peso llegó a cotizar hasta en 19.82 pesos, lo que implicó un aumento de casi 32 centavos, tras cerrar esta tarde en el país hasta en 19.50 pesos por billete verde al mayoreo.
"""
]

if __name__ == '__main__':

	news = 'pemex_fitch.json'
	folder = 'news_csv/'
	file = PATH + folder + news

	data = pd.read_json(file)

	"""n = 1
	for index, row in data.iterrows():
		print((' ' + str(n) + ' ') * 30)
		print(row['title'])
		print(row['url'])
		n += 1"""

	raw_text = PATH + folder + news.split('.')[0] + '_text.json'  

	dict_ = {'id': [], 'title': [], 'text': []}

	id_ = 0
	for i in range(len(title)):
		dict_['id'].append(id_)
		dict_['title'].append(title[i])
		dict_['text'].append(text[i])

		id_ += 1

	with open(raw_text, 'w') as fp:
		json.dump(dict_, fp)

	"""print(data.shape)
	print(len(title))
	print(len(text))"""