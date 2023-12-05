import streamlit as st
import random

listaAnimais = ['CACHORRO', 'GATO', 'PAPAGAIO', 'PEIXE', 'COBRA', 'TARTARUGA', 'COELHO', 'HAMSTER', 'FURÃO', 'PORQUINHO DA ÍNDIA', 'CHINCHILA', 'PÁSSARO']
listaObjetos = ['CADEIRA', 'MESA', 'LIVRO', 'CANETA', 'CELULAR', 'TELEVISÃO', 'CARRO', 'BICICLETA', 'GELADEIRA', 'BOLA']

listaObejtosComC = ['CADEIRA', 'CANETA', 'CELULAR', 'CARRO', 'CAMA', 'CACHIMBO', 'COLHER', 'COMPUTADOR', 'CORTINA']

opcao = st.selectbox(
    'ESCOLHA UMA OPÇÃO',
    ('ANIMAIS', 'OBJETOS'),
    index=None,
   placeholder="")

numeroAleatorioAnimais = random.randint(0, len(listaAnimais)-1)
numeroAleatorioObjetos = random.randint(0, len(listaObjetos)-1)

st.markdown("----", unsafe_allow_html=True)
columns = st.columns((2, 1, 2))
# button_pressed = columns[1].button('Click Me!')
botao = columns[1].button('CLIQUE AQUI')
st.markdown("----", unsafe_allow_html=True)

if botao == False:
    st.write()
elif botao == True and opcao == 'ANIMAIS':
    st.markdown(f"<h1 style='text-align: center; color: red;'>{listaAnimais[numeroAleatorioAnimais]}</h1>", unsafe_allow_html=True)
else:
    st.markdown(f"<h1 style='text-align: center; color: red;'>{listaObjetos[numeroAleatorioObjetos]}</h1>", unsafe_allow_html=True)