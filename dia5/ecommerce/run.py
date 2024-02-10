from app import create_app

app = create_app()

@app.route('/')
def index():
    return '<h1>api rest</h1>'
    
app.run(debug=True)