import streamlit as st
from modules.database import listar_transacoes, salvar_transacao
from modules.auth import check_password

# Verifica se o usuário está logado antes de carregar a página
if check_password():
    st.title("📝 Lançamentos Financeiros")

    # --- FORMULÁRIO DE ENTRADA ---
    with st.expander("Adicionar Nova Transação", expanded=True):
        with st.form("form_transacao", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                descricao = st.text_input("Descrição (Ex: Aluguel, Salário)")
                valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
            with col2:
                tipo = st.selectbox("Tipo", ["Receita", "Despesa"])
                data = st.date_input("Data do Lançamento")
            
            submit = st.form_submit_button("Salvar Lançamento")
            
            if submit:
                if descricao and valor > 0:
                    sucesso = salvar_transacao(descricao, valor, tipo, data)
                    if sucesso:
                        st.success("Lançamento salvo com sucesso!")
                        st.balloons()
                else:
                    st.warning("Por favor, preencha a descrição e o valor.")

    # --- LISTAGEM E HISTÓRICO ---
    st.divider()
    st.subheader("Histórico de Movimentações")
    
    dados = listar_transacoes()
    
    if dados:
        # Exibindo em um DataFrame para melhor visualização
        import pandas as pd
        df = pd.DataFrame(dados)
        
        # Renomeando colunas para o usuário
        df_formatado = df.rename(columns={
            'descricao': 'Descrição',
            'valor': 'Valor (R$)',
            'tipo': 'Tipo',
            'data': 'Data'
        })
        
        # Mostra a tabela (removendo colunas técnicas de ID se desejar)
        st.dataframe(df_formatado[['Data', 'Descrição', 'Tipo', 'Valor (R$)']], use_container_width=True)
    else:
        st.info("Nenhuma transação encontrada no banco de dados.")