import streamlit as st

st.title('Hello, world!')

x = st.slider('Pick a number', 0, 10, 2)
st.write(f'You picked: {x}')
