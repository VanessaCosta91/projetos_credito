import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("pipeline_credito/data/raw/creditcard.csv")

print("Linhas iniciais do dataset\n", df.head().to_string())

print("\nFormato do dataset: ", df.columns)

print("\nFormato do dataset: ", df.shape)

print("\nInformações gerais:")
print(df.info())

print("\nEstatísticas básicas: \n", df.describe())

print("\nQuantidade de valores unicos por colunas: \n", df.nunique())

print("\nQuantidade e nulos por colunas: \n", df.isnull().sum())

# Histograma da coluna Amount
plt.figure(figsize=(10,6))
plt.hist(df["Amount"], bins=50)
plt.title("Distribuição original do Amount")
plt.show()

plt.figure(figsize=(10,6))
plt.hist(np.log1p(df["Amount"]), bins=50)
plt.title("Distribuição do Amount com log1p")
plt.show()

# Verificar outliers
plt.boxplot(df["Amount"])
plt.title("Boxplot Original - coluna Amount")
plt.show()

plt.boxplot(np.log1p(df["Amount"]))
plt.title("Boxplot Original - coluna Amount")
plt.show()



