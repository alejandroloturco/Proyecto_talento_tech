from funciones import *

app=Flask(__name__)
#CORS(app)

carpeta=os.getcwd()
ruta = os.path.join(carpeta,'json', 'preguntas.json')       
print('aqui2:' + ruta)  
if not os.path.isfile(ruta):
    print('aqui3:' + ruta)
    set_json(ruta, [])
else:
    data = get_json(ruta)


@app.route('/insertar', methods=['POST'])

def insertar(name):
    '''Carga la información de un cliente en el archivo clientes.json, primero extrae la informacion del
    json y luego lo guarda los nuevos datos en el archivo clientes.json'''
    data = request.json()
    clientes =get_json(name)
    clientes.append(data)
    set_json(name, clientes)
    return {"mensaje guardado:": "Clientes insertado de forma correcta" }
    

if __name__=="__main__":
    app.run(debug=True, port=5000)
        
