import streamlit as st
from PIL import Image
import random

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="Trulimero Trulichina", page_icon="🤯", layout="centered")

# ---------------- TITULOS ---------------- #
st.title("🌌 Trulimero Trulichina 🚀")
st.markdown("""
### ✨ Por más que **Trulimero** esté bravo con *Bombini*  
😡 No parcha con **Tripi Tropi**...  
🥶 ¡Y mucho menos con **Frigo Camelo**!
""")

# ---------------- IMAGEN ---------------- #
image = Image.open("trulimero.png")
st.image(image, caption="🌀 El único, el inigualable: **Trulimero**", use_column_width=True)

# ---------------- OPINION ---------------- #
st.subheader("💭 ¿Qué opina el parcero?")
texto = st.text_input("Dígalo sin miedo:", "Texto")
st.success(f"👉 El parcero sabe que son: **{texto}**")

# ---------------- EMOCIONES ---------------- #
st.subheader("🔥 Estado actual de Trulimero")
estado = st.radio(
    "Seleccione cómo está el man hoy:",
    ["😡 Bravo", "😂 Feliz", "🤯 Trulichado", "🥶 Con Frigo Camelo", "👽 De otro planeta"]
)

if estado == "😡 Bravo":
    st.error("Ojo que está que estalla 💥")
elif estado == "😂 Feliz":
    st.balloons()
    st.success("El parcero anda parchado 😎")
elif estado == "🤯 Trulichado":
    st.warning("Demasiada información... demasiado poder 🌀")
elif estado == "🥶 Con Frigo Camelo":
    st.info("Brrrr... frío cósmico 🧊")
elif estado == "👽 De otro planeta":
    st.success("Contactando marcianos... 👾")

# ---------------- BOTON DE SORPRESA ---------------- #
if st.button("🎲 Truco Trulichi"):
    frases = [
        "El que no tru, no limero 🚀",
        "Bombini llorando en un rincón 😢",
        "Tripi Tropi en otra dimensión 🌌",
        "Frigo Camelo no aguanta este frío 🧊",
        "La trulichi energía es infinita ♾️"
    ]
    st.markdown(f"✨ **{random.choice(frases)}**")

# ---------------- LIKE COUNTER ---------------- #
if "likes" not in st.session_state:
    st.session_state.likes = 0

if st.button("❤️ Darle amor a Trulimero"):
    st.session_state.likes += 1

st.metric(label="Likes de Trulimero", value=st.session_state.likes)
