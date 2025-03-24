from flask import Flask, render_template, request
from wsgiref.simple_server import make_server

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    return render_template('vastaus.html', nimi=request.args['nimi'])

@app.route("/bigwin")
def bigwin():
    return render_template('bigwin.html', massi=request.args['massi'])
@app.route("/cheeky")
def cheeky():
    return render_template('cheeky.html')

if __name__ == "__main__":
    #app.run()
    try: 
        with make_server("localhost", 8000, app) as server: 
            server.serve_forever()
    except KeyboardInterrupt:
        print("hei hei")