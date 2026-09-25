import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px

# Configuração da página (deve ser o primeiro comando)
st.set_page_config(page_title="Telecom Churn Analytics", page_icon="📊", layout="wide")

st.title("📊 Inteligência de Retenção (Churn) - Versão Python")
st.markdown("Dashboard analítico interativo consumindo dados do SQL Server com Pandas e Plotly.")

# Função com cache para evitar consultas repetidas ao banco de dados ao interagir com a tela
@st.cache_data
def load_data():
    # Configurações de Conexão com a sua VM (Hyper-V)
    db_server = '192.168.15.200,1433'
    db_name = 'Portfolio_Telecom'
    db_user = 'sa'
    db_password = 'Carlos@0209' # <-- INSIRA A SENHA AQUI
    
    conn_str = (
        'DRIVER={SQL Server};'
        f'SERVER={db_server};'
        f'DATABASE={db_name};'
        f'UID={db_user};'
        f'PWD={db_password};'
    )
    
    # Conecta, executa a query e carrega direto para um DataFrame do Pandas
    conn = pyodbc.connect(conn_str)
    query = "SELECT * FROM tb_churn_data"
    df = pd.read_sql(query, conn)
    conn.close()
    
    return df

try:
    # 1. Extração dos Dados
    with st.spinner('Conectando ao SQL Server e extraindo dados...'):
        df = load_data()
    
    # 2. Transformação e Cálculo dos KPIs (Data Science / Pandas)
    total_customers = len(df)
    df_churn = df[df['Churn'] == 'Yes'] # Filtra apenas os cancelamentos
    total_churn = len(df_churn)
    churn_rate = (total_churn / total_customers) * 100 if total_customers > 0 else 0
    mrr_lost = df_churn['MonthlyCharges'].sum()

    # 3. Renderização dos KPIs na Interface
    st.markdown("### 📈 Indicadores Executivos")
    
    # Cria 4 colunas responsivas
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    kpi1.metric("Base Total de Clientes", f"{total_customers:,}".replace(',', '.'))
    kpi2.metric("Cancelamentos (Churn)", f"{total_churn:,}".replace(',', '.'))
    kpi3.metric("Taxa de Churn Rate", f"{churn_rate:.2f}%")
    kpi4.metric("MRR Perdido", f"$ {mrr_lost:,.2f}")

    st.divider()

    # 4. Renderização Gráfica com Plotly
    st.markdown("### 🔍 Análise de Ofensores")
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("Evasão por Tipo de Contrato")
        # Agrupa os dados usando Pandas
        churn_by_contract = df_churn['Contract'].value_counts().reset_index()
        churn_by_contract.columns = ['Contrato', 'Cancelamentos']
        
        # Cria gráfico de rosca interativo
        fig_contract = px.pie(churn_by_contract, values='Cancelamentos', names='Contrato', hole=0.4,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_contract, use_container_width=True)

    with chart_col2:
        st.subheader("Evasão por Tecnologia de Internet")
        # Agrupa os dados usando Pandas
        churn_by_internet = df_churn['InternetService'].value_counts().reset_index()
        churn_by_internet.columns = ['Serviço de Internet', 'Cancelamentos']
        
        # Cria gráfico de barras interativo
        fig_internet = px.bar(churn_by_internet, x='Serviço de Internet', y='Cancelamentos',
                              text='Cancelamentos', color='Serviço de Internet',
                              color_discrete_sequence=px.colors.qualitative.Set2)
        fig_internet.update_traces(textposition='outside')
        st.plotly_chart(fig_internet, use_container_width=True)

except Exception as e:
    st.error(f"Erro crítico na execução do pipeline de dados: {e}")