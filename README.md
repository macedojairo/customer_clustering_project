
- **Data/**: contém o dataset original `Mall_Customers.csv` e demais arquivos gerados.
- **Reports/Images/**: imagens utilizadas no README e nos notebooks.
- **Models/**: pipelines e modelos salvos (.pkl).
- **Scripts/**: notebooks e scripts do projeto:
  - `code_0_initial_exploration.ipynb`: exploração inicial com histogramas e limpeza.
  - `code_1_no_pipeline_clustering.ipynb`: clusterização sem pré-processamento (didático).
  - `code_2_final_analysis.ipynb`: clusterização com pipeline + PCA.
  - `functions.py`: funções auxiliares reutilizadas nos notebooks.
  - `config.py`: arquivos de configuração com caminhos e constantes globais.
- **Reports/**: relatórios gerados com [ydata-profiling](https://github.com/ydataai/ydata-profiling).

---

## 🧾 Dataset Utilizado

O arquivo [`Mall_Customers.csv`](Data/raw/Mall_Customers.csv) contém os seguintes campos:

- `CustomerID`: identificador do cliente
- `Gender`: gênero
- `Age`: idade
- `Annual Income (k$)`: renda anual
- `Spending Score (1–100)`: pontuação de gastos (comportamento)

---

## 📊 Resultados da Segmentação

Após aplicar o pipeline com pré-processamento, PCA e K-Means, foram identificados 5 clusters distintos:

![pairplot](Images/clusters-visualizacao.png)
![boxplot](Images/clusters_visualizacao_gender.png)

| Cluster | Pontuação de Gastos | Renda    | Idade    |
| ------- | ------------------- | -------- | -------- |
| 0       | Moderada            | Moderada | Alta     |
| 1       | Moderada            | Moderada | Jovem    |
| 2       | Baixa               | Alta     | Moderada |
| 3       | Alta                | Baixa    | Jovem    |
| 4       | Alta                | Alta     | Jovem    |

---

## ▶️ Como Reproduzir o Projeto

O projeto foi desenvolvido em Python 3.11.4. Para reproduzi-lo:

1. Crie um ambiente virtual com Conda ou `venv`.
2. Instale as bibliotecas a seguir:

| Biblioteca       | Versão |
|------------------|--------|
| matplotlib       | 3.7.1  |
| numpy            | 1.24.3 |
| pandas           | 1.5.3  |
| scikit-learn     | 1.3.0  |
| seaborn          | 0.12.2 |
| ydata-profiling  | —      |
| ipympl (opcional)| —      |

> `ydata-profiling` é usada para gerar relatórios automáticos de EDA.  
> `ipympl` permite visualizações interativas em 3D nos notebooks.

---

Se quiser, posso gerar também o `requirements.txt` completo ou configurar um ambiente `conda.yml`. Deseja?


