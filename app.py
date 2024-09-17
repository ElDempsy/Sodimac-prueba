from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    #return "<h1>Rental MultiStorage - Prueba</h1>"
    data={
        'titulo':'Index',
        'bienvenida':'Saludos'
    }
    return render_template('index.html', data=data)

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

if __name__=='__main__':
    app.run(debug=True, port=5000)
