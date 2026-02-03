import streamlit as st
import pandas as pd
from modules.database import get_transacoes

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

st.title("📊 Dashboard Financeiro")

# 1. Buscar dados do banco
response = get_transacoes()
data = response.data

if not data:
    st.warning("Nenhum dado encontrado. Vá em 'Transações' para cadastrar.")
else:
    # 2. Transformar em DataFrame para facilitar cálculos
    df = pd.DataFrame(data)
    df['valor'] = df['valor'].astype(float)
    df['data'] = pd.to_datetime(df['data'])

    # 3. Cálculos de resumo
    receitas = df[df['tipo'] == 'Receita']['valor'].sum()
    despesas = df[df['tipo'] == 'Despesa']['valor'].sum()
    saldo = receitas - despesas

    # 4. Exibição de Métricas (Cartões)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Receitas", f"R$ {receitas:,.2f}", delta_color="normal")
    col2.metric("Total Despesas", f"R$ {despesas:,.2f}", delta_color="inverse")
    col3.metric("Saldo Atual", f"R$ {saldo:,.2f}")

    st.markdown("---")

    # 5. Gráficos
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Despesas por Categoria")
        df_despesas = df[df['tipo'] == 'Despesa']
        if not df_despesas.empty:
            cat_chart = df_despesas.groupby('categoria')['valor'].sum()
            st.bar_chart(cat_chart)
        else:
            st.info("Sem despesas para exibir gráfico.")

    with col_right:
        st.subheader("Evolução Mensal")
        # Agrupar por mês/ano e tipo
        df['mes_ano'] = df['data'].dt.to_period('M').astype(str)
        evolucao = df.groupby(['mes_ano', 'tipo'])['valor'].sum().unstack().fillna(0)
        st.line_chart(evolucao)

    # 6. Tabela detalhada
    st.subheader("Últimos Lançamentos")
    st.dataframe(df[['data', 'descricao', 'categoria', 'tipo', 'valor']].sort_values(by='data', ascending=False), use_container_width=True)
