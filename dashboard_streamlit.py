import streamlit as st
from retartext import *

st.write('''# Retartext
Have you ever felt like your texts aren't retarded enough?\n
Well, here is your solution.''')

text= st.text_input('Enter the text:')

if st.button('Eliminate intellegence'):
	st.write(add_emoji(text))
