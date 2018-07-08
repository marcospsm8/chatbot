from flask import Flask
app = Flask (__name__)

@app.route("/")
def ola():
    return u"Olá Mundo!!"

@app.route("/login")
def login():
    return u"Vem pra copa você também!"    

if __name__ == '__main__':
    app.run()
