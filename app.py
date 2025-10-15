import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# TÍTULO PRINCIPAL
# =========================
st.title("Deberes de Gilson Stalyn Tenemea Aguilar")
st.write("Aplicación interactiva con NumPy, Pandas y Matplotlib para análisis y visualización de datos.")

# =========================
# MENÚ DE NAVEGACIÓN
# =========================
st.sidebar.title("📘 Navegación")
seccion = st.sidebar.radio("Selecciona una sección:", [
    "🧮 Ejercicios con NumPy + Streamlit",
    "🎨 Ejercicios con Matplotlib"
])

# ============================================================
# SECCIÓN 1: NUMPY + STREAMLIT
# ============================================================
if seccion == "🧮 Ejercicios con NumPy + Streamlit":
    st.header("📊 Ejercicios con NumPy + Streamlit")
    st.write("Aplicación interactiva que utiliza NumPy y Pandas para análisis numérico y visualización de datos.")

    # =========================
    # EJERCICIO 1
    # =========================
    st.subheader("Ejercicio 1: Estadísticas básicas del 1 al 100")

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
    st.subheader("Ejercicio 2: Matriz aleatoria 5x5 (Distribución normal estándar)")

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
    st.subheader("Ejercicio 3: Distribución de frecuencias de números aleatorios")

    nums = np.random.randint(0, 11, 1000)
    valores, conteos = np.unique(nums, return_counts=True)
    df_frecuencias = pd.DataFrame({'Número': valores, 'Frecuencia': conteos})

    st.write("**Tabla de frecuencias:**")
    st.dataframe(df_frecuencias)

    st.bar_chart(df_frecuencias.set_index("Número"))

    # =========================
    # EJERCICIO 4
    # =========================
    st.subheader("Ejercicio 4: Normalización de un vector")

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
    st.subheader("📚 Gestión de Datos de Estudiantes")

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

    materias = [
        "Inteligencia Artificial",
        "Aplicaciones en la Nube",
        "Aplicaciones Seguras",
        "Formulación de Proyectos",
        "Proyectos Tecnológicos"
    ]

    data = {
        "nombres_completos": nombres_estudiantes,
        "edad": [0] * len(nombres_estudiantes),
        "nota_final": [0.0] * len(nombres_estudiantes),
        "materia": [materias[i % len(materias)] for i in range(len(nombres_estudiantes))]
    }

    df_estudiantes = pd.DataFrame(data)

    st.write("📝 **Editar o actualizar datos:**")
    df_editado = st.data_editor(df_estudiantes, num_rows="dynamic", use_container_width=True)

    st.write("**📊 Datos actuales:**")
    st.dataframe(df_editado, use_container_width=True)

    csv = df_editado.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descargar CSV", data=csv, file_name="estudiantes.csv", mime="text/csv")

    st.success("✅ Sección NumPy completada correctamente.")

# ============================================================
# SECCIÓN 2: MATPLOTLIB
# ============================================================
elif seccion == "🎨 Ejercicios con Matplotlib":
    st.header("🎨 Ejercicios (Matplotlib)")
    st.write("Visualización de datos con gráficos usando Matplotlib y Pandas.")

    # Crear y mostrar DataFrame base
    datos = {
        "fecha": pd.date_range("2024-01-01", periods=24, freq="M"),
        "categoria": ["A", "B", "C"] * 8,
        "producto": ["P1", "P2", "P3"] * 8,
        "precio": [10, 12, 9, 11, 10, 8, 12, 14, 9, 13, 12, 10,
                   11, 13, 9, 10, 15, 12, 14, 9, 8, 10, 11, 13],
        "cantidad": [5, 3, 6, 2, 8, 1, 4, 5, 7, 3, 2, 6,
                     4, 3, 8, 6, 7, 2, 5, 9, 3, 4, 2, 8],
    }
    df = pd.DataFrame(datos)
    df["mes"] = df["fecha"].dt.month_name()
    df["total"] = df["precio"] * df["cantidad"]

    st.subheader("📋 Datos de ejemplo")
    st.dataframe(df.head(), use_container_width=True)

    # 1️⃣ Gráfico de líneas
    st.subheader("1️⃣ Evolución del precio promedio mensual")
    promedio_mensual = df.groupby("mes")["precio"].mean()
    fig, ax = plt.subplots()
    ax.plot(promedio_mensual.index, promedio_mensual.values, marker="o", color="blue")
    ax.set_title("Evolución del precio promedio mensual")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Precio promedio")
    ax.grid(True)
    st.pyplot(fig)

    # 2️⃣ Gráfico de barras
    st.subheader("2️⃣ Top 5 combinaciones producto–mes con mayor total")
    top5 = df.groupby(["producto", "mes"])["total"].sum().sort_values(ascending=False).head(5)
    fig, ax = plt.subplots()
    top5.plot(kind="bar", color="skyblue", ax=ax)
    ax.set_title("Top 5 combinaciones producto–mes con mayor total")
    ax.set_xlabel("Producto - Mes")
    ax.set_ylabel("Total vendido")
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)

    # 3️⃣ Boxplot
    st.subheader("3️⃣ Boxplot del total por categoría")
    datos_categoria = [df[df["categoria"] == c]["total"] for c in df["categoria"].unique()]
    fig, ax = plt.subplots()
    ax.boxplot(datos_categoria, labels=df["categoria"].unique(), patch_artist=True)
    ax.set_title("Distribución del total por categoría")
    ax.set_ylabel("Total")
    ax.grid(True)
    st.pyplot(fig)

    # 4️⃣ Histograma
    st.subheader("4️⃣ Histograma de cantidad")
    fig, ax = plt.subplots()
    ax.hist(df["cantidad"], bins=10, color="lightgreen", edgecolor="black")
    ax.set_title("Distribución de cantidades vendidas")
    ax.set_xlabel("Cantidad")
    ax.set_ylabel("Frecuencia")
    ax.grid(True)
    st.pyplot(fig)

    st.success("✅ Gráficos generados correctamente.")
