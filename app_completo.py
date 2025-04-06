import streamlit as st

st.title("Evaluación Guardia CAES")

# Diccionario de secciones con preguntas
secciones = {
    "POLICÍA": [
        "¿Cuida su imagen y presencia durante toda la guardia?",
        "¿Lleva el cabello con color natural y corte uniforme o recogido en moño (si aplica)?",
        "¿Tiene las uñas cuidadas y aseadas, sin pintar?",
        "¿Está correctamente afeitado al entrar y salir de la guardia?",
        "¿Tiene los tatuajes tapados conforme a la normativa?",
        "¿Utiliza maquillaje natural, si corresponde?",
        "¿Lleva el uniforme limpio y completo durante toda la guardia?",
        "¿El calzado está limpio y en condiciones reglamentarias?",
        "¿Adopta en todo momento una postura corporal adecuada y profesional?",
        "¿Evita manipular elementos no reglamentarios (manos en bolsillos, móviles, etc.)?",
        "¿Cumple las normas de imagen sin necesidad de advertencias previas?",
        "¿Su presencia inspira respeto y refleja seriedad?"
    ],
    "DISCIPLINA": [
        "¿Se exige a sí mismo en el cumplimiento de sus obligaciones?",
        "¿Cumple correctamente todas las órdenes recibidas?",
        "¿Mantiene comportamientos disciplinados en todo momento?",
        "¿Corrige con forma y tono adecuados cuando es necesario?"
    ],
    "INTERÉS": [
        "¿Muestra entrega y disponibilidad para realizar los cometidos de la guardia?",
        "¿Conoce los medios disponibles y sabe utilizarlos correctamente?",
        "¿Demuestra interés por ampliar sus conocimientos profesionales?",
        "¿Pregunta o investiga si desconoce un procedimiento o material?"
    ],
    "RESPONSABILIDAD": [
        "¿Asume ante el mando las órdenes que da a sus subordinados?",
        "¿Se responsabiliza de las decisiones tomadas durante su turno?",
        "¿Informa de forma honesta si algo no ha salido correctamente?"
    ],
    "INICIATIVA": [
        "¿Se ofrece voluntariamente para tareas fuera de sus obligaciones?",
        "¿Muestra entusiasmo y motivación por sus cometidos?",
        "¿Demuestra acierto, prudencia e iniciativa en su desempeño?",
        "¿Propone ideas o mejoras de forma proactiva?"
    ],
    "CONFIANZA EN SÍ MISMO": [
        "¿Toma decisiones con seguridad y sin dudar innecesariamente?",
        "¿Expresa sus ideas y opiniones de forma clara y respetuosa?",
        "¿Muestra actitud resolutiva ante los problemas?"
    ],
    "ACTITUD CON LOS SUBORDINADOS": [
        "¿Trata a sus subordinados con lealtad, respeto y corrección?",
        "¿Transmite con claridad los cometidos asignados?",
        "¿Es un modelo de comportamiento y actitud para sus subordinados?",
        "¿Se interesa por las condiciones de trabajo y seguridad de su personal?",
        "¿Fomenta la motivación del personal a su cargo?"
    ],
    "ACTITUD CON EL MANDO": [
        "¿Muestra lealtad y cooperación con sus superiores?",
        "¿Mantiene un trato correcto y respetuoso con el mando?",
        "¿Expone sus opiniones con corrección y educación?",
        "¿Evita actitudes defensivas o justificaciones innecesarias?"
    ],
    "COMPETENCIA / EFICACIA": [
        "¿Cumple los objetivos marcados en tiempo y forma durante la guardia?",
        "¿Realiza su trabajo con calidad y en los plazos asignados?",
        "¿Conoce perfectamente las tareas necesarias de su puesto?",
        "¿Actúa con eficacia en situaciones imprevistas o urgentes?"
    ],
    "TRATO": [
        "¿Se muestra afable y correcto con todos los miembros del equipo?",
        "¿Se comporta con respeto y empatía en situaciones de tensión o conflicto?",
        "¿Evita conflictos personales o enfrentamientos innecesarios?",
        "¿Contribuye a generar un buen ambiente de trabajo?"
    ],
    "RESISTENCIA A LA FATIGA": [
        "¿Mantiene la calidad de sus cometidos durante toda la guardia?",
        "¿Evita mostrar signos visibles de fatiga?",
        "¿Se mantiene activo, con energía y estado de alerta?",
        "¿Actúa con profesionalidad incluso ante el cansancio o el final del turno?"
    ]
}

total_puntos = 0
total_preguntas = 0
resultados = {}

for seccion, preguntas in secciones.items():
    st.header(seccion)
    respuestas = []
    for pregunta in preguntas:
        respuesta = st.checkbox(pregunta, key=pregunta)
        respuestas.append(respuesta)
    puntos = sum(respuestas)
    nota = round((puntos / len(preguntas)) * 10, 2)
    total_puntos += puntos
    total_preguntas += len(preguntas)
    resultados[seccion] = nota
    st.markdown(f"**Nota en {seccion}: {nota}**")

st.subheader("Resumen final")
nota_total = round((total_puntos / total_preguntas) * 10, 2)

if nota_total >= 9:
    letra = "A"
elif nota_total >= 7:
    letra = "B"
elif nota_total >= 5:
    letra = "C"
else:
    letra = "D"

st.markdown(f"### Nota final: {nota_total}")
st.markdown(f"### Calificación final: **{letra}**")
