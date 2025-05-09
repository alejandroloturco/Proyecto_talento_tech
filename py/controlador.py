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

ruta_registro = os.path.join(carpeta,'json', 'registros.json')    
if not os.path.isfile(ruta_registro):
    set_json(ruta_registro, [])
else:
    data = get_json(ruta_registro)

ruta_cuestionario = os.path.join(carpeta,'json', 'cuestionario.json')    
if not os.path.isfile(ruta_cuestionario):
    set_json(ruta_cuestionario, [])
else:
    data = get_json(ruta_cuestionario)


@app.route('/insertar_contactanos', methods=['POST'])

def insertar_contactanos(name = ruta_contactos):
    '''Carga la información de un cliente en el archivo clientes.json, primero extrae la informacion del
    json y luego lo guarda los nuevos datos en el archivo clientes.json'''
    data = request.json
    clientes =get_json(name)
    clientes.append(data)
    set_json(name, clientes)
    return {"mensaje:": "Clientes insertado de forma correcta" }

@app.route('/insertar_registros', methods=['POST'])

def insertar_registros(name = ruta_registro):
    '''Carga la información de un cliente en el archivo clientes.json, primero extrae la informacion del
    json y luego lo guarda los nuevos datos en el archivo clientes.json'''
    data = request.json
    clientes =get_json(name)    
    clientes.append(data)
    set_json(name, clientes)
    return {"mensaje:": "Clientes insertado de forma correcta" }

@app.route('/insertar_cuestionario', methods=['POST'])

def insertar_cuestionario(name = ruta_cuestionario):
    '''Carga la información de un cliente en el archivo clientes.json, primero extrae la informacion del
    json y luego lo guarda los nuevos datos en el archivo clientes.json'''
    data = request.json
    clientes =get_json(name)
    clientes.append(data)
    set_json(name, clientes)
    return {"mensaje:": "Clientes insertado de forma correcta" }



'''@app.route('/consultar_registros', methods=['GET'])

def consultar(name = ruta):
    Carga la información de un cliente en el archivo clientes.json, primero extrae la informacion del
    clientes = get_json(name)
    return jsonify(clientes)'''
    

if __name__=="__main__":
    app.run(debug=True, port=5000)
        
