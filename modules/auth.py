import streamlit as st

def check_password():
    """Retorna True se o usuário tiver uma sessão válida."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("🔒 Acesso Restrito")
        user = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            # Aqui você pode validar contra o Supabase Auth posteriormente
            if user == st.secrets["auth"]["admin_user"] and password == st.secrets["auth"]["admin_password"]:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos")
        return False
    return True