import streamlit as st
import pages.produto.creat as PageIncluirProduto
import pages.produto.list as PageListProduto


st.sidebar.title("MENU")
Page_Produto = st.sidebar.selectbox('PRODUTOS', ['Incluir', 'Consultar'])

if Page_Produto == 'Consultar':
    PageListProduto.ListPageProduto()

if Page_Produto == 'Incluir':
    PageIncluirProduto.IncluirPageProduto()

