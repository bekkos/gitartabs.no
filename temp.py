import json
import codecs

db = [
        {
            'id': 0,
            'artist': 'Åge Aleksandersen',
            'title': 'Akkurat No',
            'type': 'AKKORDER',
            'rating': '* * * * *',
            'author': 'bekkos',
            'date': '15.09.2021 04.26',
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
            'date': '15.09.2021 04.26',
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
            'date': '15.09.2021 04.26',
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
        },
        {
            'id': 3,
            'artist': 'Hans Rotmo',
            'title': 'Vårres Jul 2',
            'type': 'AKKORDER',
            'rating': '* * * * *',
            'author': 'bekkos',
            'date': '15.09.2021 04.26',
            'content': ''
        },
        {
            'id': 4,
            'artist': 'Hans Rotmo',
            'title': 'Fjellturn',
            'type': 'AKKORDER',
            'rating': '* * * * *',
            'author': 'OlaNormann',
            'date': '15.09.2021 04.26',
            'content': ''
        },
        {
            'id': 5,
            'artist': 'CC Cowboys',
            'title': 'Ugress Og Vilniss',
            'type': 'AKKORDER',
            'rating': '* * * * *',
            'author': 'bekkos',
            'date': '15.09.2021 04.26',
            'content': 
            '''
[Intro]
C  Am   Em  G  x2
 
[Verse 1]
C        Am          Em                  G
Kanskje vi bare skal ta det litt uten en plan
C        Am          Em                  G
Å løpe avgårde langs kanten som uredde barn
F                   G         F             G
For jeg vet ikke hvor jeg vil feste mitt blikk
F                   G         F             G
Og hvor enn jeg ser så vil jeg no'nytt
 
 
[Chorus]
C      G       Am
Så her går jeg rundt
            Em       G
I ugress og villniss
C      G       Em
Så her går jeg rundt
               G
I ugress og villniss
 
 
[Verse 2]
C               Am               Em        G
Kanskje er det verdt å slippe taket å bare, kjøre på
C               Am               Em        G
å sveve der ute som en sky hvor hele himmelen er blå
F                   G         F             G
men jeg vet ikke hvor jeg skal ta mine skritt
F                   G         F         G
for hvorenn jeg går så ser jeg no'nytt
 
 
[Chorus]
C      G       Am
Så her går jeg rundt
            Em       G
I ugress og villniss
C      G       Em
Så her går jeg rundt
               G
I ugress og villniss
 
 
[Bridge]
F                G              F           G
men jeg vet ikke hvor jeg skal ta mine skritt
F                G              F           G
og jeg vet ikke hvor jeg vil feste mitt blikk
F                G              F           G
Men jeg vet at der inne i mitt hjerte av glass
F                G              F           G
I ugress og villniss er min stemme av kraft
 
 
[Chorus]
C      G       Am
Så her går jeg rundt
            Em       G
I ugress og villniss
C      G       Em
Så her går jeg rundt
               G
I ugress og villniss
 
[Outro]
C       G        Am        Em       G
Her går jeg rundt
C       G        Am        Em       G
Her går jeg rundt
C       G        Am        Em       G
Her går jeg rundt
C       G        Am        Em       G
Her går jeg rundt
            '''
        },
        {
            'id': 6,
            'artist': 'DumDum Boys',
            'title': 'Slave',
            'type': 'TAB',
            'rating': '* * * * *',
            'author': 'bekkos',
            'date': '15.09.2021 04.26',
            'content': 
            '''
[RIFF 1]
<code>
e|------------------|
B|------------------|
G|------------------|
D|----4---4--4-----4|
A|------------------|
E|2-----2--2---2----|
</code>
[RIFF 2]
 <code>
e|-----------|
B|-----------|
G|-----------|
D|----2-----4|
A|2-4---2-4--|
E|-----------|
</code>
[RIFF 3]
 <code>
e|-----------|
B|----------7|
G|----6------|
D|4-7---4-7--|
A|-----------|
E|-----------|
</code>
 
 
[Verse 1]
 
RIFF 1                                RIFF 2
Du kan rive meg opp med lange negler
RIFF 1                                RIFF 2
gi meg navn på dyr som kryper
RIFF 1                                RIFF 2
du kan ringe meg opp fra en anne seng
RIFF 1                                RIFF 2
og kaste glass og flasker når jeg kommer hjem
 
          B
Men det er en ting lille pike
Bm                             RIFF 3 RIFF 1           C#m7      Bm
kanskje du tror det men jeg blir aldri slaven din
 
RIFF 1                                RIFF 2
Hvis du vil kan du ligge øverst
RIFF 1                                RIFF 2
du er så søt du tør og prøver
RIFF 1                                RIFF 2
hvis du har kan jeg godt få litt
RIFF 1                                RIFF 2
for jeg blir en zombie uten kjærlighet
 
          B
Men det er en ting lille pike
Bm                             RIFF 3 RIFF 1           C#m7      Bm
kanskje du tror det men jeg blir aldri slaven din
 
RIFF 1                                RIFF 2
Jeg har sett det før
RIFF 1                                RIFF 2
lat man har mot det man får
RIFF 1                                RIFF 2
bolter dører og vinduer
RIFF 1                                RIFF 2
fader ut i grått og forsvinner
 
          B
Men det er en ting lille pike
Bm                             RIFF 3 RIFF 1           C#m7      Bm
kanskje du tror det men jeg blir aldri slaven din
 
           B
Jeg har ikke sett sånn før
Bm                             RIFF 3 RIFF 1           C#m7      Bm
fatter hvor du vil men jeg gjør det bare aldri
 
[SOLO]
 
 
 
          B
Men det er en ting lille pike
Bm                             RIFF 3 RIFF 1           C#m7      Bm
kanskje du tror det men jeg blir aldri slaven din

            '''
        },
        {
            'id': 7,
            'artist': 'DumDum Boys',
            'title': 'Synd For Deg',
            'type': 'AKKORDER',
            'rating': '* * * * *',
            'author': 'bekkos',
            'date': '15.09.2021 04.26',
            'content': 
            '''
[Verse 1]
 
C             G     Am  D
   Jeg skulle aldri spurt
G           D       Em  D
   nå føler jeg meg lurt
C             G     Am  D
   for jeg snakket sant
G           D       Em  D
   å ga hjerte mitt i pant
C             G     Am  D
   jeg ser deg gjennom røyken
G           D       Em  D
   og broen brenner
C             G     Am  D
   du er litt full og jeg er litt tom
G           D       Em  D
   vi to blir aldri bare venner
 
 
[Pre-Chorus]
G                 C          D
Du ser ut som jeg føøøøøler meg
G    C   D
Synd for deg
 
 
[Chorus]
Em          G        C
Jeg er lett å lede
C           D     Em
om jeg skal samme vei
Em          G        C
Du er helt med
C           D        Em
helt med til du går lei
 
 
[Verse 2]
C             G     Am  D
   Det må ha vært smilet
G           D                Em      D
   jeg har som vanlig kun meg selv å klandre
C             G     Am  D
   så takk for følget deres løyhet
G           D       Em
   løp å lek med noen andre
 
 
[Pre-Chorus]
G                 C          D
Du ser ut som jeg føøøøøler meg
G    C   D
Synd for deg
 
 
[Solo]
Em G C C D Em
 
 
[Pre-Chorus]
G                 C          D
Du ser ut som jeg føøøøøler meg
G    C   D
Synd for deg
G                 C          D
Du ser ut som jeg føøøøøler meg
 
 
[Chorus]
Em          G        C
Jeg er lett å lede
C           D     Em
om jeg skal samme vei
Em          G        C
Du er helt med
C           D        Em
helt med til du går lei
Em          G        C
Jeg er lett å lede
C           D     Em
om jeg skal samme vei
Em          G        C
Du er helt med
C           D        Em
helt med til du går lei
 
 
[Outro]
C             G     Am  D   G
Jeg skulle aldri spurt
            '''
        },
        {
            'id': 8,
            'artist': 'Vømmølgutan',
            'title': 'Flyktningelosen',
            'type': 'AKKORDER',
            'rating': '* * * * *',
            'author': 'bekkos',
            'date': '15.09.2021 04.26',
            'content': 
            '''
[Verse]
 
E                 B        A              E
Vi dro fra Hallemskorsen, en iskald vinterdag
E                 B        A              E
Vi gikk på ski over Blommen, fire mainn i lag
C#m                   A                     E
Losen går først, hain dreie mot øst shølom føre e løst,
E                B                E
Så går vi med flyktningelosen mot fre
 
 
[Verse]
 
E                 B        A              E
Vi skifta los ved brua, over Malsåa
E                 B        A              E
Vi bynt å få opp trua, på at det skull går bra
C#m                   A                     E
Kurs'n e stø i d knejupe snø, vi må kjæmp eller dø
E                B                E
Så går vi med flyktningelosen mot fre
 
 
[Chorus]
 
C#m                  B          A                 E
I grensefjella i det kvitesnø, som spægle sæ mot Veresjøn
E                      B                 E
Her i høgda vi tenne bål, i den stille kveld
 
 
[Verse]
 
E                 B        A              E
Da vi kom t Sjækra, gikk ælva kaill å stri
E                 B        A              E
Vi mått gå t Væstly, shølom vi mesta tid
C#m                   A                     E
En tysker der rundt, vi kasta oss ned, bak et nefaillstre
E                B                E
Der ligg vi bak flyktningelosen, mot fre
 
 
[Verse]
 
E                 B        A              E
Vi tok oss opp i Juldal'n, det va fer seint å snu
E                 B        A              E
Å da det lei utpå mårran, fainn vi ei seterbu
C#m                   A                     E
Vi tar oss inn, i ovn va det brinn, varma kråpp å sinn
E                B                E
Så kvile vi med flyktningelosen, mot fre
 
 
[Chorus]
 
C#m                  B          A                 E
I grensefjella i det kvitesnø, som spægle sæ mot Veresjøn
E                      B                 E
Her i høgda vi tenne bål, i den stille kveld
 
[Solo]
 <code>
e|-----------------13|-------------------|-------------------|-------------------|
B|13------11-10-11---|--11-10------------|-------------------|-------------------|
G|-------------------|--------10---------|---9----10-9-------|-------------------|
D|-------------------|-------------------|10---10------10----|-------------------|
A|-------------------|-------------------|----------------13-|-12-10-8------7-8p7|
E|-------------------|-------------------|-------------------|-------------------|
 
e|-------------------|-------------------|-------------------|-------------------|
B|-------------------|-------------------|---10----11-13-----|-------------------|
G|-----------9-10-9--|----------------10-|12---------------12|-10-9-10-----------|
D|--------10---------|10-----7-8-10------|-------------------|-------------------|
A|-----12------------|-------------------|-------------------|-------------------|
E|8/10---------------|-------------------|-------------------|-------------------|
 </code>
[Saxophone Solo]
 
 
 
[Verse]
 
E                 B        A              E
Vi sov oss igjennom dagen, å gikk da det vart kveill
E                 B        A              E
Vi tok oss over grensa, før vi jol opp eill(eld)
C#m                   A                     E
Inn i Sværri vi går, vår frihet vi får, når med losen vi går
E                B                E
Så drekk vi kaffe med flyktningelosen mot fre
 
 
[Chorus]
 
C#m                  B          A                 E
I grensefjella i det kvitesnø, som spægle sæ mot Veresjøn
E                      B                 E
Her i høgda vi tenne bål, i den stille kveld
OOOOOOH
C#m                  B          A                 E
I grensefjella i det kvitesnø, som spægle sæ mot Veresjøn
E                      B                 E
Her i høgda vi tenne bål, i den stille kveld

            '''
        }

    ]

with codecs.open('tempdb.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False)