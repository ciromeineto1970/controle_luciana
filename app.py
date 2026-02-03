import streamlit as st
from modules.auth import check_password

st.set_page_config(page_title="Finanças Pro", layout="wide")

if check_password():
    st.sidebar.success("Bem-vindo ao seu controle financeiro!")
    st.title("🏠 Home")
    
    st.write("""
    ### Dashboard Geral
    Utilize o menu lateral para navegar entre o Dashboard detalhado e o cadastro de transações.
    """)
    
    # Aqui você pode colocar um resumo rápido (Ex: Saldo Total)