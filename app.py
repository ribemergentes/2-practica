from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de cursos para el formulario de inscripción
cursos = ['Python Básico', 'JavaScript Avanzado', 'Diseño Web', 'Base de Datos']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'apellidos': request.form.get('apellidos'),
            'curso': request.form.get('curso')
        }
        return render_template('resultado.html', form_name='Inscripción del Curso', data=datos)
    return render_template('inscripcion_curso.html', cursos=cursos)




@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'apellidos': request.form.get('apellidos'),
            'correo': request.form.get('correo'),
            'contraseña': '********'  # Por seguridad, no mostramos la contraseña
        }
        return render_template('resultado.html', form_name='Registro de Usuarios', data=datos)
    return render_template('registro_usuarios.html')




@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        datos = {
            'producto': request.form.get('producto'),
            'categoria': request.form.get('categoria'),
            'existencia': request.form.get('existencia'),
            'precio': request.form.get('precio')
        }
        return render_template('resultado.html', form_name='Registro de Productos', data=datos)
    return render_template('registro_productos.html')



@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        datos = {
            'titulo': request.form.get('titulo'),
            'autor': request.form.get('autor'),
            'resumen': request.form.get('resumen'),
            'medio': request.form.get('medio')
        }
        return render_template('resultado.html', form_name='Registro de Libros', data=datos)
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)