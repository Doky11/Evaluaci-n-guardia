import streamlit as st
from docx import Document
from datetime import date
from io import BytesIO

st.title("Informe de Guardia CAES - Evaluación Automática")

# --- 1. ENCABEZADO MANUAL ---
st.header("Encabezado del Informe")
informante = st.text_input("Informante")
fecha = st.date_input("Fecha", value=date.today())
alumno = st.text_input("Alumno evaluado")
puesto = st.text_input("Puesto durante la guardia")

# --- 2. CHECKLIST Y CÁLCULO POR CATEGORÍA ---
st.header("Evaluación por Categorías")

secciones = {
    "POLICÍA": 12,
    "DISCIPLINA": 6,
    "INTERES": 6,
    "RESPONSABILIDAD": 5,
    "INICIATIVA": 5,
    "CONFIANZA EN SI MISMO": 5,
    "ACTITUD CON LOS SUBORDINADOS": 6,
    "ACTITUD CON EL MANDO": 5,
    "COMPETENCIA / EFICACIA": 5,
    "TRATO": 5,
    "RESISTENCIA A LA FATIGA": 4
}

notas_letras = {}
notas_numericas = []

for seccion, total_preguntas in secciones.items():
    st.subheader(seccion)
    respuestas_positivas = st.slider(f"Número de respuestas positivas en {seccion}", 0, total_preguntas, 0)
    nota = round((respuestas_positivas / total_preguntas) * 10, 2)
    notas_numericas.append(nota)
    
    if nota >= 9:
        letra = "A"
    elif nota >= 7:
        letra = "B"
    elif nota >= 5:
        letra = "C"
    else:
        letra = "D"
    
    notas_letras[seccion] = letra
    st.write(f"Nota: {nota} — Calificación: {letra}")

# --- 3. NOTA FINAL Y OBSERVACIONES ---
st.header("Resumen Final")
nota_media = round(sum(notas_numericas) / len(notas_numericas), 2)

if nota_media >= 9:
    nota_final = "A"
elif nota_media >= 7:
    nota_final = "B"
elif nota_media >= 5:
    nota_final = "C"
else:
    nota_final = "D"

st.write(f"📊 Nota media: **{nota_media}**")
st.write(f"🔠 Calificación final: **{nota_final}**")

observaciones = st.text_area("Observaciones generales / Justificación")

# --- 4. GENERACIÓN DE INFORME ---
st.header("Generar Informe")

def generar_informe():
    plantilla = "INFORME EN BLANCO.docx"
    doc = Document(plantilla)

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                texto = cell.text.strip()
                if texto == "INFORMANTE":
                    cell.text = "INFORMANTE\n" + informante
                elif texto == "FECHA":
                    cell.text = "FECHA\n" + fecha.strftime('%d/%m/%Y')
                elif texto == "ALUMNO":
                    cell.text = "ALUMNO\n" + alumno
                elif texto == "PUESTO":
                    cell.text = "PUESTO\n" + puesto
                elif texto in notas_letras:
                    letra = notas_letras[texto]
                    if letra == "A":
                        row.cells[1].text = "X"
                    elif letra == "B":
                        row.cells[2].text = "X"
                    elif letra == "C":
                        row.cells[3].text = "X"
                    elif letra == "D":
                        row.cells[4].text = "X"
                elif "Nota media:" in texto:
                    cell.text = "Nota media: " + str(nota_media)
                elif "OBSERVACIONES GENERAL" in texto:
                    cell.text = "OBSERVACIONES GENERAL / JUSTIFICACIÓN\n" + observaciones

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

if st.button("📄 Generar Informe Word"):
    docx_file = generar_informe()
    st.download_button(
        label="📥 Descargar Informe",
        data=docx_file,
        file_name=f"Informe_{alumno.replace(' ', '_')}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
