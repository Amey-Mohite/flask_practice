from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
   port = int(os.getenv('PORT'))
   app.run(debug=True, port=port)
