from flask import Flask
app = Flask (__name__)

@app.route("/")
def ola():
    return u"Olá Mundo!!"

@app.route("/login")
def login():
    return u"Vem pra copa você também!"    

@app.route("/user")
def user():
    return u"Dê tchau para a copa!"        

if __name__ == '__main__':
    app.run()
