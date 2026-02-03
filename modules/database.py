import streamlit as st
from supabase import create_client, Client

# Conecta ao Supabase usando segredos do Streamlit
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

def get_transacoes():
    return supabase.table("transacoes").select("*").execute()

def insert_transacao(descricao, valor, tipo, categoria, data):
    data_dict = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "categoria": categoria,
        "data": str(data)
    }
    return supabase.table("transacoes").insert(data_dict).execute()
