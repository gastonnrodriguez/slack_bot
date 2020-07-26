# slack_bot
Proyecto AI Developer Senpai Academy

● Conformación del equipo ya definida.

  Este proyecto lo hare de manera individual: Gastón Rodriguez
  
● Descripción de la problemática a solucionar.
  Opción 3 de Proyecto final: Bot con análisis de sentimientos
  Descripción
  El estudiante deberá utilizar dos métodos distintos para el análisis de sentimientos en español o inglés. Deberá además crear un      bot de Slack que permita a los usuarios decir una frase y recibir una clasificación de la misma utilizando por lo menos uno de los dos modelos.
    
● Descripción de la solución inicial planteada.

Se creara un bot de slack con el cual permitira a los usuarios elegir entre ingles o español y escribir mensajes, el bot respondera con el sentimiento que predijo del mensaje recibido: positivo, negativo o neutral.

● Descripción inicial del algoritmo de machine learning o modelo de deep learning a
utilizar.

 Para la solucion utilizare:
  -Model con NTLK y una regresion logistica
  -CNNs

● Análisis de soluciones existentes y detalle de la alternativa seleccionada
  
  Para el modelo de regresion logistica me baso en lo visto en clase y https://www.codigofuente.org/clasificacion-texto-python/ y https://towardsdatascience.com/sentiment-analysis-with-python-part-1-5ce197074184 .
  
  Para la red neuronal me baso en lo visto en clase y en https://stackabuse.com/python-for-nlp-movie-sentiment-analysis-using-deep-learning-in-keras/ 
  
  
  La idea es conectar la api de Slack para poder generar un bot que permita el analisis de sentimientos de los textos que escriban los usuarios, pienso que el usuario pueda indicar que modelo utilizar previo al ingreso del texto.
  
  Para ello armare una app con 2 endpoints: uno para cada modelo de manera de poder utilizarlos a ambos, tambien tengo pensado entrenar al modelo en español y a la red en ingles de manera que el bot sea bilingüe.
Las herramientas que utilizare son:
  -Python
  -Flask
  -keras
  -scikit learn

  Proyecto final:
  Para utilizar la aplicación hay que levanta la misma en el server (EC2 de amazon) y luego en nuestros canales Slack de Senpai en el canal "Varios" se generaron 2 slash commands /predict_es para analisis de sentimientos en español y /predict_en para hacerlo en ingles:

  La manera de utilizarlo es invocar /predict_es separado de un espacio y el texto que se desea analizar, ej.: /predict_es que bueno que ganamos el campeonato 
  El resultado del analisis la aplicacion slack_bot lo posteara como un mensaje abierto para todos los usuarios.
