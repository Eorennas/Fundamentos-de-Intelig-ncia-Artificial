import streamlit as st
import google.generativeai as genai

# Configura a API key do Gemini corretamente
genai.configure(api_key="AIzaSyBEIW_iJvfvnYqZVM903imQ_J45bFbpyjk")

# Função para gerar receita usando a IA
def gerar_receita(ingredientes, tipo_culinaria, nivel_dificuldade, restricao_str):
    try:
        # Criar o prompt com base nas entradas do usuário
        prompt = (f"Sugira uma receita {tipo_culinaria} com nível de dificuldade {nivel_dificuldade} "
                  f"(sendo 1 muito fácil e 5 desafiador). Deve usar principalmente os seguintes ingredientes: '{ingredientes}'. "
                  f"{restricao_str} Apresente o nome da receita, uma lista de ingredientes adicionais se necessário, e um breve passo a passo.")
        
        # Gerar conteúdo utilizando o modelo Gemini
        response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
        
        # Retorna o texto gerado pela IA
        return response.text
    except Exception as e:
        return f"Erro ao gerar receita: {str(e)}"

# Interface para o usuário
st.title("Gerador de Receitas Culinárias Personalizadas com IA 🧑‍🍳")

# 1. Ingredientes Principais
ingredientes = st.text_area("Quais ingredientes você possui? (Exemplo: 'frango, tomate, cebola, arroz')", "")

# 2. Tipo de Culinária
tipo_culinaria = st.selectbox("Escolha o Tipo de Culinária:", ["Italiana", "Brasileira", "Asiática", "Mexicana", "Qualquer uma"])

# 3. Nível de Dificuldade
nivel_dificuldade = st.slider("Escolha o Nível de Dificuldade", 1, 5, 1)

# 4. Restrição Alimentar
restricao_checkbox = st.checkbox("Possui Restrição Alimentar?")
restricao_str = ""
if restricao_checkbox:
    restricao_str = st.text_input("Digite a sua restrição alimentar (Ex: 'sem glúten', 'vegetariana', 'sem lactose')", "")

# 5. Botão "Sugerir Receita"
if st.button("Sugerir Receita"):
    if ingredientes:
        with st.spinner("Gerando receita..."):
            if restricao_str:
                restricao_str = f"Adicionalmente, a receita deve ser {restricao_str}."
            else:
                restricao_str = ""
            
            receita_gerada = gerar_receita(ingredientes, tipo_culinaria, nivel_dificuldade, restricao_str)
            st.subheader("Receita Gerada:")
            st.write(receita_gerada)
    else:
        st.warning("Por favor, insira os ingredientes antes de gerar a receita.")
