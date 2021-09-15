from flask import Flask, request, render_template, session, url_for, redirect
import json, codecs

app = Flask(__name__)


with codecs.open('tempdb.json', 'r', encoding='utf-8') as f:
    database = json.load(f)

users = [
    {
        'id': 0,
        'username': 'bekkos',
        'email': 'bekkosm@gmail.com',
        'password': 'test',
        'role': 'Administrator',
        'profilepic': 'https://styles.redditmedia.com/t5_8qe12/styles/profileIcon_5jkgogjwghn71.jpg?width=256&height=256&crop=256:256,smart&s=3d18aadd7cf120f900d70b53befb7e20bd1d4a25',
        'gtPoints': 1337
    },
    {
        'id': 1,
        'username': 'OlaNormann',
        'email': 'olanormann@gmail.com',
        'password': 'test',
        'role': 'Bannlyst',
        'profilepic': 'https://bil24.no/wp-content/uploads/2019/09/Ferrari-812-GTS-1.jpg',
        'gtPoints': 0
    },
]

posts = [
    {
        'id': 0,
        'author': 'bekkos',
        'author_id': 0,
        'date': '15.09.2021 05:22',
        'title': 'Hallo Verden',
        'content': 
        '''
        Lorem ipsum dalar tarem!
        Dette er en test.
                Dette er også en test.
                Test
        Hallo Test
            123
        '''
    }, 
    {
        'id': 1,
        'author': 'bekkos',
        'author_id': 0,
        'date': '15.09.2021 05:24',
        'title': 'Hallo Verden 2',
        'content': 
        '''
        Lorem ipsum dalar tarem!
        Dette er en test.
                Dette er også en test.
                Test
        Hallo Test
            123 321 123 321
        '''
    }
]

# Uoptimalisert søkemetode. Bør finne en ny måte.
def searchForElement(cue):
    findings = []
    for x in database:
            if cue.lower() in x['title'].lower() or cue.lower() in x['artist'].lower() or cue.lower() in x['author'].lower():
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

@app.route("/tab", methods = ['GET'])
def displaySong():
    if request.args.get("id") == None:
        return redirect(url_for("index"))
    else:
        song = database[int(request.args.get("id"))]

        print(song["content"])
        return render_template("songview.html", song=song)
    
@app.route("/user", methods = ['GET'])
def user():
    user = None
    for u in users:
        if u['username'] == request.args.get("username"):
            user = u
    if user is None:
        return redirect(url_for("index"))
    else:
        user['password'] = ""
        results = searchForElement(user['username'])
        results = results[::-1]
        results = results[0:6]
        return render_template("userpage.html", user=user, results=results)

@app.route("/artist", methods = ['GET'])
def artist():
    artist = request.args.get("name")
    if artist is None:
        return redirect(url_for("index"))
    else:
        results = searchForElement(artist)
        return render_template("artistpage.html", artist=artist, results=results)

@app.route("/tabs", methods = ['GET'])
def tabs():
    return render_template("tabs.html", results=database)

@app.route("/forum", methods = ['GET'])
def forum():
    return render_template("forum.html", posts=posts[::-1])

@app.route("/forum/post", methods = ['GET'])
def openPost():
    if request.args.get(id) is None:
        return redirect(url_for("forum"))
    post = None
    for p in posts:
        if p['id'] == request.args.get(id):
            post = p
    if post is not None:
        return render_template("postview.html", post=post)
    else:
        return redirect(url_for("forum"))