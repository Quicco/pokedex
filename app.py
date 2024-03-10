from flask import Flask, render_template, request
import sqlite3
import pokebase as pb
from db_commands.region_dexs import regions

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def index():
    choices = regions
    return render_template("index.html", choices=choices)


@app.route("/dex", methods=["GET", "POST"])
def region():

    # Get list of region choices for the inputs
    choices = regions
    # Connect to the database
    con = sqlite3.connect("pokedex.db")
    cur = con.cursor()

    if request.method == "POST":
        region = request.form.getlist("region")

        # Check if any regions were selected
        if not region:
            return render_template("error.html", message="Missing a region.")
        else:
            # placeholders = , ?, ?
            placeholders = ", ".join(["?" for _ in region])
            dex = cur.execute(
                f"SELECT * FROM pokedex WHERE region IN ({placeholders})",
                tuple(region),
            )
            dex = dex.fetchall()
            return render_template(
                "pokedex.html", region=region, dex=dex, pb=pb, choices=choices
            )

    con.close()
    return render_template("index.html")


# Route for an individual page of a pokemon
@app.route("/pkmn", methods=["GET", "POST"])
def pkmn():

    if request.method == "POST":
        # DATA the page needs: DexNº, Name, Types, Region
        id = request.form.get("pkmn-id")
        name = request.form.get("pkmn-name")
        p_type = request.form.get("pkmn-ptype")
        s_type = request.form.get("pkmn-sectype")
        region = request.form.get("pkmn-region")

        return render_template(
            "pkmn-page.html",
            id=id,
            name=name,
            p_type=p_type,
            s_type=s_type,
            region=region,
            pb=pb,
        )
    return render_template("index.html")
