import streamlit as st
import pandas as pd
import os

def show_benchmarks():
    st.header("Benchmarks IA (Qwen, Mistral, Mock)")
    csv_path = "benchmark_results.csv"
    if not os.path.exists(csv_path):
        st.warning("Aucun benchmark_results.csv trouvé. Lancez le script de benchmark pour générer les résultats.")
        return
    df = pd.read_csv(csv_path)
    st.dataframe(df)
    # Filtres
    model = st.selectbox("Filtrer par modèle", ["Tous"] + sorted(df["model"].unique()))
    if model != "Tous":
        df = df[df["model"] == model]
    # Graphiques
    st.subheader("Temps de réponse par prompt")
    st.bar_chart(df.groupby("prompt")["duration_s"].mean())
    st.subheader("Score qualité par modèle")
    st.bar_chart(df.groupby("model")["quality"].mean())
    st.subheader("Mémoire consommée par modèle")
    st.bar_chart(df.groupby("model")["mem_peak_kb"].mean())
    st.info("Export complet disponible dans benchmark_results.csv et benchmark_results.md")

def main():
    st.sidebar.title("Athalia/Arkalia Dashboard")
    page = st.sidebar.radio("Navigation", ["Vue d'ensemble", "Benchmarks", "Logs", "Feedback"])
    if page == "Benchmarks":
        show_benchmarks()
    # ... autres onglets ...

if __name__ == "__main__":
    main() 