import sqlite3

conn = sqlite3.connect('services/cadastro.db', check_same_thread=False)
cursor = conn.cursor()
