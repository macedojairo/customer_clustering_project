import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.utils.validation import check_array

from matplotlib.colors import ListedColormap
import seaborn as sns
import os

# Cor solicitada
rgb_color = (162/255, 37/255, 56/255)

def graficos_elbow_silhouette(
    X,                         # array-like (n_amostras x n_features): dados numéricos para o K-means
    intervalo_k=(2, 11),       # tupla ou range com os Ks a testar; (2,11) => testa K=2..10
    random_state=42,           # semente para reprodutibilidade (KMeans e amostragem do silhouette)
    padronizar=True,           # se True, aplica StandardScaler antes do KMeans (recomendado)
    sample_silhouette=10000,   # nº máx. de observações para calcular silhouette; None usa todas
    max_iter=300,              # nº máximo de iterações do KMeans por execução
    n_init="auto",             # nº de inicializações do KMeans; use 10 se sklearn<1.4
    return_metrics=True,       # se True, retorna DataFrame com métricas e o best_k
):
    if isinstance(intervalo_k, tuple):
        k_values = range(intervalo_k[0], intervalo_k[1])
    else:
        k_values = intervalo_k

    X_arr = check_array(X.values if hasattr(X, "values") else np.asarray(X),
                        ensure_2d=True, dtype=np.float64)

    X_proc = StandardScaler().fit_transform(X_arr) if padronizar else X_arr

    inertias, silhouettes, calinski, davies = [], [], [], []
    for k in k_values:
        if k < 2 or X_proc.shape[0] <= k:
            inertias.append(np.nan); silhouettes.append(np.nan)
            calinski.append(np.nan); davies.append(np.nan)
            continue

        km = KMeans(n_clusters=k, init="k-means++", n_init=n_init,
                    max_iter=max_iter, random_state=random_state)
        labels = km.fit_predict(X_proc)

        inertias.append(km.inertia_)
        try:
            silhouettes.append(
                silhouette_score(
                    X_proc, labels,
                    sample_size=sample_silhouette if (sample_silhouette and X_proc.shape[0] > sample_silhouette) else None,
                    random_state=random_state
                )
            )
        except Exception:
            silhouettes.append(np.nan)

        try:
            calinski.append(calinski_harabasz_score(X_proc, labels))
        except Exception:
            calinski.append(np.nan)

        try:
            davies.append(davies_bouldin_score(X_proc, labels))
        except Exception:
            davies.append(np.nan)

    # ----- GRÁFICOS (sem grid e com cor rgb_color) -----
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))

    # Elbow / SSE
    axs[0].plot(list(k_values), inertias, marker="o", color=rgb_color)
    axs[0].set_title("Elbow (SSE / Inertia)")
    axs[0].set_xlabel("K")
    axs[0].set_ylabel("SSE (Inertia)")

    # Silhouette
    axs[1].plot(list(k_values), silhouettes, marker="o", color=rgb_color)
    axs[1].set_title("Silhouette médio")
    axs[1].set_xlabel("K")
    axs[1].set_ylabel("Silhouette")

    plt.tight_layout()
    plt.show()

    if return_metrics:
        metrics = pd.DataFrame({
            "K": list(k_values),
            "inertia": inertias,
            "silhouette": silhouettes,
            "calinski_harabasz": calinski,
            "davies_bouldin": davies
        })
        return metrics


###################################
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D

def visualizar_clusters(
    dataframe,
    colunas,
    quantidade_cores,
    centroids,
    mostrar_centroids=True,
    mostrar_pontos=False,
    coluna_clusters=None,
    salvar_em=None  # <- novo argumento opcional
):
    """Gerar gráfico 3D com os clusters.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Dataframe com os dados.
    colunas : List[str]
        Lista com o nome das colunas (strings) a serem utilizadas.
    quantidade_cores : int
        Número de cores para o gráfico.
    centroids : np.ndarray
        Array com os centroides.
    mostrar_centroids : bool, opcional
        Se o gráfico irá mostrar os centroides ou não, por padrão True
    mostrar_pontos : bool, opcional
        Se o gráfico irá mostrar os pontos ou não, por padrão False
    coluna_clusters : List[int], opcional
        Coluna com os números dos clusters para colorir os pontos
        (caso mostrar_pontos seja True), por padrão None
    salvar_em : str, opcional
        Caminho para salvar o gráfico, por exemplo: "../Reports/Images/fig.png"
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    cores = plt.cm.tab10.colors[:quantidade_cores]
    cores = ListedColormap(cores)

    x = dataframe[colunas[0]]
    y = dataframe[colunas[1]]
    z = dataframe[colunas[2]]

    for i, centroid in enumerate(centroids):
        if mostrar_centroids:
            ax.scatter(*centroid, s=500, alpha=0.5)
            ax.text(
                *centroid,
                f"{i}",
                fontsize=20,
                horizontalalignment="center",
                verticalalignment="center",
            )

    if mostrar_pontos:
        s = ax.scatter(x, y, z, c=coluna_clusters, cmap=cores)
        ax.legend(*s.legend_elements(), bbox_to_anchor=(1.3, 1))

    ax.set_xlabel(colunas[0])
    ax.set_ylabel(colunas[1])
    ax.set_zlabel(colunas[2])
    ax.set_title("Clusters")

    # Salva se o caminho for fornecido
    if salvar_em:
        plt.savefig(salvar_em, dpi=300, bbox_inches="tight")
    
    plt.show()

