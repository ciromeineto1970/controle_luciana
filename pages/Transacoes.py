import streamlit as st
from modules.database import insert_transacao, get_transacoes
import pandas as pd

st.title("Lançamentos")

with st.form("nova_transacao"):
    desc = st.text_input("Descrição")
    valor = st.number_input("Valor", min_value=0.0, step=0.01)
    tipo = st.selectbox("Tipo", ["Receita", "Despesa"])
    cat = st.selectbox("Categoria", ["Lazer", "Alimentação", "Salário", "Contas"])
    data = st.date_input("Data")
    
    if st.form_submit_button("Salvar"):
        insert_transacao(desc, valor, tipo, cat, data)
        st.success("Salvo com sucesso!")

# Exibir dados
data = get_transacoes()
if data.data:
    df = pd.DataFrame(data.data)
    st.table(df)
