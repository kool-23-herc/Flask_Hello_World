from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)

# @app.route("/contact/")
# def MaPremiereAPI():
#     return "<h2>Ma page de contact</h2>"
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html") 

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user*val_user)
  
@app.route('/somme/<int:val1>/<int:val2>')
def somme(val_user):
    return "<h2>La somme de nos valeurs est : </h2>" + str(val1+val2)


                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>" #comm

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
  
@app.route('/pi/<int:val1>')
def pi(val1):
  if val1%2==0:
    return "<h2>pair</h2>"
  else:
    return "<h2>impaire</h2>"   





def somme_valeurs_saisies():
    somme = 0  
    while True: 
        valeur = input("Entrez une valeur (ou 'stop' pour terminer) : ")
        if valeur.lower() == 'stop':
            break  
        try:
            nombre = float(valeur)
            somme += nombre  
        except ValueError:
            print("Veuillez entrer un nombre valide ou 'stop' pour terminer.")
    print(f"La somme des valeurs saisies est : {somme}")

somme_valeurs_saisies()
    
if __name__ == "__main__":
  app.run(debug=True)

