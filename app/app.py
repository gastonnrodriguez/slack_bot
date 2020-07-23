from slack import WebClient
from joblib import dump, load
import pickle
import flask


# Inicializar aplicación Flask
app = flask.Flask(__name__)
# Definir variable global para el modelo
model = None


def load_trained_model():
    print("Cargando modelo..")
    # Cargar el modelo de Keras que editamos en el Jupyter notebook y está guardado en el archivo: vgg19_saved_model.h5
    global model
    ## SOLUCIÓN
    model = load('./modelo_entrenado.pkl')    
    return model

def prepare_text(text):
    #preparo el texto para correrlo en le modelo
    texto = [texto]
    vectorizer = load('./vectorizer.pkl')
    new_data = vectorizer.transform(texto)
    
        # Retornar texto vectorizado
    return new_data


@app.route("/predict_es", methods=["POST"])
def predict():
    # Inicializo retorno
    data = {"success": False}

    if flask.request.method == "POST":
        if flask.request.files.get("text"):
            # Leer el texto
            texto = flask.request.data
            
            ## SOLUCIÓN
            new_data = prepare_text(texto)

            # Usar el modelo para predecir            
            result = model.predict(new_data)
             # Inicializar el retorno como una lista vacía
            data["sentiment"] = []

            data["sentiment"].append(result)

            # Indicar el éxito de la operación
            data["success"] = True

    # Contesto un JSON
    return flask.jsonify(data)


# Comenzar la ejecución del servidor
if __name__ == "__main__":
    print("Inicializando servidor")
    load_trained_model()
    app.run()


#curl -X POST --data "hoy es una noche hermosa"" 'http://localhost:5000/predict_es'