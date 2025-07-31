# --------------------------------------------------------------------------------------
# Arquivo: app_streamlit.py
# Descrição: Aplicação web da creche criada com Streamlit.
# Para rodar, instale as dependências com `pip install -r requirements.txt`
# e depois execute no terminal: `streamlit run app_streamlit.py`
# --------------------------------------------------------------------------------------

import streamlit as st

# --- Configurações da Página ---
# Use o layout "wide" para aproveitar melhor o espaço horizontal.
st.set_page_config(
    page_title="Creche Vida de Criança",
    page_icon="👶",
    layout="wide"
)

# --- Dados de Exemplo ---
# Substitua estas informações e as URLs/arquivos de imagem pelos seus.
FOTOS_GALERIA = [
    {'url': 'https://placehold.co/600x400/E0F7FA/0056b3?text=Crian%C3%A7as+pintando',
        'legenda': 'Crianças pintando'},
    {'url': 'https://placehold.co/600x400/FFECB3/333333?text=Hora+da+hist%C3%B3ria',
        'legenda': 'Hora da história'},
    {'url': 'https://placehold.co/600x400/C8E6C9/1B5E20?text=Brincando+no+parquinho',
        'legenda': 'Brincando no parquinho'},
    {'url': 'https://placehold.co/600x400/E1BEE7/4A148C?text=Atividade+em+grupo',
        'legenda': 'Atividade em grupo'},
    {'url': 'https://placehold.co/600x400/B3E5FC/01579B?text=Comemora%C3%A7%C3%A3o+de+anivers%C3%A1rio',
        'legenda': 'Comemoração de aniversário'},
    {'url': 'https://placehold.co/600x400/FFCDD2/B71C1C?text=Lanche+da+manh%C3%A3',
        'legenda': 'Lanche da manhã'},
]

LOCALIZACAO_CRECHE = {
    "latitude": -9.9168923,
    "longitude": -63.9042211,
}

# --- Funções para cada página ---


def home_page():
    """Conteúdo da página inicial."""
    st.title("Bem-vindos à Creche Vida de Criança!")
    st.subheader(
        "Um lugar onde a felicidade e o aprendizado andam de mãos dadas.")
    st.image("https://placehold.co/1200x600/FFD54F/333333?text=Banner+da+Creche",
             use_column_width=True)

    st.markdown("---")

    st.header("Nossos Diferenciais")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**Equipe Qualificada**")
        st.write("Profissionais dedicados e com amor pela educação infantil.")
    with col2:
        st.markdown("**Ambiente Seguro**")
        st.write("Estrutura pensada para o bem-estar e a segurança dos pequenos.")
    with col3:
        st.markdown("**Atividades Lúdicas**")
        st.write("Brincadeiras que estimulam a criatividade e o desenvolvimento.")
    with col4:
        st.markdown("**Alimentação Saudável**")
        st.write("Cardápio nutritivo, elaborado por nutricionista.")


def sobre_page():
    """Conteúdo da página 'Sobre Nós'."""
    st.title("Sobre Nós")
    st.header("Nossa História e Missão")
    st.write(
        "A Creche Alegria foi fundada em [Ano de Fundação] com a missão de criar um espaço acolhedor e "
        "estimulante, onde cada criança possa se desenvolver de forma integral. Acreditamos que a infância "
        "é a fase mais importante da vida, e nosso objetivo é nutrir a curiosidade, a criatividade e o respeito mútuo."
    )
    st.write(
        "Nossa filosofia pedagógica é baseada em princípios de afeto e ludicidade, incentivando a aprendizagem "
        "através da exploração e da diversão."
    )

    st.markdown("---")

    st.header("Nossa Equipe")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Professoras")
        st.write("Equipe dedicada e qualificada para cuidar e educar.")
    with col2:
        st.subheader("Nutricionista")
        st.write("Cardápio balanceado e saudável para o crescimento.")
    with col3:
        st.subheader("Equipe de Apoio")
        st.write("A creche sempre limpa e organizada para as crianças.")


def galeria_page():
    """Conteúdo da página da galeria de fotos."""
    st.title("Galeria de Fotos")
    st.subheader("Momentos de Alegria e Aprendizado")
    st.write(
        "Confira alguns registros do nosso dia a dia e das atividades realizadas com muito carinho."
    )

    # Cria uma grade de 3 colunas para as fotos.
    cols = st.columns(3)
    for i, foto in enumerate(FOTOS_GALERIA):
        with cols[i % 3]:
            st.image(foto['url'], caption=foto['legenda'],
                     use_column_width=True)


def contato_page():
    """Conteúdo da página de contato."""
    st.title("Entre em Contato Conosco")
    st.subheader("Fale conosco e agende uma visita!")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Nossas Informações")
        st.markdown("**Endereço:** Rua das Crianças, 123 - Centro")
        st.markdown("**Cidade:** Ariquemes - RO")
        st.markdown("**Telefone:** (69) 1234-5678")
        st.markdown("**E-mail:** contato@crechealegria.com.br")
    with col2:
        st.header("Onde nos Encontrar")
        # Usa st.map para mostrar a localização no mapa.
        st.map(LOCALIZACAO_CRECHE, zoom=15)


# --- Lógica principal da aplicação ---
# Cria um menu de navegação na barra lateral.
st.sidebar.title("Navegação")
page = st.sidebar.radio(
    "Ir para:", ["Home", "Sobre Nós", "Galeria de Fotos", "Contato"])

# Chama a função da página selecionada.
if page == "Home":
    home_page()
elif page == "Sobre Nós":
    sobre_page()
elif page == "Galeria de Fotos":
    galeria_page()
elif page == "Contato":
    contato_page()
