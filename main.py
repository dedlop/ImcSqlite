import sqlite3

con = sqlite3.connect('imc.db')
cur = con.cursor()

#cur.execute("CREATE TABLE paciente (nome text, imc float, situacao text)")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc  = float(peso / (altura * altura))

if imc < 18.5:
    situacao = "Baixo peso"
    cur.execute("INSERT INTO paciente VALUES (?, ?, ?)", (nome, imc, situacao))
    con.commit()
elif imc >= 18.5 and imc <= 24.99:
    situacao = "Peso normal"
    cur.execute("INSERT INTO paciente VALUES (?, ?, ?)", (nome, imc, situacao))
    con.commit()
elif imc >= 25 and imc <= 29.99:
    situacao = "Sobrepeso"
    cur.execute("INSERT INTO paciente VALUES (?, ?, ?)", (nome, imc, situacao))
    con.commit()
else:
    situacao = "Obesidade"
    cur.execute("INSERT INTO paciente VALUES (?, ?, ?)", (nome, imc, situacao))
    con.commit()

cur.execute("SELECT * FROM paciente")
print(cur.fetchall())

con.close()