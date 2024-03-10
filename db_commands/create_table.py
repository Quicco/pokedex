import sqlite3

con = sqlite3.connect("pokedex.db")
print("successfully connected to the db")

# Create cursor object
cur = con.cursor()

cur.execute(
    "CREATE TABLE pokedex(id INTEGER PRIMARY KEY, pokemon TEXT, primary_type TEXT, secondary_type TEXT, region TEXT);"
)
print("successfully created db table")

con.commit()

con.close()
