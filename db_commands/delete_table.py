import sqlite3

con = sqlite3.connect("pokedex.db")
print("successfully connected to the db")

cur = con.execute("DROP TABLE IF EXISTS pokedex")
print("successfully deleted db table")

con.close()
