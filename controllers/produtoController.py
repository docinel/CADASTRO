import services.database as db
import models.Produto as Produto


def Incluir(Produto):
    db.cursor.execute('''
INSERT INTO produto(data_cadastro, nome, qtd, cod_aux, valor_leilao, valor_loja)
VALUES(?,?,?,?,?,?)''', (Produto.data_cadastro, Produto.nome, Produto.qtd, Produto.cod_aux, Produto.valor_leilao, Produto.valor_loja)).rowcount
    db.conn.commit()


def SelecionarTodos():
    db.cursor.execute("SELECT * FROM PRODUTO")
    productList = []

    for row in db.cursor.fetchall():
        productList.append(Produto.Produto(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    return productList
