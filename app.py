from flask import Flask,render_template,request, url_for, redirect
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        musicas = request.form['nome']
        return redirect(url_for('musicas',nome=musicas))
    else:
        url = "https://spotify23.p.rapidapi.com/playlist_tracks/"

        querystring = {"id":"6yEH3EWPkCaKn21BCc3yCN","offset":"0","limit":"100"}

        headers = {
	        "X-RapidAPI-Key": "a20c999515msh9ad00c73d2b660ap1c376ajsn2046be0cfe12",
	        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring) 
        res = response.json() 
        link = res['items'][0]['track']['uri']
        imagem = res['items'][0]['track']['album']['images'][1]['url']
        link1 = res['items'][1]['track']['uri']
        imagem1 = res['items'][1]['track']['album']['images'][1]['url']
        link2 = res['items'][2]['track']['uri']
        imagem2 = res['items'][2]['track']['album']['images'][1]['url']
        link3 = res['items'][3]['track']['uri']
        imagem3 = res['items'][3]['track']['album']['images'][1]['url']
        link4 = res['items'][4]['track']['uri']
        imagem4 = res['items'][4]['track']['album']['images'][1]['url']
        link5 = res['items'][5]['track']['uri']
        imagem5 = res['items'][5]['track']['album']['images'][1]['url']
        link6 = res['items'][6]['track']['uri']
        imagem6 = res['items'][6]['track']['album']['images'][1]['url']
        link7 = res['items'][7]['track']['uri']
        imagem7 = res['items'][7]['track']['album']['images'][1]['url']
        link8 = res['items'][8]['track']['uri']
        imagem8 = res['items'][8]['track']['album']['images'][1]['url']
        link9 = res['items'][9]['track']['uri']
        imagem9 = res['items'][9]['track']['album']['images'][1]['url']
        link10 = res['items'][10]['track']['uri']
        imagem10 = res['items'][10]['track']['album']['images'][1]['url']
        link11 = res['items'][11]['track']['uri']
        imagem11 = res['items'][11]['track']['album']['images'][1]['url']
        return render_template('index.html',link=link,imagem=imagem,link1=link1,imagem1=imagem1,link2=link2,imagem2=imagem2,link3=link3,imagem3=imagem3,link4=link4,imagem4=imagem4,link5=link5,imagem5=imagem5,link6=link6,imagem6=imagem6,link7=link7,imagem7=imagem7,link8=link8,imagem8=imagem8,link9=link9,imagem9=imagem9,link10=link10,imagem10=imagem10,link11=link11,imagem11=imagem11)
@app.route('/musicas/<nome>')
def musicas(nome=None):
    url = "https://spotify23.p.rapidapi.com/search/"
    musica = nome
    querystring = {"q": musica,"type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}

    headers = {
	"X-RapidAPI-Key": "a20c999515msh9ad00c73d2b660ap1c376ajsn2046be0cfe12",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    musica = response.json()
    uri = musica['albums']['items'][0]['data']['artists']['items'][0]['uri']
    name = musica['albums']['items'][0]['data']['name']
    imagem = musica['albums']['items'][0]['data']['coverArt']['sources'][0]['url']
    return render_template('musicas.html', uri=uri, musica=musica, name=name, imagem=imagem)
if __name__ == '__name__':
    app.run(debug=True)    