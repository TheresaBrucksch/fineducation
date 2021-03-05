
from flask import Flask, render_template,request, redirect, url_for
import pandas as pd
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/index.html')
def Landing():
    return render_template('index.html')

@app.route('/finanztypen_1Preserver.html')
def Preserver():
    return render_template('finanztypen_1Preserver.html')

@app.route('/finanztypen_2Akkumulator.html')
def Akkumulator()):
    return render_template('finanztypen_2Akkumulator.html')

@app.route('/finanztypen_3Follower.html')
def Follower():
    return render_template('finanztypen_3Follower.html')

@app.route('/finanztypen_4Independents.html')
def Independents():
    return render_template('finanztypen_4Independents.html')

@app.route('/dasprojekt.html')
def Projekt():
    return render_template('dasprojekt.html')

@app.route('/finanztypen.html')
def Finanztypen():
    return render_template('finanztypen.html')

@app.route('/test1.html')
def test():
    return render_template('test1.html')

@app.route('/test1.html'methods=['POST'])
def quiz():

Preserver = 0
Follower = 0
Independent = 0
Accumulator  = 0


class TypQuiz(Form):
    q1 = RadioField(
        "1. Meine Hauptaufgabe bei der Verwaltung meines Geldes ist:",
        choices=[('a', 'Mein Geld zu schützen, indem ich keine riskanten Ausgaben tätige, die ich möglicherweise bereue.'), 
            ('b', 'Aktiv mit meinem Geld zu haushalten, mit dem Ziel Vermögen anzuhäufen.'), 
            ('c', 'Vor Kaufentscheidungen intensiv Recherchen betreiben.'), 
            ('d', 'Auf andere hören, um Ratschläge zum Umgang mit Geld zu erhalten.')]
        )

if q1 == "a":
  Preserver += 1
elif q1 == "b":
  Follower += 1
elif q1 == "c":
  Independent += 1
elif q1 == "d":
  Accumulator += 1
else:
  print("Sorry, ich verstehe diese Antwort nicht.")

    q2 = RadioField(
        "2. Wenn es um finanzielle Angelegenheiten geht, stimme ich welcher Aussage am meisten zu?",
        choices=[('The Preserver / Der Beibehalter', 'Geld zu verlieren ist das schlimmste mögliche Ergebnis.'), 
            ('The Follower / Der Mitläufer', 'Ich sollte Gelegenheiten zum Geldverdienen schnell wahrnehmen.'), 
            ('The Independent / Der Selbständige', 'Ich muss zufrieden sein, dass ich mir die Zeit nehme, eine geplante Investition zu verstehen, auch wenn ich dadurch vielleicht Chancen verpasse.'), 
            ('The Accumulator / Der Sammler', 'Es wäre besser, wenn ich nicht für die Verwaltung meines Geldes zuständig bin.')]
        )

if q2 == "a":
  Preserver += 1
elif q2 == "b":
  Follower += 1
elif q2 == "c":
  Independent += 1
elif q2 == "d":
  Accumulator += 1
else:
  print("Sorry, ich verstehe diese Antwort nicht.")

    q3 = RadioField(
        "3. Wenn ich mich für eine Investition entscheide, vertraue ich dem Rat von:",
        choices=[('a', 'Meiner eigenen Selbstdisziplin.'), 
            ('b', 'Meinem Bauchgefühl.'), 
            ('c', 'Meine eigene Recherche.'), 
            ('d', 'Jemand anderes als ich selbst.')],
        )

if q3 == "a":
  Preserver += 1
elif q3 == "b":
  Follower += 1
elif q3 == "c":
  Independent += 1
elif q3 == "d":
  Accumulator += 1
else:
  print("Sorry, ich verstehe diese Antwort nicht.")

    q4 = RadioField(
        "4. Stell dir vor, du kaufst dir eine Aktie und du siehst, dass die Aktie mehr Wert gewinnt.
        Wie verhältst du dich:",
        choices=[('a', 'Erleichtert.'), 
            ('b', 'Aufgeregt.'), 
            ('c', 'Ruhig und rational.'), 
            ('d', 'Ich bin froh, dass ich den Rat von jemandem befolge.')]
        )

if q4 == "a":
  Preserver += 1
elif q4 == "b":
  Follower += 1
elif q4 == "c":
  Independent += 1
elif q4 == "d":
  Accumulator += 1
else:
  print("Sorry, ich verstehe diese Antwort nicht.")


 if Preserver > Follower and Preserver > Independent and Preserver > Accumulator:
    print("Preserver")
  elif Follower > Preserver and Follower > Independent and Follower > Accumulator:
    print("Follower")
  elif Independent > Preserver and Independent > Follower and Independent > Accumulator:
    print("Independent")
  elif Accumulator > Preserver and Accumulator > Follower and Accumulator > Independent:
    print("Accumulator")
  else:
    print("Zu schwierig, sich zu entscheiden. Vielleicht braucht dieses Quiz mehr Fragen. Du bist geeignet als ")

  mehrheit = []
  if Preserver > 0:
      mehrheit.append("Preserver")
  if Follower > 0:
      mehrheit.append("Follower")
  if Independent > 0:
      mehrheit.append("Independent")
  if Accumulator > 0:
      mehrheit.append("Accumulator")
  for mehrheit in mehrheit:
      print(mehrheit)

    # optional hier bereits TypVerwertung
    
    AnswersList = [q1, q2, q3, q4]

    typetable = pd.DataFrame({
    "Preserver", "Follower", "Independent", "Accumulator" 
    typetable.to_csv(Dateiname1)


    return render_template('test1.html', AnswersList = AnswersList )

app.run(debug=True)







