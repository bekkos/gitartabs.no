from flask import Flask, request, render_template, session, url_for, redirect

app = Flask(__name__)

database = [
        {
            'id': 0,
            'artist': 'Åge Aleksandersen',
            'title': 'Dekksguten',
            'type': 'AKKORDER',
            'rating': '* * * * *'
        },
        {
            'id': 1,
            'artist': 'Spidergawd',
            'title': 'Into Tomorrow',
            'type': 'AKKORDER',
            'rating': '* * * * *'
        },
        {
            'id': 2,
            'artist': 'Terje Skaug',
            'title': 'Våpendrager',
            'type': 'AKKORDER',
            'rating': '* * * *'
        },
        {
            'id': 3,
            'artist': 'Elle Melle',
            'title': 'Himmelhøge Sti',
            'type': 'TABLATUR',
            'rating': '* * *'
        },
        {
            'id': 4,
            'artist': 'Odd Norstoga',
            'title': 'Dans Dans Dans',
            'type': 'AKKORDER',
            'rating': '* * * * *'
        },
        {
            'id': 5,
            'artist': 'Odd Norstoga',
            'title': 'Heim Te Mor',
            'type': 'AKKORDER',
            'rating': '* * * * *'
        },
        {
            'id': 6,
            'artist': 'Odd Norstoga',
            'title': 'Frøken Franzen',
            'type': 'AKKORDER',
            'rating': '* * * * *'
        }
    ]

# Uoptimalisert søkemetode. Bør finne en ny måte.
def searchForElement(cue):
    findings = []
    for x in database:
            if cue.lower() in x['title'].lower() or cue.lower() in x['artist'].lower():
                findings.append(x)
    return findings


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        results = searchForElement(request.form.get("cue"))
        if len(results) == 0:
            return render_template("index.html", results=results, empty=True)
        return render_template("index.html", results=results)