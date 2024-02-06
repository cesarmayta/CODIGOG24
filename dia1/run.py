from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'status':True,
        'message':'Mi primer api rest con flask'
    }
    return jsonify(context)

if __name__ == '__main__':
    app.run(debug=True)