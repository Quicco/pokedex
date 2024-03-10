import sqlite3
from region_dexs import dex_pokemon

con = sqlite3.connect("pokedex.db")
print("successfully connected to the db")

# Create cursor object
cur = con.cursor()


for pokemon in dex_pokemon:

    cur.execute(
        "INSERT INTO pokedex(pokemon, primary_type, secondary_type, region) VALUES (?, ?, ?, ?);",
        (
            pokemon["pokemon"],
            pokemon["primary_type"],
            pokemon["secondary_type"],
            pokemon["region"],
        ),
    )

print("successfully populated db table")

con.commit()

con.close()
