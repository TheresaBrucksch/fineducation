# Testing TypQuiz
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Alle Typ-Fragen mit Single-Choice Option
class TypQuiz(Form):
    q1 = RadioField(
        "1. Meine Hauptaufgabe bei der Verwaltung meines Geldes ist:",
        choices=[('The Preserver / Der Beibehalter', 'Mein Geld zu schützen, indem ich keine riskanten Ausgaben tätige, die ich möglicherweise bereue.'), 
            ('The Follower / Der Mitläufer', 'Aktiv mit meinem Geld zu haushalten, mit dem Ziel Vermögen anzuhäufen.'), 
            ('The Independent / Der Selbständige', 'Vor Kaufentscheidungen intensiv Recherchen betreiben.'), 
            ('The Accumulator / Der Sammler', 'Auf andere hören, um Ratschläge zum Umgang mit Geld zu erhalten.')],
        validators=[CorrectAnswer('X')]
        )

    q2 = RadioField(
        "2. Wenn es um finanzielle Angelegenheiten geht, stimme ich welcher Aussage am meisten zu?",
        choices=[('The Preserver / Der Beibehalter', 'Geld zu verlieren ist das schlimmste mögliche Ergebnis.'), 
            ('The Follower / Der Mitläufer', 'Ich sollte Gelegenheiten zum Geldverdienen schnell wahrnehmen.'), 
            ('The Independent / Der Selbständige', 'Ich muss zufrieden sein, dass ich mir die Zeit nehme, eine geplante Investition zu verstehen, auch wenn ich dadurch vielleicht Chancen verpasse.'), 
            ('The Accumulator / Der Sammler', 'Es wäre besser, wenn ich nicht für die Verwaltung meines Geldes zuständig bin.')],
        validators=[CorrectAnswer('X')]
        )

    q3 = RadioField(
        "3. Wenn ich mich für eine Investition entscheide, vertraue ich dem Rat von:",
        choices=[('The Preserver / Der Beibehalter', 'Meiner eigenen Selbstdisziplin.'), 
            ('The Follower / Der Mitläufer', 'Meinem Bauchgefühl.'), 
            ('The Independent / Der Selbständige', 'Meine eigene Recherche.'), 
            ('The Accumulator / Der Sammler', 'Jemand anderes als ich selbst.')],
        validators=[CorrectAnswer('X')]
        )

    q4 = RadioField(
        "4. Stell dir vor, du kaufst dir eine Aktie und du siehst, dass die Aktie mehr Wert gewinnt.
        Wie verhältst du dich:",
        choices=[('The Preserver / Der Beibehalter', 'Erleichtert.'), 
            ('The Follower / Der Mitläufer', 'Aufgeregt.'), 
            ('The Independent / Der Selbständige', 'Ruhig und rational.'), 
            ('The Accumulator / Der Sammler', 'Ich bin froh, dass ich den Rat von jemandem befolge.')],
        validators=[CorrectAnswer('X')]
        )

    q5 = RadioField(
        "5. Welches Wort beschreibt dich im finanziellen Bereich am besten?",
        choices=[('The Preserver / Der Beibehalter', 'Behüter'), 
            ('The Follower / Der Mitläufer', 'Händler'), 
            ('The Independent / Der Selbständige', 'Informant'), 
            ('The Accumulator / Der Sammler', 'Ratsuchende')],
        validators=[CorrectAnswer('X')]
        )

    q6 = RadioField(
        "6. Wenn es darum geht, einen Plan für den Umgang mit Geld zu verfolgen, was beschreibt deine Denkweise am besten?",
        choices=[('The Preserver / Der Beibehalter', 'Wenn das Befolgen eines Plans hilft, mein Vermögen zu sichern, werde ich es tun.'), 
            ('The Follower / Der Mitläufer', 'Einem Plan zu folgen ist nicht so wichtig.'), 
            ('The Independent / Der Selbständige', 'Ein Plan ist gut, aber bei Investitionsentscheidungen muss ich mitdenken.'), 
            ('The Accumulator / Der Sammler', 'Ich neige dazu, den Ratschlägen anderer zu folgen; wenn mir also ein Plan empfohlen wird, werde ich ihn befolgen oder ich höre mir einfach die Ideen anderer an.')],
        validators=[CorrectAnswer('X')]
        )

    q7 = RadioField(
        "7. Ich fühle mich in Bezug auf mein Geld am sichersten, wenn:",
        choices=[('The Preserver / Der Beibehalter', 'Ich nachts mit dem Wissen schlafen kann, dass mein Vermögen sicher angelegt ist.'), 
            ('The Follower / Der Mitläufer', 'Ich in Anlagen investiert bin, die ein hohes Wertsteigerungspotenzial haben.'), 
            ('The Independent / Der Selbständige', 'Ich treffe meine eigenen Anlageentscheidungen oder habe zumindest Einfluss auf den Prozess.'), 
            ('The Accumulator / Der Sammler', 'Ich bin in Dinge investiert, in die viele andere auch investiert sind.')],
        validators=[CorrectAnswer('X')]
        ) 

    q8 = RadioField(
        "8. Wenn ein Freund eine &quot;sichere Sache&quot; als Investitionsidee vorschlägt, wäre meine Antwort:",
        choices=[('The Preserver / Der Beibehalter', 'Ich bin normalerweise skeptisch bei dieser Art von Ideen.'), 
            ('The Follower / Der Mitläufer', 'Ich liebe solche Ideen und möchte bei Gelegenheit auch sofort handeln.'), 
            ('The Independent / Der Selbständige', 'Ich werde selbst recherchieren und dann entscheiden, was zu tun ist.'), 
            ('The Accumulator / Der Sammler', 'Ich werde jemand anderen um Rat fragen müssen, bevor ich eine Entscheidung treffe.')],
        validators=[CorrectAnswer('X')]
        )

    q9 = RadioField(
        "9. Stell dir vor, du hast Geld in eine Anlageform investiert. Kurzfristige Schwankungen meines angelegten Geldes führen dazu, dass ich:",
        choices=[('The Preserver / Der Beibehalter', 'Panisch werde und über einen Verkauf nachdenke.'), 
            ('The Follower / Der Mitläufer', 'Eine Chance wahrnehme und über einen Kauf nachdenke.'), 
            ('The Independent / Der Selbständige', 'Mich unter Kontrolle fühle, möglicherweise nichts tue.'), 
            ('The Accumulator / Der Sammler', 'Jemanden anrufen möchte, um zu erfahren, wie es mit meinem Geld aussieht.')],
        validators=[CorrectAnswer('X')]
        )

    q10 = RadioField(
        "10. Angenommen du wärst bei einer Sportveranstaltung. Welche Position nimmst du am ehesten ein?",
        choices=[('The Preserver / Der Beibehalter', 'Ein defensiver Spieler.'), 
            ('The Follower / Der Mitläufer', 'Ein offensiver Spieler.'), 
            ('The Independent / Der Selbständige', 'Stratege/Coach.'), 
            ('The Accumulator / Der Sammler', 'Fan.')],
        validators=[CorrectAnswer('X')]
        )

    # optional hier bereits TypVerwertung
    AnswersList = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    TypA = 
    TypB =
    TypC =
    TypD =

    UserTyp =

    submit = SubmitField("Submit")