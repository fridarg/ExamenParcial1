#Frida Rangel
#A01651385
#Problema 2

#Importar librerias

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

#Cargar datos de la tabla de excel
archivo_excel = 'Estadística de Tallas (CS4015_P2023) (Respuestas).xlsx'
df = pd.read_excel(archivo_excel, engine='openpyxl')

# Calcular medidas de tendencia central (media y desviación estándar)
media_estatura = df['estatura'].mean()
std_estatura = df['estatura'].std()
media_calzado = df['calzado'].mean()
std_calzado = df['calzado'].std()

print(f"Media de estatura: {media_estatura}, desviación estándar: {std_estatura}")
print(f"Media de talla de calzado: {media_calzado}, desviación estándar: {std_calzado}")

# Graficar histogramas y funciones gaussianas
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

sns.histplot(df['estatura'], kde=True, ax=axs[0])
axs[0].set_title('Histograma de estaturas y función gaussiana')

sns.histplot(df['calzado'], kde=True, ax=axs[1])
axs[1].set_title('Histograma de tallas de calzado y función gaussiana')

plt.show()

# Calcular probabilidad dentro de la primera desviación estándar
prob_estatura = norm.cdf(1) - norm.cdf(-1)
prob_calzado = norm.cdf(1) - norm.cdf(-1)

print(f"Probabilidad de estatura dentro de la primera desviación estándar: {prob_estatura:.2%}")
print(f"Probabilidad de talla de calzado dentro de la primera desviación estándar: {prob_calzado:.2%}")

# Aproximación lineal entre estatura y talla de calzado
X = df[['estatura']]
y = df['calzado']

reg = LinearRegression()
reg.fit(X, y)

print(f"Relación lineal entre estatura y talla de calzado: calzado = {reg.intercept_:.2f} + {reg.coef_[0]:.2f} * 'estatura'")

# Graficar la relación lineal entre estatura y talla de calzado
plt.scatter(X, y, label='Datos')
plt.plot(X, reg.predict(X), color='red', label='Regresión lineal')
plt.xlabel('Estatura')
plt.ylabel('Talla de calzado')
plt.legend()
plt.title('Regresión lineal entre estatura y talla de calzado')
plt.show()

# Aproximación lineal por subgrupos divididos por sexo
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='estatura', y='calzado', hue='sexo', palette='deep')
plt.xlabel('Estatura')
plt.ylabel('Talla de calzado')
plt.title('Regresión lineal entre estatura y talla de calzado por sexo')

for sexo in df['sexo'].unique():
    df_sexo = df[df['sexo'] == sexo]
    
    X_sexo = df_sexo[['estatura']]
    y_sexo = df_sexo['calzado']
    
    reg_sexo = LinearRegression()
    reg_sexo.fit(X_sexo, y_sexo)
    
    print(f"Relación lineal entre estatura y talla de calzado para {sexo}: calzado = {reg_sexo.intercept_:.2f} + {reg_sexo.coef_[0]:.2f} * la estatura de cada persona")
    
    plt.plot(X_sexo, reg_sexo.predict(X_sexo), label=f'Regresión lineal para {sexo}')

plt.legend()
plt.show()
