import streamlit as st
import controllers.produtoController as produtoController
import pandas as pd


def ListPageProduto():
    st.title("LISTAGEM DE PRODUTO")
    productList = []

    for item in produtoController.SelecionarTodos():
        productList.append([item.data_cadastro, item.nome, item.qtd, item.cod_aux, item.valor_leilao, item.valor_loja])

    df = pd.DataFrame(
        productList,
        columns=['CADASTRO', 'NOME', 'QTD', 'COD AUX', 'VALOR FEIRAO', 'VALOR LOJA']
    )

    st.table(df)
    st.markdown(
        """
        <style>
            .stTable {
                font-size: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
