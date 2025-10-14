import streamlit as st
import numpy as np
import pandas as pd

# =========================
# TÍTULO PRINCIPAL
# =========================
st.title("Deberes de Gilson Stalyn Tenemea Aguilar")
st.title("📊 Ejercicios con NumPy + Streamlit")
st.write("Aplicación interactiva que utiliza NumPy y Pandas para análisis numérico y visualización de datos.")

# =========================
# EJERCICIO 1
# =========================
st.header("Ejercicio 1: Estadísticas básicas del 1 al 100")

arr = np.arange(1, 101)
media = np.mean(arr)
mediana = np.median(arr)
varianza = np.var(arr)
percentil_90 = np.percentile(arr, 90)

st.write(f"**Array:** {arr}")
st.write(f"**Media:** {media}")
st.write(f"**Mediana:** {mediana}")
st.write(f"**Varianza:** {varianza}")
st.write(f"**Percentil 90:** {percentil_90}")

# =========================
# EJERCICIO 2
# =========================
st.header("Ejercicio 2: Matriz aleatoria 5x5 (Distribución normal estándar)")

matriz = np.random.randn(5, 5)
determinante = np.linalg.det(matriz)
traza = np.trace(matriz)

st.write("**Matriz generada:**")
st.write(matriz)
st.write(f"**Determinante:** {determinante:.4f}")
st.write(f"**Traza:** {traza:.4f}")

# =========================
# EJERCICIO 3
# =========================
st.header("Ejercicio 3: Distribución de frecuencias de números aleatorios")

nums = np.random.randint(0, 11, 1000)
valores, conteos = np.unique(nums, return_counts=True)
df_frecuencias = pd.DataFrame({'Número': valores, 'Frecuencia': conteos})

st.write("**Tabla de frecuencias:**")
st.dataframe(df_frecuencias)

st.bar_chart(df_frecuencias.set_index("Número"))

# =========================
# EJERCICIO 4
# =========================
st.header("Ejercicio 4: Normalización de un vector")

opcion = st.radio("Selecciona una opción:", ["Ingresar vector manualmente", "Generar vector aleatorio"])

if opcion == "Ingresar vector manualmente":
    entrada = st.text_input("Ingresa números separados por comas (ejemplo: 5, 10, 15):")
    if entrada:
        try:
            v = np.array([float(x.strip()) for x in entrada.split(",")])
        except:
            st.error("Error al procesar el vector. Asegúrate de ingresar números válidos.")
            v = np.array([])
    else:
        v = np.array([])
else:
    longitud = st.slider("Selecciona longitud del vector", 3, 15, 5)
    v = np.random.randint(1, 100, longitud)
    st.write(f"**Vector aleatorio generado:** {v}")

if v.size > 0:
    media_v = np.mean(v)
    std_v = np.std(v)
    normalizado = (v - media_v) / std_v
    st.write(f"**Media:** {media_v:.2f} | **Desviación estándar:** {std_v:.2f}")
    st.write(f"**Vector normalizado:** {normalizado}")

# =========================
# SECCIÓN ADICIONAL: DATAFRAME DE ESTUDIANTES
# =========================
st.header("📚 Gestión de Datos de Estudiantes")

st.write("Agrega información de 18 jóvenes del ciclo:")

# Lista de estudiantes
nombres_estudiantes = [
    "MARIUXI ANDREA CALLE DUMAGUALA",
    "MAURA MILETH CALLE LEON",
    "STEVEN ALEXANDER CARPIO CHILLOGALLO",
    "ERICK FERNANDO CHACON AVILA",
    "EDWIN ALEXANDER CHOEZ DOMINGUEZ",
    "ADRIANA VALENTINA CORNEJO ULLOA",
    "DAVID ALFONSO ESPINOZA CHÉVEZ",
    "ANTHONY MAURICIO FAJARDO VASQUEZ",
    "FREDDY ISMAEL GOMEZ ORDOÑEZ",
    "WENDY NICOLE LLIVICHUZHCA MAYANCELA",
    "ALEXANDER ISMAEL LOJA LLIVICHUZHCA",
    "DAVID ALEXANDER LOPEZ SALTOS",
    "VICTOR JONNATHAN MENDEZ VILLA",
    "JOHN SEBASTIAN MONTENEGRO CALLE",
    "CARMEN ELIZABETH NEIRA INGA",
    "JOEL STALYN PESANTEZ BERREZUETA",
    "GILSON STALYN TENEMEA AGUILAR",
    "KENNY ALEXANDER VALDIVIESO CORONEL"
]

# Materias (puedes asignarlas aleatoriamente o iguales para todos)
materias = [
    "Inteligencia Artificial",
    "Aplicaciones en la Nube",
    "Aplicaciones Seguras",
    "Formulación de Proyectos",
    "Proyectos Tecnológicos"
]

# Crear DataFrame base
data = {
    "nombres_completos": nombres_estudiantes,
    "edad": [0] * len(nombres_estudiantes),
    "nota_final": [0.0] * len(nombres_estudiantes),
    "materia": [materias[i % len(materias)] for i in range(len(nombres_estudiantes))]
}

df_estudiantes = pd.DataFrame(data)

# DataFrame editable
st.write("📝 **Editar o actualizar datos:**")
df_editado = st.data_editor(df_estudiantes, num_rows="dynamic", use_container_width=True)

# Mostrar los datos
st.write("**📊 Datos actuales:**")
st.dataframe(df_editado, use_container_width=True)

# Botón para descargar CSV
csv = df_editado.to_csv(index=False).encode('utf-8')
st.download_button("📥 Descargar CSV", data=csv, file_name="estudiantes.csv", mime="text/csv")

st.success("✅ Aplicación completada correctamente.")