import streamlit as st
from st_supabase_connection import SupabaseConnection

# Inicializa a conexão usando os Secrets do Streamlit
conn = st.connection("supabase", type=SupabaseConnection)

def listar_transacoes():
    """Busca todas as transações no banco de dados."""
    try:
        # Nota: Em um sistema multi-usuário, filtraríamos por user_id aqui
        res = conn.table("transacoes").select("*").order("data", desc=True).execute()
        return res.data
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        return []

def salvar_transacao(descricao, valor, tipo, data):
    """Insere uma nova transação no Supabase."""
    try:
        dados = {
            "descricao": descricao,
            "valor": valor,
            "tipo": tipo,
            "data": str(data)
        }
        conn.table("transacoes").insert([dados]).execute()
        return True
    except Exception as e:
        st.error(f"Erro ao salvar: {e}")
        return False