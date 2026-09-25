# 📊 Telecom Churn Analytics: Dual-Stack End-to-End

Este repositório contém uma solução completa de análise de evasão de clientes (Churn), desenvolvida com foco nos desafios reais do setor de telecomunicações. O projeto demonstra a capacidade de transitar entre a Engenharia de Software tradicional e a Ciência de Dados ágil, utilizando o mesmo banco de dados relacional.

## 🏗️ Arquitetura e Tecnologias

*   **Infraestrutura de Dados:** Microsoft SQL Server hospedado em uma Máquina Virtual (Windows Server via Hyper-V) para simular um ambiente corporativo isolado.
*   **Pipeline de Dados (ETL):** Scripts em `Python` (com `pandas` e `pyodbc`) para extração, limpeza (tratamento de nulos/tipos) e carga massiva (Batch Insert) no banco de dados.
*   **Fase 1 - Portal Corporativo (Engenharia de Software):** 
    *   Aplicação web desenvolvida em `C# ASP.NET Core MVC`.
    *   Integração direta com o banco via `Entity Framework Core` (ORM).
    *   Interface responsiva com `CSS Grid` e gráficos com `Chart.js`.
*   **Fase 2 - Advanced Analytics (Ciência de Dados):**
    *   Dashboard interativo construído 100% em `Python` utilizando `Streamlit`.
    *   Agregações e regras de negócio processadas in-memory com `Pandas`.
    *   Visualizações gráficas dinâmicas com `Plotly`.

## 🎯 Objetivo do Negócio
Identificar os principais ofensores de churn (ex: evasão por Tipo de Contrato e Tecnologia de Internet) e calcular o impacto financeiro (MRR - Monthly Recurring Revenue perdido), fornecendo inteligência acionável para equipes de retenção.