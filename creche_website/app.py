# Importa a biblioteca do Streamlit
import streamlit as st

# O nome do arquivo HTML que você precisa salvar
html_file_path = "creche_page.html"

# Tenta abrir e ler o arquivo HTML
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Usa o componente st.components.v1.html para renderizar o HTML
    st.components.v1.html(html_content, height=800, scrolling=True)

except FileNotFoundError:
    st.error(f"Erro: O arquivo '{html_file_path}' não foi encontrado. "
             "Por favor, salve o código HTML gerado em um arquivo com este nome.")
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar a página: {e}")
