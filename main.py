from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    database='aula3',
    password=''
)

cursor = conexao.cursor()

#inserir na tabela
# nome = "Felix tetsrae 3h24"
# idade = 33
# contacto = "879993283"
#
# query = f"INSERT INTO user(nome, idade, contacto) VALUES ('{nome}','{idade}','{contacto}')"
# cursor.execute(query)
# conexao.commit()

#LER DADOS DA BASE DE DADOS
@app.route('/')
def index():
    ler = "SELECT * FROM user"
    cursor.execute(ler)
    dados = cursor.fetchall()

    return render_template("index.html", dados=dados)
@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    idade = request.form['idade']
    contacto = request.form['contacto']

    cursor.execute(f'INSERT INTO user (nome, idade, contacto) VALUES ("{nome}", {idade}, "{contacto}")')
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    cursor.execute(f"SELECT * FROM user WHERE id = {id}")
    dados=cursor.fetchall()
    return render_template("editar.html", resultados=dados)

@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    nome = request.form['nome']
    idade = request.form['idade']
    contacto = request.form['contacto']

    cursor.execute(f'UPDATE user set nome = "{nome}", idade = "{idade}", contacto = "{contacto}" where id = {id}')
    conexao.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):

    cursor.execute(f'DELETE FROM user where id = {id}')
    conexao.commit()
    return redirect(url_for('index'))


#ACTUALIZAR DADOS DO USER
# id=2
# nome="Felix Nome actual"
# idade=10
# contacto="1234567890"
# alterar = f"UPDATE user SET nome='{nome}',`idade`='{idade}',`contacto`='{contacto}' WHERE id = {id}"
# cursor.execute(alterar)
# conexao.commit()
# cursor.close()
# conexao.close()

#apagar um dado
deleteid = 4
delete = f"DELETE FROM user WHERE id = {deleteid}"
cursor.execute(delete)
conexao.commit()
# cursor.close()
# conexao.close()

# print(dados)

if __name__ == '__main__':
    app.run()
