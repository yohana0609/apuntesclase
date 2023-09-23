import streamlit as st

st.sidebar.title("calculadora ICI")
def pedir_valores():
    name = st.text_input("Nombre")
    n1 = st.number_input("Numero 1")
    n2 = st.number_input("Numero 2")

    if st.button("Sumar"):

        st.success(f"Hola {name}")
        st.write (f"{n1} + {n2} = {n1+n2}")

def operacion_resta():
    name = st.text_input("Nombre")
    n1 = st.number_input("Numero 1")
    n2 = st.number_input("Numero 2")

    if st.button("Resta"):

        st.success("Hola {name}")
        st.write (f"{n1} - {n2} = {n1-n2}")

def operacion_multiplicacion():
    name = st.text_input("Nombre")
    n1 = st.number_input("Numero 1")
    n2 = st.number_input("Numero 2")

    if st.button("Multiplicacion"):

        st.success(f"Hola {name}")
        st.write (f"{n1} * {n2} = {n1*n2}")

def operacion_division():
    name = st.text_input("Nombre")
    n1 = st.number_input("Numero 1")
    n2 = st.number_input("Numero 2")

    if st.button("Division"):

        st.success(f"Hola {name}")
        st.write (f"{n1} / {n2} = {n1/n2}")

opcion = st.sidebar.selectbox("Opciones", ["Suma","Resta","Multiplicacion","Division","Acerca de"])

match opcion:
    case "Suma":
        st.write ("Esta es la opcion suma...")
        pedir_valores()
    case "Resta":
        st.write ("Esta es la opcion resta...")
        operacion_resta()
    case "Multiplicacion":
        st.write ("Esta es la opcion multiplicacion...")
        operacion_multiplicacion()
    case "Division":
        st.write ("Esta es la opcion division...")
        operacion_division()
    case "Acerca de":
        st.write ("Derechos reservados ")
        
