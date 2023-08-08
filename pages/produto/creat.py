import streamlit as st
from datetime import date
import controllers.produtoController as produtoController
import models.Produto as produto

def IncluirPageProduto():
        st.title("CADASTRO DE PRODUTO")
        with st.form(key="include_produto",clear_on_submit=True):
            input_date = st.date_input(label="data de cadastro:".upper(), value=date.today(), format="DD/MM/YYYY")
            input_name = st.text_input(label="Insira o produto:".upper()).upper()
            input_qtd= st.number_input(label="Insira a QTD:".upper(), step=1)
            input_cod_aux = st.text_input(label="Insira o Cod Aux:".upper()).upper()
            input_valor_leilao = st.number_input("Insira o valor leilao:".upper())
            input_valor_loja = st.number_input("Insira o valor loja".upper())
            input_button_submit = st.form_submit_button("Enviar")

        if input_button_submit:
            produto.Produto.data_cadastro = input_date
            produto.Produto.nome = input_name
            produto.Produto.qtd = input_qtd
            produto.Produto.cod_aux = input_cod_aux
            produto.Produto.valor_leilao = input_valor_leilao
            produto.Produto.valor_loja = input_valor_loja

            produtoController.Incluir(produto.Produto(0, input_date, input_name, input_qtd, input_cod_aux, input_valor_leilao, input_valor_loja))
            st.success("PRODUTO CADASTRADO COM SUCESSO!")