import streamlit as st
import google.generativeai as genai

# Configura a API key do Gemini corretamente para a versão instalada
genai.configure(api_key="AIzaSyBEIW_iJvfvnYqZVM903imQ_J45bFbpyjk")

model = genai.GenerativeModel("gemini-2.0-flash")

# Função para gerar o início da história
def gerar_historia(nome_protagonista, genero, local_inicial, frase_desafio):
    try:
        # Criar o prompt com base nas entradas do usuário
        prompt = (f"Crie o início de uma história de '{genero}' com o protagonista chamado '{nome_protagonista}'. "
                  f"A história começa em '{local_inicial}'. Incorpore a seguinte frase ou desafio no início: '{frase_desafio}'.")

        # Gerar conteúdo utilizando o modelo Gemini
        response = model.generate_content(prompt)
        
        # Retorna o texto gerado pela IA
        return response.text
    except Exception as e:
        return f"Erro ao gerar história: {str(e)}"

# Interface para o usuário
st.title("Criador de Histórias Interativas com IA 📚")

# 1. Nome para o protagonista
nome_protagonista = st.text_input("Nome para o Protagonista:")

# 2. Gênero Literário
genero = st.selectbox("Escolha o Gênero Literário:", ["Fantasia", "Ficção Científica", "Mistério", "Aventura"])

# 3. Local Inicial
local_inicial = st.radio("Escolha o Local Inicial da História:", 
                         ["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado", "Uma nave espacial à deriva"])

# 4. Frase de Efeito ou Desafio Inicial
frase_desafio = st.text_area("Adicione uma Frase de Efeito ou Desafio Inicial:")

# 5. Botão "Gerar Início da História"
if st.button("Gerar Início da História"):
    if nome_protagonista and frase_desafio:
        with st.spinner("Gerando história..."):
            historia_gerada = gerar_historia(nome_protagonista, genero, local_inicial, frase_desafio)
            st.subheader("História Gerada:")
            st.write(historia_gerada)
    else:
        st.warning("Por favor, preencha todos os campos antes de gerar a história.")
