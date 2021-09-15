from flask import Flask, request, render_template, session, url_for, redirect
from jinja2 import Template

app = Flask(__name__)


database = [
        {
            'id': 0,
            'artist': 'Åge Aleksandersen',
            'title': 'Akkurat No',
            'type': 'AKKORDER',
            'rating': '* * * * *',
            'author': 'bekkos',
            'content':
            '''
[Intro]
D A7 D Bm D

[Verse]
D          A7           D         Bm
Akkurat no legg en båt i fra ei lita kai
        G          Em          D
Akkurat no står ei gammel dame opp
        Bm       A             Em        D
Akkurat no kokes kaffe før man reise på jobb
        A          G           D
Akkurat no skimtes sola bak en topp

[Verse]
D          A7           D         Bm
Akkurat no e det regnvær over trøndelag
        G          Em          D
Akkurat no e det klart og fint i sør
        Bm       A             Em        D
Akkurat no sår en bonde korn i fruktbar jord
        A          G           D
Akkurat no e det i Longyearby'n det snør

[Verse]
D          A7           D         Bm
Akkurat no e det no'n som slit med ensomhet
        G          Em          D
Akkurat no e venna go' å ha
        Bm       A             Em        D
Akkurat no e det to som finn si kjærlighet
        A          G           D
Akkurat no e det no'n som skille lag

[Solo]
[Guitar 1]
F – C | F – Dm || Bb – Gm | F ||
Dm – C | Gm – F || C – Bb | Dm – C ||
Bb - Gm | A – A7 | D

<code>
[Guitar 2]
e|-----------------------|------------------------------|
B|-----------------------|------------------------------|
G|-----------------------|------------------------------|
D|-----------------------|------------------------------|
A|-3----5----8---10--12--|12--10--12--13--12--10--10--12|
E|-----------------------|------------------------------|
 
e|-----------------------|------------------------------|
B|-----------------------|------------------------------|
G|------------7-7-7-7--10|-9--7--5----------------------|
D|-----------------------|---------7--------------------|
A|10--8----8-------------|------------------------------|
E|-----------------------|------------------------------|
 
e|-----------------------|------------------------------|
B|-----------------------|------------------------------|
G|5-7-10-12-14--5-7-10-14|-12---14--15--14-12-9-12b-----|
D|-----------------------|------------------------------|
A|-----------------------|------------------------------|
E|-----------------------|------------------------------|
 
e|-----------------------|------------------------------|
B|10-10/8--10-8-6--------|-----------------------10-10/8|
G|----------------7-5-7--|--14--15--14-12-9-12b---------|
D|-----------------------|------------------------------|
A|-----------------------|------------------------------|
E|-----------------------|------------------------------|
 
e|-----------------------|------------------------------|
B|-8-8/6-----------------|------------------------------|
G|--------7-5-7----------|------------------------------|
D|-----------------------|------------------------------|
A|-----------------------|------------------------------|
E|-----------------------|------------------------------|
</code>

[Verse]
D          A7           D         Bm
Akkurat no blir det født en liten guttunge
        G          Em          D
Akkurat no endt et liv så alt for fort
        Bm       A             Em        D
Akkurat no fell et slag som gir varige sår
        A          G           D
Akkurat no stryk ei hund all smerte bort

[Verse]
        D        A7          D            Bm
Akkurat no e det blå dis over hav og land
        G        Em              D
Akkurat no e det kveld i Nord og Sør
        Bm        A          Em     D               A  G  D
Akkurat no e det godt å bo i Norges land – Akkurat no
        Bm        A          Em     D               A  G  D
Akkurat no e det godt å bo i Norges land – Akkurat no
            '''
        },
        {
            'id': 1,
            'artist': 'Spidergawd',
            'title': 'Into Tomorrow',
            'type': 'AKKORDER',
            'rating': '* * * * *',
            'author': 'bekkos',
            'content':
            '''
Intro:
<code>
e|-------------------------------------|
B|-------------------------------------|
G|-------------------------------------|
D|--7-7-9-7-7-7-9-7-7-7-9-7-7-5-5-6----|   x 2
A|--5-5-5-5-5-5-5-5-5-5-5-5-5-3-3-4----|
E|-------------------------------------|
</code>

Første vers, litt rolig
D             Bb        F        C
Looking for a brand new place to begin
    G                  D
And I can be there for you
Bb          F         C      G
You can run off and I follow into
  Intro-riff
a brand new tomorrow

Skru opp til 11 her!
D                      Bb      F     C
Well you feel like I'm getting closer
     G                            D
Just pretend that you are walking away
     Bb       F      C
In a way I've always known
               G
Where you'd be heading

D                  Bb          F             C
I ain't the one to lie just to make you feel better
      G                     D
But I guess that I can look away
      Bb          F      C        A
To be ready for a better day      


Refreng:
D
Come on, yeah come on now
                             C  G
Death can always make you an angel
D
We can be all you want us to be
                             C  G
Death will always meet us as angels


Mellomspill
<code>
e|--------------------------------------|
B|--------------------------------------|
G|--------------------------------------|
D|------------------------------5-7-7---|
A|---5-0-3-7-5-3-2-3--5-0-3-7-5---------|
E|--------------------------------------|
</code>

D                   Bb        F           C
The city where they sleep and all tend to hide
G                    D
I am going back from everyone
Bb              F        C        G
Longing for the break of day      

    D                    Bb   F     C
Oh, stick with me and we wait until morning
    G                         D
The sun will be like going to hell
       Bb         F     C             A
What a start on a new tomorrow        


Refreng

Mellomspill x 2

Solo

Mellomspill 2: D Bb F C G

Refreng


Siste refreng (med alernativ tekst)
D
Something new, something borrowed
                        C   G
as we head into a new tomorrow
D
Give your blues, give your sorrow
                        C   G
as we head into a new tomorrow

Outro:
D C G F
            '''
        },
        {
            'id': 2,
            'artist': 'Terje Skaug',
            'title': 'Våpendrager',
            'type': 'AKKORDER',
            'rating': '* * * *',
            'author': 'bekkos',
            'content':
            '''
G                  C
Morran gløder ifra start
D                  C
våkner av sol over alt
G                        C
Frokost og du som kommer ned
        Em           D             C
og jeg er han du deler første koppen med


Am                           D
Så blir jeg redd du har tatt feil
    G          Bm                C     G
at du aldri egentlig var ment til meg
Am                      D
at du en kald kveld angrer deg


G                      Bm       C   G
Vil du ha en som bærer tunge dager
G        Am              G        D
går du i krig er jeg din våpendrager
        G               D
vil du ha en som løfter blikket ditt
    C          G
som tåler at du knekker litt
Am                     Em
som aldri ser en annen vei
C      Am             Em
da skal du holde fast i meg


G                  C
Syltetøy og trøtte smil
D                  C
vi tryller frem to timer til
G                  C
for du er lys lys lys
        Em           D             C
mot øyelokk som ikke kjennes tjukke nok


Am                           D
Men blir jeg redd du har tatt feil
    G          Bm                C     G
og at du aldri egentlig var ment til meg
Am                      D
at du en kald kveld angrer deg


G                      Bm       C   G
Vil du ha en som bærer tunge dager
G        Am              G        D
går du i krig er jeg din våpendrager
        G               D
vil du ha en som løfter blikket ditt
    C          G
som tåler at du knekker litt
Am                     Em
som aldri ser en annen vei
C      Am             Em
da skal du holde fast i meg


Em                  B
Så stikker livet av sted
                    G
og uten at vi kjenner det
                    A
så har vi plutselig blitt gamle
                    F
og alt vi har da er hverandre
        D
så får vi se


Am                           D
Men blir jeg redd du har tatt feil
    G          Bm                C     G
og at du aldri egentlig var ment til meg
Am                      D
at du en kald kveld angrer deg


G                      Bm       C   G
Vil du ha en som bærer tunge dager
G        Am              G        D
går du i krig er jeg din våpendrager
        G               D
vil du ha en som løfter blikket ditt
    C          G
som tåler at du knekker litt
Am                     Em
som aldri ser en annen vei
C      Am             Em
da skal du holde fast i meg
G
i meg
            '''
        }
    ]

users = [
    {
        'id': 0,
        'username': 'bekkos',
        'email': 'bekkosm@gmail.com',
        'password': 'test',
        'role': 'Administrator',
        'gtPoints': 5
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
        return render_template("userpage.html", user=user, results=results)
