from flask import Flask, render_template, request
import requests

app = Flask(__name__)

base_url = "https://pokeapi.co/api/v2/pokemon/"

@app.route("/", methods=["POST", "GET"])
def show_pokemons():

    if request.method == "POST":
        pokemon = request.form.get("pokemon_name").lower().strip()
    else:
        pokemon = "typhlosion"
    
    try:
        url = base_url + pokemon
        response = requests.get(f"{url}")
        if response.status_code == 200:
            data = response.json()
            sprite_link = data["sprites"]["front_default"]
            print(sprite_link)
            name = data["forms"][0]["name"].capitalize()
            return render_template("index.html", src=sprite_link, pokemon_name=name)
        else:
            return render_template("index.html",pokemon_name=name, alt=f"{pokemon.capitalize()}")
    
    except requests.exceptions.ConnectTimeout:
        return


app.run(host="127.0.0.1", port="80")