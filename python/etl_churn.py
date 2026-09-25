import pandas as pd
import pyodbc
import numpy as np
import os

print("--- INICIANDO PIPELINE DE INGESTÃO DE DADOS ---")

# 1. Configurações de Arquivo e Banco
# Verifique se o nome do arquivo CSV está exatamente assim na sua pasta Data:
caminho_csv = r'C:\Portfolio_Telecom\Data\WA_Fn-UseC_-Telco-Customer-Churn.csv' 
db_server = '192.168.15.200,1433'
db_name = 'Portfolio_Telecom'
db_user = 'sa'
db_password = 'Carlos@0209' # <-- INSIRA A SENHA DA CONTA SA AQUI

# 2. Leitura e Tratamento dos Dados
print("1. Lendo os dados do CSV...")
df = pd.read_csv(caminho_csv)

# Tratamento crítico: A coluna TotalCharges vem como string e contém espaços em branco
print("2. Aplicando regras de limpeza de dados (Data Cleansing)...")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].replace(' ', np.nan))
df['TotalCharges'] = df['TotalCharges'].fillna(0) # Preenche valores nulos com 0

# 3. Conexão com o SQL Server
print(f"3. Conectando ao banco de dados no servidor {db_server}...")
conn_str = (
    'DRIVER={SQL Server};'
    f'SERVER={db_server};'
    f'DATABASE={db_name};'
    f'UID={db_user};'
    f'PWD={db_password};'
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # 4. Inserção em Lote (Batch Insert)
    print("4. Executando inserção em lote (Batch Insert)...")
    insert_query = '''
        INSERT INTO tb_churn_data (
            customerID, gender, SeniorCitizen, Partner, Dependents, tenure, 
            PhoneService, MultipleLines, InternetService, OnlineSecurity, 
            OnlineBackup, DeviceProtection, TechSupport, StreamingTV, 
            StreamingMovies, Contract, PaperlessBilling, PaymentMethod, 
            MonthlyCharges, TotalCharges, Churn
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    '''
    
    # Converte o DataFrame para uma lista de tuplas para o executemany
    records = df.values.tolist()
    cursor.executemany(insert_query, records)
    conn.commit()
    
    print(f"SUCESSO! {len(records)} registros foram inseridos na tabela tb_churn_data.")

except Exception as e:
    print(f"\n[ERRO NA INGESTÃO]: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("--- PIPELINE FINALIZADO ---")