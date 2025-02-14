# from flask import Flask
# from flask import render_template
# from flask import json
# import sqlite3
                                                                                                                                       
# app = Flask(__name__)

# # @app.route("/contact/")
# # def MaPremiereAPI():
# #     return "<h2>Ma page de contact</h2>"
# @app.route("/contact/")
# def MaPremiereAPI():
#     return render_template("contact.html") 

# @app.route('/calcul_carre/<int:val_user>')
# def carre(val_user):
#     return "<h2>Le carré de votre valeur est : </h2>" + str(val_user*val_user)
  
# @app.route('/somme/<int:val1>/<int:val2>')
# def somme(val_user):
#     return "<h2>La somme de nos valeurs est : </h2>" + str(val1+val2)


                                                                                                                                       
# @app.route('/')
# def hello_world():
#     return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>" #comm

# @app.route('/exercices/')
# def exercices():
#     return render_template('exercices.html')
  
# @app.route('/pi/<int:val1>')
# def pi(val1):
#   if val1%2==0:
#     return "<h2>pair</h2>"
#   else:
#     return "<h2>impaire</h2>"   


# if __name__ == "__main__":
#   app.run(debug=True)






from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html") 

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user*val_user)
  
@app.route('/somme/<int:val1>/<int:val2>')
def somme(val1, val2):
    return "<h2>La somme de nos valeurs est : </h2>" + str(val1 + val2)

@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
  
@app.route('/pi/<int:val1>')
def pi(val1):
    if val1 % 2 == 0:
        return "<h2>pair</h2>"
    else:
        return "<h2>impaire</h2>"

@app.route('/somme/')
def afficher_formulaire_somme():
    return render_template('somme.html')

@app.route('/calculer_somme', methods=['POST'])
def calculer_somme():
    valeurs = request.form['valeurs']
    valeurs_liste = [int(v) for v in valeurs.split(',')]
    somme_valeurs = sum(valeurs_liste)
    return f"<h2>La somme des valeurs est : {somme_valeurs}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
