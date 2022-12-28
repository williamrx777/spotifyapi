from flask import Flask,render_template,request, url_for, redirect
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        musicas = request.form['nome']
        return redirect(url_for('musicas',nome=musicas))
    else:    
        return render_template('index.html')
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