<<<<<<< HEAD
# Trilha Inicial 
## Código Certo 

Este projeto foi desenvolvido por Ícaro Santos como parte da trilha inicial de Ciência de Dados.
As tecnologias usadas foram:
`-> Python,`
`-> Pandas,`
`-> Matplotlib,`
`-> Seaborn,`
`-> Streamlit,`

## Sobre o projeto 

Para rodar o projeto, crie um ambiente virtual e rode o comando para instalar as dependências necessárias: 

```bash
pip install -r requirements.txt 

```

Para rodar a aplicação Streamlit, basta digitar o comando: 

```bash
streamlit run streamlit.py
```

### Requisitos Funcionais 
Foram apresentados os seguintes requisitos funcionais: 

`-> Carregamento de dados:` Para essa tarefa, foi utilizada a biblioteca Pandas´

```python
# Importar arquivo txt e exportar arquivo csv 
dados = pd.read_csv('dados.txt')
dados.to_csv('dados.csv', index=False)

# Importar arquivo csv 
df = pd.read_csv('dados.csv')
```

`-> Exploração de dados:` Para a exploração de dados também utilizei Pandas

```python
# Exploração de Dados
df.head() # Exibe as primeiras linhas
df.info()  # Informações básicas do conjunto de dados
```
`-> Estatísticas descritivas:`

```python
# Estatísticas Descritivas
df.describe()  # Estatísticas descritivas para colunas numéricas
```

`-> Visualização de dados:` Nessa parte foram utilizadas as bibliotecas Matplotlib e Seaborn tanto no arquivo analisys.py quanto nos arquivos streamlit.py e dash.py 
![alt text](image.png)
![alt text](image-1.png)

## Sobre os uso de Streamlit

Streamlit é um framework Python de código aberto desenvolvido para cientista de dados e engenheiros de IA/ML para construção de aplicações interativas.

Dentro do seu navegador, vai ser possível acessar a rota `http://localhost:8501/` onde a aplicação vai estar funcionando. 

![alt text](image-2.png)

Basta selecionar a opção que deseja ver na caixa de seleção que se encontra na barra lateral e poderá ter a mesma visualização de dados que é mostrada dentro do arquivo analisys.ipynb
=======
![Código Certo Coders](https://utfs.io/f/3b2340e8-5523-4aca-a549-0688fd07450e-j4edu.jfif)

# 📚 Trilha Inicial Ciência de Dados Jr
Este projeto tem como objetivo realizar uma análise básica de dados utilizando Python, explorando um conjunto de dados pré-definido para extrair insights simples através de estatísticas descritivas e visualizações gráficas.

## Requisitos Funcionais:
- Carregamento de Dados: Implementar a funcionalidade para carregar um conjunto de dados em formato CSV ou outro formato simples suportado pelo Python.
- Exploração de Dados: Exibir as primeiras linhas e informações básicas do conjunto de dados, como número de linhas, colunas e tipos de dados presentes.
- Estatísticas Descritivas: Calcular e exibir estatísticas descritivas básicas para colunas numéricas do conjunto de dados, como média, mediana, mínimo, máximo e desvio padrão.
- Visualização de Dados: Criar pelo menos dois tipos de gráficos utilizando bibliotecas como Matplotlib ou Seaborn, como gráfico de barras para contagem de categorias e gráfico de dispersão para relação entre variáveis.

   #### Análise de Dados: Vendas de Cursos Online
   ```plaintext
   ID,Nome do Curso,Quantidade de Vendas,Preço Unitário,Data
   1,Introdução à Programação em Python,50,39.90,2023-01-01
   2,Desenvolvimento Web com HTML e CSS,30,59.90,2023-01-02
   3,JavaScript Avançado: Frameworks e Bibliotecas,20,79.90,2023-01-03
   4,Introdução ao Machine Learning,15,99.90,2023-01-04
   5,Desenvolvimento Mobile com React Native,25,69.90,2023-01-05
   6,Arquitetura de Microserviços,12,89.90,2023-01-06
   7,Banco de Dados SQL e NoSQL,18,79.90,2023-01-07
   8,Segurança da Informação: Fundamentos,10,109.90,2023-01-08
   9,Cloud Computing com AWS,22,99.90,2023-01-09
   10,DevOps: Integração e Entrega Contínua,8,119.90,2023-01-10
   11,Desenvolvimento Web com HTML e CSS,20,59.90,2023-01-11
   12,JavaScript Avançado: Frameworks e Bibliotecas,15,79.90,2023-01-12
   13,Introdução ao Machine Learning,10,99.90,2023-01-13
   14,Desenvolvimento Mobile com React Native,18,69.90,2023-01-14
   15,Arquitetura de Microserviços,8,89.90,2023-01-15
   16,Banco de Dados SQL e NoSQL,12,79.90,2023-01-16
   17,Segurança da Informação: Fundamentos,5,109.90,2023-01-17
   18,Cloud Computing com AWS,15,99.90,2023-01-18
   19,DevOps: Integração e Entrega Contínua,6,119.90,2023-01-19
   20,Introdução à Programação em Python,45,39.90,2023-01-20
   21,Desenvolvimento Web com HTML e CSS,25,59.90,2023-01-21
   22,JavaScript Avançado: Frameworks e Bibliotecas,18,79.90,2023-01-22
   23,Introdução ao Machine Learning,12,99.90,2023-01-23
   24,Desenvolvimento Mobile com React Native,20,69.90,2023-01-24
   25,Arquitetura de Microserviços,10,89.90,2023-01-25
   ```
Utilize esses dados e transforme em arquivo .CSV, você vai utilizar para realizar a análise utilizando o Python com pandas e Matplotlib/Seaborn para visualização de dados.

- **ID:** Identificador único de cada curso vendido.
- **Nome do Curso:** Nome do curso vendido na plataforma.
- **Quantidade de Vendas:** Número de vendas realizadas para cada curso.
- **Preço Unitário:** Preço unitário do curso.
- **Data:** Data da venda do curso.

## Desafios Propostos:
   1. Calcular a receita total gerada pela venda dos cursos.
   2. Identificar o curso com o maior número de vendas.
   3. Visualizar a distribuição das vendas ao longo do tempo através de gráficos.

## Entregáveis:
   1. **Código Fonte:**
      - Código fonte do projeto, organizado conforme a estrutura acima.
   2. **Repositório GitHub:**
      - Repositório público contendo o código fonte e documentação.
   3. **Documentação:**
      - Documentação Simples: Breve documentação explicando o funcionamento do script e as conclusões básicas obtidas.

### Detalhes Técnicos: 🔧
- **Boas Práticas:** Utilizar boas práticas de código limpo, legível e bem documentado.
- **Git:** Utilizar Git para controle de versão e submeter o projeto através de um repositório público no GitHub.

### Dicas para Abordar o Projeto 🌟
- **Crie um Fork desse Repositório.**
- **Criar do Zero:** É fundamental que o projeto seja desenvolvido completamente do zero, demonstrando suas habilidades e criatividade desde o início.
- **Documente cada etapa do processo para facilitar a compreensão.**

### Critérios de Avaliação: 📝
- **Funcionalidade:** A aplicação atende aos requisitos funcionais e funciona corretamente?
- **Qualidade do Código:** O código é limpo, bem estruturado e adequadamente documentado?
- **Precisão dos Resultados:** As estatísticas descritivas e as visualizações de dados devem refletir com precisão as informações presentes no conjunto de dados utilizado?
- **Uso do Git:** O controle de versão é usado de forma eficaz com mensagens de commit significativas?

### Não Queremos 🚫
- Descobrir que o candidato não foi quem realizou o teste.
- Ver commits grandes sem muita explicação nas mensagens no repositório.
- Entregas padrão ou cópias de outros projetos. Buscamos originalidade e autenticidade em cada contribuição.

### Prazo ⏳
Os candidatos devem completar a trilha em no máximo em 2 semanas, começando a contar a partir de 15/06.

A conclusão da trilha inicial é um requisito obrigatório para avançar para a trilha 
final. Caso a trilha inicial não seja concluída dentro do prazo estabelecido, o 
candidato estará impossibilitado de prosseguir para trilha final.

**Data máxima para entrega: 29/06**

### **Configuração do Ambiente:**
1. **Instalar Python:** Certifique-se de ter o Python instalado em sua máquina.
2. **Instalar Jupyter Notebook:** Utilize o comando `pip install notebook` para instalar o Jupyter Notebook.
3. **Instalar Bibliotecas:** Utilize o comando `pip install pandas matplotlib seaborn scikit-learn` para instalar as bibliotecas necessárias.
4. **Criar Repositório no GitHub:** Crie um repositório público para o projeto.
5. **Clonar o Repositório:** Clone o repositório para a sua máquina local e configure o ambiente de trabalho.

### Instruções de Entrega: 📬
Após finalizar o projeto, em seu repositório do GitHub, você cria um arquivo README.md que descreve o projeto, explica como executar o código Python, e detalha as análises realizadas e os insights obtidos. Você pode incluir gráficos gerados pelo Matplotlib ou Seaborn e preencha o [Formulário](https://forms.gle/gZViPMTSDV5nidSu6):

---

### Desafio da Inovação 🚀
Achou esse projeto inicial simples? Eleve ainda mais! Estamos em busca de mentes inovadoras que não apenas criem, mas que também desafiem os padrões. Como você pode transformar essa estrutura inicial em algo verdadeiramente extraordinário? Demonstre o poder da sua criatividade e o impacto das suas ideias inovadoras!

---

🔗 **Mantenha-se Conectado:**
- [Discord](https://discord.gg/wzA9FGZHNv)
- [Website](http://www.codigocertocoders.com.br/)
- [LinkedIn](https://www.linkedin.com/company/codigocerto/)
  
🌐 **Contato:**
- Email: codigocertocoders@gmail.com

---

### Precisa de Ajuda?
Está com alguma dificuldade, encontrou algum problema no desafio ou tem alguma sugestão pra gente? Crie uma issue e descreva o que achar necessário.

**Construindo o amanhã, hoje.**
>>>>>>> ce7c21f201249d1c09152e1dcf9593e2570345ee
