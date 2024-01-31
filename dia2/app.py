from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    nombre_args = request.args.get('nombre','nn')
    #monto_origen = request.args.get('monto_origen','0')
    monto_destino = 0
    if request.method == 'POST':
        monto_origen = request.form['monto_origen']
        monto_destino = int(monto_origen) / 3.8
        
    return render_template('index.html',nombre=nombre_args,monto_destino=monto_destino)

app.run(debug=True)