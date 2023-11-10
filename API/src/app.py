from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL


app= Flask(__name__)

conexion = MySQL(app)

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql =  'SELECT id, Nombre, Edad, Telefono from employees'
        cursor.execute(sql)
        datos=cursor.fetchall()
        cursos=[]
        for fila in datos:
            curso ={'Codigo': fila[0], 'Nombre': fila[1], 'Edad': fila[2], 'Telefono': fila[3]}
            cursos.append(curso)
        return jsonify({'cursos':cursos, 'mensaje':"Cursos Listados"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        cursor= conexion.connection.cursor()
        sql = "SELECT id, Nombre, Edad, Telefono FROM employees WHERE Nombre = '{0}'".format(codigo)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            curso ={'Codigo': datos[0], 'Nombre': datos[1], 'Edad': datos[2], 'Telefono': datos[3]}
            return jsonify({'cursos':curso, 'mensaje':"Cursos Encontrados"})
        else:
            return jsonify({'mensaje':"Curso no encotrado"})
    except Exception as ex:
        return   jsonify({'mensaje': ex})

@app.route('/cursos', methods=['POST'])
def registrar_curso():
    try:
        #print(request.json)
        cursor= conexion.connection.cursor()
        sql = """INSERT INTO employees (id, Nombre, Edad, Telefono)
        VALUES ('{0}','{1}','{2}',{3})""".format(request.json['codigo'],
        request.json['Nombre'],request.json['Edad'],request.json['Telefono'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de insercion
        return jsonify({'mensaje': "Curso Registrado"})
    except Exception as ex:
        return jsonify({'mensaje':"error"})
    
@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        #print(request.json)
        cursor= conexion.connection.cursor()
        sql = "DELETE FROM employees WHERE id= '{0}'".format(codigo)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de elimnar
        return jsonify({'mensaje': "Curso Eliminado"})
    except Exception as ex:
        return jsonify({'mensaje':"error"})

@app.route('/cursos/<codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    try:
        #print(request.json)
        cursor= conexion.connection.cursor()
        sql = """UPDATE employees SET Nombre ='{0}',Edad ='{1}', Telefono ='{2}'
        WHERE id = '{3}'""".format(request.json['Nombre'],request.json['Edad'],
                                        request.json['Telefono'], codigo)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion de insercion
        return jsonify({'mensaje': "Curso Actualizado"})
    except Exception as ex:
        return jsonify({'mensaje':"error"})

def pagina_no_encontrada(error):
    return "<h1>La pagina no existe</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)
