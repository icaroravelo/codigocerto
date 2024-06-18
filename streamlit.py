import streamlit as st
import pandas as pd
import seaborn as sns

# Importar arquivo txt e exportar arquivo csv 
dados = pd.read_csv('dados.txt')
dados.to_csv('dados.csv', index=False)

# Importar arquivo csv 
df = pd.read_csv('dados.csv')

################################### LAYOUT ###################################


# Título da página 
st.header('Visualização de dados - Código Certo') 

# Exibir os dados na tela para checar a conexão (Tabela)
# st.table(df)

# OPÇÕES DE SELEÇÃO 
opcoes = ['Home', 'Vendas', 'Cursos mais vendidos']

opcao_selecionada = st.sidebar.selectbox('Escolha uma opção', opcoes)

def processar_opcao_selecionada(opcao):
    if opcao == 'Vendas':
        st.subheader('Vendas')
        receitas = df['Quantidade de Vendas'] * df['Preço Unitário']
        receita_total = format(receitas.sum(), '.2f') # receitas.sum()
        st.write('Receita total:', receita_total)

    elif opcao == 'Cursos mais vendidos':
        st.subheader('Cursos mais vendidos')
        mais_vendidos = df.groupby('Nome do Curso')['Quantidade de Vendas'].sum().idxmax()
        st.write(f'O curso mais vendido foi: {mais_vendidos}')
        st.write(f'Vendeu {df[df["Nome do Curso"] == mais_vendidos]["Quantidade de Vendas"].sum()} vezes')

    elif opcao == 'Home':
        st.subheader('Home')
        top_cursos = df.groupby('Nome do Curso')['Quantidade de Vendas'].sum().nlargest(5)
        st.bar_chart(top_cursos)

    else:
        pass

processar_opcao_selecionada(opcao_selecionada)