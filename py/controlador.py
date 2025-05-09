from funciones import *

app=Flask(__name__)
CORS(app)

carpeta=os.getcwd()

ruta_contactos = os.path.join(carpeta,'json', 'contactos.json')
if not os.path.isfile(ruta_contactos):
    set_json(ruta_contactos, [])
else:
    data = get_json(ruta_contactos)
    
ruta = os.path.join(carpeta,'json', 'preguntas.json')    
if not os.path.isfile(ruta):
    set_json(ruta, [])
else:
    data = get_json(ruta)


@app.route('/insertar', methods=['POST'])


def insertar(name = ruta_contactos):
    '''Carga la información de un cliente en el archivo clientes.json, primero extrae la informacion del
    json y luego lo guarda los nuevos datos en el archivo clientes.json'''
    data = request.json
    clientes =get_json(name)
    clientes.append(data)
    set_json(name, clientes)
    return {"mensaje:": "Clientes insertado de forma correcta" }



@app.route('/consultar', methods=['GET'])

def consultar(name = ruta):
    ''''Carga la información de un cliente en el archivo clientes.json, primero extrae la informacion del'''
    clientes = get_json(name)
    return jsonify(clientes)
    

if __name__=="__main__":
    app.run(debug=True, port=5000)
        
