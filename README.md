# Análise de Dados e Modelagem Preditiva no Varejo (Walmart Dataset) 📊✨

Este repositório contém uma exploração de quatro algoritmos fundamentais de Machine Learning (Aprendizado de Máquina) aplicados a um dataset de vendas do Walmart. O objetivo é demonstrar a implementação e as aplicações práticas de cada algoritmo em cenários de dados de varejo.

## Dataset 📁

O dataset utilizado (`Walmart.csv`) contém informações sobre transações de vendas, incluindo detalhes como preço unitário, quantidade, margem de lucro, categoria do produto, método de pagamento, filial e avaliações de clientes.

## Algoritmos Implementados 🚀

Cada algoritmo está em um notebook Jupyter (`.ipynb`) separado, com o código completo para carregamento de dados, pré-processamento, treinamento e avaliação.

### 1. K-Means (Aprendizado Não Supervisionado) 🔍

* **Objetivo:** Agrupar transações de vendas em clusters (segmentos) com base em suas características numéricas.
* **Aplicação:** Identificar perfis de compra distintos, segmentar clientes ou tipos de transações para estratégias de marketing e operações mais direcionadas.
* **Features Utilizadas:** `unit_price`, `quantity`, `rating`, `profit_margin`.
* **Notebook:** `Kmeans.ipynb` 

### 2. K-Nearest Neighbors (KNN) (Aprendizado Supervisionado - Classificação) 🤝

* **Objetivo:** Classificar transações para prever se elas receberão uma "Alta Avaliação" (`rating >= 7`) ou "Baixa Avaliação" (`rating < 7`).
* **Aplicação:** Identificar transações com potencial de insatisfação (Baixa Avaliação) ou entender o que leva a Altas Avaliações para replicar o sucesso.
* **Features Utilizadas:** `unit_price`, `quantity`, `profit_margin`, `category`, `payment_method`, `Branch`.
* **Variável Alvo (`y`):** `High_Rating` (binária).
* **Notebook:** `KNN.ipynb`

### 3. Árvore de Decisão (Aprendizado Supervisionado - Classificação) 🌳

* **Objetivo:** Construir um modelo de decisão em forma de árvore para prever se uma transação resultará em "Alta Avaliação" ou "Baixa Avaliação".
* **Aplicação:** Similar ao KNN na previsão, mas com a vantagem adicional de oferecer um modelo **interpretável** que mostra as regras de decisão que levaram a uma determinada previsão. Ideal para entender os fatores que mais influenciam as avaliações.
* **Features Utilizadas:** `unit_price`, `quantity`, `profit_margin`, `category`, `payment_method`, `Branch`.
* **Variável Alvo (`y`):** `High_Rating` (binária).
* **Notebook:** `arvore.ipynb` (Nome sugerido para seu arquivo Jupyter)

### 4. Redes Neurais (Perceptron Multicamadas - MLP) (Aprendizado Supervisionado - Classificação) 🧠

* **Objetivo:** Utilizar uma arquitetura de rede neural para prever a "Alta Avaliação" ou "Baixa Avaliação" de uma transação.
* **Aplicação:** Abordar problemas de classificação complexos, onde as relações entre os dados podem ser não lineares e difíceis de serem capturadas por modelos mais simples. Redes Neurais são conhecidas por sua alta performance em diversas tarefas.
* **Features Utilizadas:** `unit_price`, `quantity`, `profit_margin`, `category`, `payment_method`, `Branch`.
* **Variável Alvo (`y`):** `High_Rating` (binária).
* **Notebook:** `Redes_Neurais.ipynb`

## Como Rodar os Códigos ⚙️

1.  Clone este repositório para sua máquina local.
2.  Certifique-se de ter o Python instalado (versão 3.x recomendada).
3.  Instale as bibliotecas necessárias usando `pip`, pra facilitar utilize o comando:
    ```bash
    pip install -r requirements.txt 
    ```
    Obs: as libs necessárias são: pandas scikit-learn matplotlib seaborn jupyter

5.  O codigo dataset_download.py deve colocar o arquivo `Walmart.csv` na pasta data para os codigos funcionarem.
6.  Abra cada notebook Jupyter (`.ipynb`) em seu ambiente Jupyter e execute as células sequencialmente.

## Autor(s) 👤

[Rael]
