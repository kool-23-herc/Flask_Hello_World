from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template('contact.html')

@app.route('/calcul_carre/<int:val>')
def carre(val):
    return "<h2>Le carré de la valeur est : </h2>" + str(val*val)

@app.route('/somme/<int:val1>/<int:val2>')
def somme(val1,val2):
    return "<h2>La somme de vos valeurs est : </h2>" + str(val1+val2)

@app.route('/parite/<int:val>')
def parite(val):
    if val%2==0:
        return "La valeur que vous avez donné est paire"
    else:
        return "La valeur que vous avez donné est impaire"

@app.route('/sommetotale/<path:val>')
def sommetot(val):
    sommet = list(map(int, val.split('/')))
    sommetotale = sum(sommet)
    return "La somme totale des valeurs est :" + str(sommetotale)

@app.route('/cnam/')
def cnampage():
    return render_template('cnam.html')

if __name__ == "__main__":
  app.run(debug=True)
