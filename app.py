import streamlit as st

st.image("Python_logo.png")


st.title("Especializacion Python for Analytics")
st.sidebar.title("Parametros")
st.write ("Elaborado por: Julio Solis")

modulos = st.sidebar.selectbox("Seleccione un módulo",["Módulo Listas","Módulo Arreglo";"Módulo Funciones"])

if modulos == "Modulos Listas":
  st.write = ("Bienvenido al Módulo Listas")

valor_inicial = st.number_input("Ingrese el valor inicial")
valor_final = st.number_input("Ingrese el valor final")

lista_numeros=list(range(int(valor_inicial), int(valor_final)))
st.write(lista_numeros)
