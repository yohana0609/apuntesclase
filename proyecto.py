# Importa la biblioteca Streamlit para crear la interfaz web.
import streamlit as st  

# Importa la biblioteca CSV para manejar archivos CSV.
import csv 

agenda = []  # Lista para almacenar los contactos.

def cargar_contactos():
    """
    Esta función intenta cargar los contactos almacenados en un archivo CSV llamado 'contactos.csv' si existe.
    Los contactos se almacenan en la lista 'agenda'.
    """
    try:
        with open('contactos.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)  # Lee el archivo CSV como un diccionario.
            for row in reader:
                agenda.append(row)  # Agrega cada contacto a la lista 'agenda'.
    except FileNotFoundError:
        pass  # Si el archivo no existe, simplemente continúa sin hacer nada.

def guardar_contactos():
    """
    Esta función guarda los contactos almacenados en la lista 'agenda' en un archivo CSV llamado 'contactos.csv'.
    """
    with open('contactos.csv', mode='w', newline='') as file:
        fieldnames = ["Nombre", "Teléfono", "Correo", "Dirección", "Cumpleaños", "Notas"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Escribe la cabecera del archivo CSV.
        for contacto in agenda:
            writer.writerow(contacto)  # Escribe cada contacto en el archivo CSV.

def agregar_contacto():
    """
    Esta función permite al usuario ingresar información de contacto y agregarlo a la lista 'agenda'.
    Luego, guarda el contacto en el archivo CSV llamando a 'guardar_contactos()'.
    """
    nombre = st.text_input("Nombre completo:")
    telefono = st.text_input("Número de teléfono:")
    correo = st.text_input("Dirección de correo electrónico:")
    direccion = st.text_input("Dirección física:")
    cumpleanos = st.text_input("Fecha de cumpleaños:")
    notas = st.text_area("Notas adicionales:")

    if st.button("Agregar contacto"):
        contacto = {
            "Nombre": nombre,
            "Teléfono": telefono,
            "Correo": correo,
            "Dirección": direccion,
            "Cumpleaños": cumpleanos,
            "Notas": notas
        }

        agenda.append(contacto)  # Agrega el contacto a la lista 'agenda'.
        st.success("Contacto agregado correctamente.")
        guardar_contactos()  # Guarda el contacto en el archivo CSV.

def buscar_contacto():
    """
    Esta función permite al usuario buscar un contacto por nombre en la lista 'agenda'.
    Muestra la información del contacto si se encuentra.
    """
    nombre = st.text_input("Nombre del contacto a buscar:")

    if st.button("Buscar contacto"):
        for contacto in agenda:
            if contacto["Nombre"].lower() == nombre.lower():
                st.write("Información del contacto:")
                for clave, valor in contacto.items():
                    st.write(f"{clave}: {valor}")
                return
        st.warning("Contacto no encontrado.")

def mostrar_contactos():
    """
    Esta función permite al usuario mostrar todos los contactos almacenados en la lista 'agenda'.
    """
    if st.button("Mostrar todos los contactos"):
        st.write("Lista de contactos:")
        for i, contacto in enumerate(agenda, 1):
            st.write(f"Contacto {i}: {contacto['Nombre']}")

cargar_contactos()  # Carga contactos al iniciar la aplicación.

st.title("Agenda Personal")  # Establece el título de la aplicación web.

opcion = st.selectbox(
    "Seleccione una opción:",  # Muestra un cuadro de selección con opciones.
    ("Agregar contacto", "Buscar contacto", "Mostrar todos los contactos")
)

# Controla la aplicación según la opción seleccionada por el usuario.
if opcion == "Agregar contacto":
    agregar_contacto()
elif opcion == "Buscar contacto":
    buscar_contacto()
elif opcion == "Mostrar todos los contactos":
    mostrar_contactos()
