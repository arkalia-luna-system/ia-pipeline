import streamlit as st
import pandas as pd
import os


def show_benchmarks():
    st.header("Benchmarks IA (Qwen, Mistral, Mock)")
    csv_path = "benchmark_results.csv"
    if not os.path.exists(csv_path):
        st.warning(
            "Aucun benchmark_results.csv trouvé. Lancez le script de benchmark "
            "pour générer les résultats."
        )
        return

    try:
        df = pd.read_csv(csv_path)
        st.dataframe(df)

        # Vérifier que df est bien un DataFrame
        if not isinstance(df, pd.DataFrame):
            st.error("Erreur: Les données ne sont pas dans le bon format")
            return

        # Vérifier les colonnes disponibles
        available_columns = df.columns.tolist()

        # Filtres
        if "model" in available_columns:
            model = st.selectbox(
                "Filtrer par modèle",
                ["Tous"] + sorted(df["model"].unique())
            )
            if model != "Tous":
                df = df[df["model"] == model]

        # Graphiques - seulement si les colonnes existent
        if "prompt" in available_columns and "duration_s" in available_columns:
            st.subheader("Temps de réponse par prompt")
            st.bar_chart(df.groupby("prompt")["duration_s"].mean())

        if "model" in available_columns and "quality" in available_columns:
            st.subheader("Score qualité par modèle")
            st.bar_chart(df.groupby("model")["quality"].mean())

        if "model" in available_columns and "mem_peak_kb" in available_columns:
            st.subheader("Mémoire consommée par modèle")
            st.bar_chart(df.groupby("model")["mem_peak_kb"].mean())

        st.info(
            "Export complet disponible dans benchmark_results.csv "
            "et benchmark_results.md"
        )

    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {e}")


def main():
    st.sidebar.title("Athalia/Arkalia Dashboard")
    page = st.sidebar.radio(
        "Navigation", ["Vue d'ensemble", "Benchmarks", "Logs", "Feedback"]
    )
    if page == "Benchmarks":
        show_benchmarks()
    # ... autres onglets ...


if __name__ == "__main__":
    main() 