#Route test
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField #Needed functionality
from wtforms.validators import InputRequired
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FinEducation2021TL' #The secret key is rnd

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/dasprojekt')
def dasprojekt():
    return render_template("/dasprojekt.html")

@app.route('/finanztypen')
def finanztypen():
    return render_template("/finanztypen.html")

Preserver = 0
Follower = 0
Independent = 0
Accumulator  = 0

def checkquestionresult(question):
    global Preserver
    global Follower
    global Independent
    global Accumulator

    if question.data == 'The Preserver / Der Beibehalter':
        Preserver += 1

    elif question.data == 'The Follower / Der Mitläufer':
        Follower += 1

    elif question.data == 'The Independent / Der Selbständige':
        Independent += 1

    elif question.data == 'The Accumulator / Der Sammler':
        Accumulator += 1

class TypQuiz(FlaskForm):
    q1 = RadioField(
        "1. Meine Hauptaufgabe bei der Verwaltung meines Geldes ist:",
        choices=[('The Preserver / Der Beibehalter', 'Mein Geld zu schützen, indem ich keine riskanten Ausgaben tätige, die ich möglicherweise bereue.'),
            ('The Follower / Der Mitläufer', 'Aktiv mit meinem Geld zu haushalten, mit dem Ziel Vermögen anzuhäufen.'),
            ('The Independent / Der Selbständige', 'Vor Kaufentscheidungen intensiv Recherchen betreiben.'),
            ('The Accumulator / Der Sammler', 'Auf andere hören, um Ratschläge zum Umgang mit Geld zu erhalten.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q2 = RadioField(
        "2. Wenn es um finanzielle Angelegenheiten geht, stimme ich welcher Aussage am meisten zu?",
        choices=[('The Preserver / Der Beibehalter', 'Geld zu verlieren ist das schlimmste mögliche Ergebnis.'),
            ('The Follower / Der Mitläufer', 'Ich sollte Gelegenheiten zum Geldverdienen schnell wahrnehmen.'),
            ('The Independent / Der Selbständige', 'Ich muss mir die Zeit nehmen, eine geplante Investition zu verstehen, auch wenn ich dadurch vielleicht Chancen verpasse.'),
            ('The Accumulator / Der Sammler', 'Es wäre besser, wenn ich nicht für die Verwaltung meines Geldes zuständig bin.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q3 = RadioField(
        "3. Wenn ich mich für eine Investition entscheide, vertraue ich dem Rat von:",
        choices=[('The Preserver / Der Beibehalter', 'Meiner eigenen Selbstdisziplin.'),
            ('The Follower / Der Mitläufer', 'Meinem Bauchgefühl.'),
            ('The Independent / Der Selbständige', 'Meiner eigenen Recherche.'),
            ('The Accumulator / Der Sammler', 'einer anderen Person.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q4 = RadioField(
        "4. Stell dir vor, du kaufst dir eine Aktie und du siehst, dass die Aktie mehr Wert gewinnt. Wie fühlst du dich:",
        choices=[('The Preserver / Der Beibehalter', 'Erleichtert.'),
            ('The Follower / Der Mitläufer', 'Aufgeregt.'),
            ('The Independent / Der Selbständige', 'Ruhig und rational.'),
            ('The Accumulator / Der Sammler', 'Ich bin froh, dass ich den Rat von jemandem befolge.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q5 = RadioField(
        "5. Welches Wort beschreibt dich im finanziellen Bereich am besten?",
        choices=[('The Preserver / Der Beibehalter', 'Behüter'),
            ('The Follower / Der Mitläufer', 'Händler'),
            ('The Independent / Der Selbständige', 'Informant'),
            ('The Accumulator / Der Sammler', 'Ratsuchende')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q6 = RadioField(
        "6. Wenn es darum geht, einen Plan für den Umgang mit Geld zu verfolgen, was beschreibt deine Denkweise am besten?",
        choices=[('The Preserver / Der Beibehalter', 'Wenn das Befolgen eines Plans hilft, mein Vermögen zu sichern, werde ich es tun.'),
            ('The Follower / Der Mitläufer', 'Ein Plan zu verfolgen ist nicht so wichtig.'),
            ('The Independent / Der Selbständige', 'Ein Plan ist gut, aber bei Investitionsentscheidungen muss ich mitdenken.'),
            ('The Accumulator / Der Sammler', 'Ich neige dazu, den Ratschlägen anderer zu folgen, wenn mir also etwas empfohlen wird, höre ich auf den Rat.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q7 = RadioField(
        "7. Ich fühle mich in Bezug auf mein Geld am sichersten, wenn:",
        choices=[('The Preserver / Der Beibehalter', 'Ich nachts mit dem Wissen schlafen kann, dass mein Vermögen sicher angelegt ist.'),
            ('The Follower / Der Mitläufer', 'Ich in Anlagen investiert habe, die ein hohes Wertsteigerungspotenzial haben.'),
            ('The Independent / Der Selbständige', 'Ich treffe meine eigenen Anlageentscheidungen oder habe zumindest Einfluss auf den Prozess.'),
            ('The Accumulator / Der Sammler', 'Ich bin in Dinge investiert, in die viele andere auch investiert sind.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q8 = RadioField(
        "8. Wenn ein Freund eine &quot;sichere Sache&quot; als Investitionsidee vorschlägt, wäre meine Antwort:",
        choices=[('The Preserver / Der Beibehalter', 'Ich bin normalerweise skeptisch bei dieser Art von Ideen.'),
            ('The Follower / Der Mitläufer', 'Ich liebe solche Ideen und möchte bei Gelegenheit auch sofort handeln.'),
            ('The Independent / Der Selbständige', 'Ich werde selbst recherchieren und dann entscheiden, was zu tun ist.'),
            ('The Accumulator / Der Sammler', 'Ich werde jemand anderen um Rat fragen müssen, bevor ich eine Entscheidung treffe.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q9 = RadioField(
        "9. Stell dir vor, du hast Geld in eine Anlageform investiert. Kurzfristige Schwankungen meines angelegten Geldes führen dazu, dass ich:",
        choices=[('The Preserver / Der Beibehalter', 'Panisch werde und über einen Verkauf nachdenke.'),
            ('The Follower / Der Mitläufer', 'Eine Chance wahrnehme und über einen weiteren Kauf nachdenke.'),
            ('The Independent / Der Selbständige', 'Mich unter Kontrolle fühle, möglicherweise nichts tue.'),
            ('The Accumulator / Der Sammler', 'Jemanden anrufen möchte, um zu erfahren, wie es mit meinem Geld aussieht.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    q10 = RadioField(
        "10. Angenommen du wärst bei einer Sportveranstaltung. Welche Position nimmst du am ehesten ein?",
        choices=[('The Preserver / Der Beibehalter', 'Ein defensiver Spieler.'),
            ('The Follower / Der Mitläufer', 'Ein offensiver Spieler.'),
            ('The Independent / Der Selbständige', 'Stratege/Coach.'),
            ('The Accumulator / Der Sammler', 'Fan.')],
            validators=[InputRequired ('Diese Frage ist unbeantwortet')]
        )

    submit = SubmitField("Submit")

@app.route('/form', methods=['GET', 'POST']) #POST and GET to actually send data via submit
def form():
    form = TypQuiz() #Instantiate the Quizform

    if form.validate_on_submit():

        global Preserver
        global Follower
        global Independent
        global Accumulator

        checkquestionresult(form.q1)
        checkquestionresult(form.q2)
        checkquestionresult(form.q3)
        checkquestionresult(form.q4)
        checkquestionresult(form.q5)
        checkquestionresult(form.q6)
        checkquestionresult(form.q7)
        checkquestionresult(form.q8)
        checkquestionresult(form.q9)
        checkquestionresult(form.q10)

        print('The Preserver: ', Preserver)
        print('The Follower: ', Follower)
        print('The Independent: ', Independent)
        print('The Accumulator: ', Accumulator)

        list1 = [Preserver, Follower, Independent, Accumulator]

        print(" Max Value: ", max(list1))

        if Preserver > Follower and Preserver > Independent and Preserver > Accumulator:
            return render_template("1Preserver.html")

        elif Follower > Preserver and Follower > Independent and Follower > Accumulator:
            return render_template("2Follower.html")

        elif Independent > Preserver and Independent > Follower and Independent > Accumulator:
            return render_template("3Independent.html")

        elif Accumulator > Follower and Accumulator > Independent and Accumulator > Preserver:
            return render_template("4Akkumulator.html")

        else:
            result = "Zu schwierig, sich zu entscheiden. Vielleicht braucht dieses Quiz mehr Fragen."

        Preserver = 0
        Follower = 0
        Independent = 0
        Accumulator = 0

        return '<center><h1> {} !</h1></center> <break> <center><h2> '.format(result)  # Insert jump to fitting Typ-Page here

    return render_template('form.html', form=form)  # Execution website, form included to pass it into the template

app.run(debug=True) #Run the app