"""
Projeto simples: Estatísticas e Gráficos sobre Doenças no Brasil (2021)
Baseado em arquivos locais de causas de morte para homens e mulheres.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Defina os caminhos corretos dos seus arquivos CSV
WOMEN_CSV = r"c:/Users/Administrador/OneDrive/Área de Trabalho/Top 10 - Doenças - Óbitos por 100k, Brasil, 2021/data/Mulheres.csv"
MEN_CSV   = r"c:/Users/Administrador/OneDrive/Área de Trabalho/Top 10 - Doenças - Óbitos por 100k, Brasil, 2021/data/Homens.csv"

# Função simples para carregar

def load_csv(path):
    df = pd.read_csv(path)
    df.columns = [c.lower() for c in df.columns]
    dcol = [c for c in df.columns if 'doen' in c or 'caus' in c or 'disease' in c][0]
    ncol = [c for c in df.columns if df[c].dtype != 'O'][0]
    return df[[dcol, ncol]].rename(columns={dcol:'disease', ncol:'rate'})

women = load_csv(WOMEN_CSV).groupby('disease')['rate'].mean().sort_values(ascending=False).head(10)
men   = load_csv(MEN_CSV).groupby('disease')['rate'].mean().sort_values(ascending=False).head(10)

# Mostrar estatísticas
print("Top 10 Mulheres:\n", women)
print("\nTop 10 Homens:\n", men)

# Gráficos
fig, axes = plt.subplots(1,2, figsize=(12,6))
women[::-1].plot.barh(ax=axes[0], title='Mulheres (2021)')
men[::-1].plot.barh(ax=axes[1], title='Homens (2021)')
plt.tight_layout()
plt.show()
