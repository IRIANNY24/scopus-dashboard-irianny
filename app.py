import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="FraudML Analytics", layout="wide")

st.title("🔎 FraudML Analytics")
st.write("Detección de Fraudes usando Machine Learning")

st.subheader("Pregunta de Investigación")
st.write("¿Cómo ayuda el Machine Learning a detectar fraudes en transacciones financieras?")

st.subheader("Keywords")
st.write("""
• Machine Learning
• Fraud Detection
• Financial Transactions
• Anomaly Detection
""")

st.subheader("Integrante")
st.write("Irianny Ardila")

archivo = st.file_uploader(
    "Sube tu archivo CSV de Scopus",
    type=["csv"]
)

if archivo is not None:

    df = pd.read_csv(archivo)

    st.subheader("Métricas Generales")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Artículos", len(df))
    col2.metric("Promedio Citas", round(df['Cited by'].mean(),2))
    col3.metric("Año Más Reciente", int(df['Year'].max()))

    st.subheader("Vista del Dataset")
    st.dataframe(df)

    st.subheader("Publicaciones por Año")

    publicaciones = df['Year'].value_counts().sort_index()

    fig, ax = plt.subplots()

    ax.bar(publicaciones.index, publicaciones.values)

    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad")

    st.pyplot(fig)

    st.subheader("Top 10 Artículos Más Citados")

    top10 = df.sort_values(
        by="Cited by",
        ascending=False
    ).head(10)

    st.dataframe(
        top10[["Title","Cited by"]]
    )

    st.subheader("Distribución de Citas")

    fig2, ax2 = plt.subplots()

    ax2.hist(df["Cited by"], bins=10)

    ax2.set_xlabel("Número de citas")
    ax2.set_ylabel("Frecuencia")

    st.pyplot(fig2)
