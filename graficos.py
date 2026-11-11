import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.title('Dashboard de Estadísticas de Jugadores.')
st.write(
    'Visualización interactiva con Streamlit, Matplotlib y Seaborn usando el dataset seleccionado.'
)


@st.cache_data
def load_data():
  return pd.read_csv('fc27-players-2026-10-11.csv')


df = load_data()

# Selector en barra lateral para elegir el gráfico
option = st.sidebar.selectbox(
    'Selecciona el gráfico a mostrar:',
    (
        '1. Top 10 Nacionalidades (Barras)',
        '2. Pie Favorito (Tarta)',
        '3. Ritmo por Posición (Box Plot)',
        '4. Aceleración vs Regate (Scatter)',
        '5. Mapa de Calor de Correlaciones',
    ),
)

if option == '1. Top 10 Nacionalidades (Barras)':
  st.subheader('Gráfico de Barras: Top 10 Nacionalidades')
  fig, ax = plt.subplots(figsize=(10, 5))
  top_nations = df['nation_name'].value_counts().head(10)
  sns.barplot(
      x=top_nations.index,
      y=top_nations.values,
      palette='viridis',
      ax=ax,
      hue=top_nations.index,
      legend=False,
  )
  plt.xlabel("Nacionalidad")
  plt.ylabel("Cantidad de Jugadores")
  st.pyplot(fig)

elif option == '2. Pie Favorito (Tarta)':
  st.subheader('Gráfico de Tarta: Proporción por Pie Favorito')
  fig, ax = plt.subplots(figsize=(6, 6))
  foot_counts = df['foot'].value_counts()
  ax.pie(
      foot_counts,
      labels=foot_counts.index,
      autopct='%1.1f%%',
      colors=['#ff9999', '#66b3ff'],
      startangle=140,
  )
  st.pyplot(fig)

elif option == '3. Ritmo por Posición (Box Plot)':
  st.subheader('Diagrama de Caja: Ritmo por Posición')
  fig, ax = plt.subplots(figsize=(10, 5))
  top_positions = df['position'].value_counts().head(8).index
  df_filtered_pos = df[df['position'].isin(top_positions)]
  sns.boxplot(
      data=df_filtered_pos,
      x='position',
      y='pac',
      palette='Set2',
      ax=ax,
      hue='position',
      legend=False,
  )
  st.pyplot(fig)
  plt.xlabel("Posición")
  plt.ylabel("Ritmo")

elif option == '4. Aceleración vs Regate (Scatter)':
  st.subheader('Gráfico de Dispersión: Aceleración vs Regate')
  fig, ax = plt.subplots(figsize=(10, 5))
  sns.scatterplot(
      data=df,
      x='aceleration',
      y='drib',
      alpha=0.5,
      color='purple',
      ax=ax,
      edgecolor=None,
  )
  plt.xlabel("Aceleración")
  plt.ylabel("Regate")
  st.pyplot(fig)

elif option == '5. Mapa de Calor de Correlaciones':
  st.subheader('Mapa de Calor: Matriz de Correlación')
  fig, ax = plt.subplots(figsize=(8, 6))
  cols_to_corr = [
      'rating',
      'acceleration',
      'agility',
      'balance',
      'dribbling',
      'pac',
      'dri',
      'phy',
  ]
  corr_matrix = df[cols_to_corr].corr()
  sns.heatmap(
      corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax, linewidths=0.5
  )
  st.pyplot(fig)
