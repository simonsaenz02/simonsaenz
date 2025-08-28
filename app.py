import streamlit as st
from PIL import Image

st.title("Trulimero Trulichina")

st.header("Por mas que Trulimero este bravo con Bombini no parcha con Tripi Tropi.")
st.write("Y si que menos con frigo camelo")
image= Image.open('trulimero.png')

st.image(image, caption='Trulimero')


texto= st.text_input('Que opina?', 'Texto')
st.write('El parcero sabe que son', texto)
