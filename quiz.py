import streamlit as st
st.title("Bem-vindo ao Quiz! :smile: ")
st.write("Por favor, escolha uma dificuldade: ")
st.write("1 - Fácil")
st.write("2 - Médio")
st.write("3 - Difícil")

#? comentario foda
x = "Você acertou! Parabéns!"
y = "Você errou! Tente novamente"
escolha = st.text_input('1 / 2 / 3')
z = "Digite sua resposta aqui: "

if 'pergunta_atual' not in st.session_state:
    st.session_state.pergunta_atual = 1

st.write(escolha)
    
#? ----------------------------------------------------------------------------------

if escolha == '1':
    st.write("Você escolheu o nível fácil!")
    if st.session_state.pergunta_atual == 1:
        st.write("Primeira pergunta: Qual a capital da Alemanha?")
        resposta_usuario = st.text_input(z)
    
        if resposta_usuario:
            if resposta_usuario.lower() == "berlim":
                st.write(x)
                st.session_state.pergunta_atual += 1
            else:
                st.write(y)
    
    if st.session_state.pergunta_atual == 2:
        st.write("Próxima pergunta!")
        st.write("Segunda pergunta: Qual o símbolo do elemento ferro?")
        resposta_usuario = st.text_input(z, key ="pergunta2")
        
        if resposta_usuario:
            if resposta_usuario.lower() == "fe":
                st.write(x)
                st.session_state.pergunta_atual += 1
            else:
                st.write(y) 
    
    if st.session_state.pergunta_atual == 3:
        st.write("Próxima pergunta!")
        st.write("Terceira pergunta: Qual animal é considerado o 'Rei da selva?' ")
        resposta_usuario = st.text_input(z, key="pergunta3") 

        if resposta_usuario:
            if resposta_usuario.lower() in ["leão", "leao"]:                           
                st.write(x)
                st.write("Você completou o quiz! Tente nas outras dificuldades!")
                st.session_state.pergunta_atual += 1
            else: 
                st.write(y)
         
#? ----------------------------------------------------------------------------------

if escolha == '2':
    st.write("Você escolheu o nível médio!")
    if st.session_state.pergunta_atual == 1: 
        st.write("Primeira pergunta: Em que ano ocorreu o atentado terrorista as Torres Gemêas?")
        resposta_usuario2 = st.text_input(z) 

        if resposta_usuario2:
            if resposta_usuario2.lower() == "2001":
                st.write(x)
                st.session_state.pergunta_atual += 1
            else:
                st.write(y)

    if st.session_state.pergunta_atual == 2:
        st.write("Próxima pergunta!")
        st.write("Segunda pergunta: Quantos ossos possue um ser humano adulto?")
        resposta_usuario2 = st.text_input(z, key="pergunta2")

        if resposta_usuario2:
            if resposta_usuario2.lower() == "206":
                st.write(x)
                st.session_state.pergunta_atual += 1
            else: 
                st.write(y)
    
    if st.session_state.pergunta_atual == 3:
        st.write("Próxima pergunta!")
        st.write("Terceira pergunta: Quem escreveu o livro 'Dom quixote'?")
        resposta_usuario2 = st.text_input(z, key="pergunta3")

        if resposta_usuario2:
            if resposta_usuario2.lower() == "miguel de cervantes":
                st.write(x)
                st.write("Você completou o quiz! Tente nas outras dificuldades!")
                st.session_state.pergunta_atual += 1
            else: 
                st.write(y)

#? ----------------------------------------------------------------------------------

if escolha == '3':
    st.write("Você escolheu o nível dificíl!")
    if st.session_state.pergunta_atual == 1:
        st.write("Primeira pergunta: Quantos presidentes da republica o Brasil já teve?")
        resposta_usuario3 = st.text_input(z)

        if resposta_usuario3:
            if resposta_usuario3.lower() == "39":
                st.write(x)
                st.session_state.pergunta_atual += 1
            else: 
                st.write(y)
    
    if st.session_state.pergunta_atual == 2:
        st.write("Próxima pergunta!")
        st.write("Segunda pergunta: Qual foi o filosófo conhecido como 'O Cínico'?")    
        resposta_usuario3 = st.text_input(z, key="pergunta2")
        
        if resposta_usuario3:
            if resposta_usuario3.lower() in ["diógenes", "diogenes"]:
                st.write(x)
                st.session_state.pergunta_atual += 1
            else:
                st.write(y)
    
    if st.session_state.pergunta_atual == 3:
        st.write("Próxima pergunta!")
        st.write("Quem foi a primeira mulher a ganhar um prêmio Nobel?")
        resposta_usuario3 = st.text_input(z, key="pergunta3")

        if resposta_usuario3:
            if resposta_usuario3.lower() == "marie curie":
                st.write(x)
                st.write("Você completou o quiz! Tente nas outras dificuldades!")
                st.session_state.pergunta_atual += 1 
            else: 
                st.write(y)
        
        
