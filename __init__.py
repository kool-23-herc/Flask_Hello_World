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

@app.route('/exercice_base1/')
def exerciceBase():
    return render_template('exercice_base1.html')

@app.route('/exercice_base2/')
def exerciceBase2():
    return render_template('exercice_base2.html')
  
@app.route('/exercice_base3/')
def exerciceBase3():
    return render_template('exercice_base3.html')

@app.route('/formulaire/')
def formulaire():
    return render_template('formulaire.html')

@app.route('/tp1/')
def tp1():
    return render_template('tp1.html')

@app.route('/maison/')
def maison():
    return render_template('maison.html')

@app.route('/vallet/')
def vallet():
    return render_template('vallet.html')

@app.route('/chenille/')
def chenille():
    return render_template('chenille.html')
  
if __name__ == "__main__":
  app.run(debug=True)
