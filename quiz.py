import streamlit as st
st.title("Bem-vindo ao Quiz! :smile: ")
st.write("Por favor, escolha uma dificuldade: ")
st.write("1 - Fácil")
st.write("2 - Médio")
st.write("3 - Difícil")

#variaveis
x = "Você acertou! Parabéns!"
y = "Você errou! Tente novamente"
escolha = st.text_input('1 / 2 / 3')

st.write(escolha)
if escolha == '1':
    st.write("Você escolheu o nível fácil!")
    st.write("Primeira pergunta: Qual a capital da Alemanha?")
    resposta_usuario = st.text_input("Digite sua resposta aqui: ")
    
    if resposta_usuario:
        if resposta_usuario.lower() == "berlim":
            st.write(x)
        else:
            st.write(y)

if escolha == '2':
    st.write("Você escolheu o nível médio!")
    st.write("Primeira pergunta: Em que ano ocorreu o atentado terrorista as Torres Gemêas?")
    resposta_usuario2 = st.text_input("Digite sua resposta aqui: ")

    if resposta_usuario2:
        if resposta_usuario2.lower() == "2001":
            st.write(x)
        else:
            st.write(y)

if escolha == '3':
    st.write("Você escolheu o nível dificíl!")
    st.write("Primeira pergunta: Quantos presidentes da republica o Brasil já teve?")
    resposta_usuario3 = st.text_input("Digite sua resposta aqui: ")

    if resposta_usuario3:
        if resposta_usuario3.lower() == "39":
            st.write(x)
        else: st.write(y)
