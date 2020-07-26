from slack import WebClient
from joblib import dump, load
from waitress import serve
#from tensorflow.keras import load_model

import flask


# Inicializar aplicacion Flask
app = flask.Flask(__name__)
# Definir variable global para el modelo
model = None


def load_trained_model():
    print("Cargando modelo..")
    
    global model
    
    model = load('./modelo_entrenado.pkl')    
    return model

def prepare_text(text):
    #preparo el texto para correrlo en le modelo
    texto = [text]
    vectorizer = load('./vectorizer.pkl')
    new_data = vectorizer.transform(texto)
    
        # Retornar texto vectorizado
    return new_data

""" #CNN model
#def load_keras_model():
    print("cargando modelo keras..")
    global modelo_keras
    modelo_keras = load_model('../modelo_CNN.h5')
    modelo_keras._make_predict_function()
    print("Modelo cargado")

#def prepare_text_keras(text):
    #preparo el texto para correrlo en le modelo
    tokenizer = load('../tokenizerCNN.pkl')
    instance = tokenizer.texts_to_sequences(text)
    flat_list = []
    for sublist in instance:
        for item in sublist:
            flat_list.append(item)

    flat_list = [flat_list]
    
    # Retornar texto vectorizado
    return flat_list
 """

@app.route("/slack_challenge", methods=["POST"])
def answerChallenge():
    value = flask.request.json
    challenge = value["challenge"]
    print(challenge)

    return challenge
@app.route("/predict_es", methods=["POST"])
def predict_es():
    
    valor = ""

    # Inicializo retornoc
    #data = {"success": False}

    if flask.request.method == "POST":
       # if flask.request.data():
      # Leer el texto
      
      texto = flask.request.form["text"]
      print(texto)
      
      new_data = prepare_text(texto)

      # Usar el modelo para predecir            
      result = model.predict(new_data)
    
      if result[0] == 0:
          valor = "El resultado del analisis de sentimiento es: negativo"
      elif result[0] == 1:
          valor = "El resultado del analisis de sentimiento es: positivo"

    data = {}
    data["response_type"] = "in_channel"
    data["text"] = valor
    #flask.jsonify(data)
    return flask.jsonify(data)

""" @app.route("/predict_en", methods=["POST"])
def predict_en():
    
    valor = ""

    # Inicializo retornoc
    #data = {"success": False}

    if flask.request.method == "POST":
       # if flask.request.data():
      # Leer el texto
      
      texto = flask.request.form["text"]
      print(texto)
      
      new_data = prepare_text_keras(texto)

      # Usar el modelo para predecir            
      result = model.predict(new_data)
    
      if result[0] == 0:
          valor = "Sentiment analysis result is: : negative"
      elif result[0] == 1:
          valor = "Sentiment analysis result is: : positive"

    data = {}
    data["response_type"] = "in_channel"
    data["text"] = valor
    #flask.jsonify(data)
    return flask.jsonify(data)
 """


# Comenzar la ejecucion del servidor
if __name__ == "__main__":
    print("Inicializando servidor")
    load_trained_model()
    #load_keras_model()
    serve(app.run(host='0.0.0.0', port=8080))

