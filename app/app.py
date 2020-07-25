from slack import WebClient
from joblib import dump, load
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


@app.route("/slack_challenge", methods=["POST"])
def answerChallenge():
    value = flask.request.json
    print(value)
    return "OK"
@app.route("/predict_es", methods=["POST"])
def predict():
    texto = flask.request.data
   

    # Inicializo retornoc
    #data = {"success": False}

    if flask.request.method == "POST":
       # if flask.request.data():
      # Leer el texto
      texto = flask.request.data
      print(texto)
      
      new_data = prepare_text(texto)

      # Usar el modelo para predecir            
      result = model.predict(new_data)
      valor = ""
      if result[0] == 0:
          valor = "negativo"
      elif result[0] == 1:
          valor = "positivo"
     
    #flask.jsonify(data)
    return valor


# Comenzar la ejecucion del servidor
if __name__ == "__main__":
    print("Inicializando servidor")
    load_trained_model()
    app.run(host='0.0.0.0', port=80)


#curl -X POST --data "hoy es una noche hermosa"" 'http://localhost:5000/predict_es'