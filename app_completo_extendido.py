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
        "¿Adopta una postura corporal profesional durante el servicio?",
        "¿Evita gestos o actitudes informales cuando está de servicio?",
        "¿Lleva todos los distintivos reglamentarios correctamente colocados?",
        "¿Cuida su postura cuando está en presencia del mando o del público?"
    ],
    "DISCIPLINA": [
        "¿Se exige a sí mismo en el cumplimiento de sus obligaciones?",
        "¿Cumple correctamente todas las órdenes recibidas?",
        "¿Mantiene comportamientos disciplinados en todo momento?",
        "¿Corrige a otros con forma y tono adecuados?",
        "¿Acude puntual a formaciones, relevos y partes?",
        "¿Se adapta sin protestas a cambios en turnos o cometidos?"
    ],
    "INTERÉS": [
        "¿Muestra entrega y disponibilidad en los cometidos?",
        "¿Conoce y domina los medios y materiales asignados?",
        "¿Demuestra interés por ampliar conocimientos técnicos?",
        "¿Pregunta cuando desconoce algo?",
        "¿Se mantiene atento durante todo su turno?",
        "¿Evita distracciones frecuentes o uso de dispositivos personales?"
    ],
    "RESPONSABILIDAD": [
        "¿Asume ante el mando las órdenes que da a sus subordinados?",
        "¿Se responsabiliza de las decisiones tomadas durante su turno?",
        "¿Informa con sinceridad cuando algo no sale como se esperaba?",
        "¿Se anticipa a las necesidades del servicio sin que se le indique?",
        "¿Finaliza sus cometidos aunque no haya supervisión directa?"
    ],
    "INICIATIVA": [
        "¿Se ofrece voluntariamente para tareas fuera de sus obligaciones?",
        "¿Muestra entusiasmo y motivación por sus cometidos?",
        "¿Demuestra acierto, prudencia e iniciativa en el desempeño?",
        "¿Propone ideas o mejoras para el servicio?",
        "¿Reacciona rápidamente ante situaciones inesperadas?"
    ],
    "CONFIANZA EN SÍ MISMO": [
        "¿Toma decisiones con seguridad y sin dudar excesivamente?",
        "¿Expresa sus ideas con claridad y respeto?",
        "¿Muestra actitud resolutiva ante los problemas?",
        "¿Se mantiene firme y tranquilo ante la presión del mando?",
        "¿Acepta responsabilidades con naturalidad?"
    ],
    "ACTITUD CON LOS SUBORDINADOS": [
        "¿Trata con respeto y corrección a sus subordinados?",
        "¿Transmite claramente los cometidos de la guardia?",
        "¿Da ejemplo en actitud y presencia?",
        "¿Se interesa por las condiciones del personal a su cargo?",
        "¿Fomenta la motivación y el buen ambiente?",
        "¿Evita favoritismos y mantiene equidad en el trato?"
    ],
    "ACTITUD CON EL MANDO": [
        "¿Muestra lealtad y cooperación con sus superiores?",
        "¿Trata con respeto al mando en todas las circunstancias?",
        "¿Expone opiniones de forma educada y constructiva?",
        "¿Cumple con lo ordenado sin justificar de forma innecesaria?",
        "¿Consulta dudas con claridad sin parecer inseguro?"
    ],
    "COMPETENCIA / EFICACIA": [
        "¿Cumple los objetivos en tiempo y forma durante la guardia?",
        "¿Realiza el trabajo con calidad y sin errores frecuentes?",
        "¿Conoce perfectamente las tareas que debe desempeñar?",
        "¿Actúa con eficacia ante imprevistos o incidencias?",
        "¿Prioriza correctamente sus tareas según la situación?"
    ],
    "TRATO": [
        "¿Es afable con todos los miembros de la guardia?",
        "¿Maneja con calma las situaciones de tensión?",
        "¿Evita actitudes conflictivas o provocadoras?",
        "¿Contribuye al clima de respeto y cooperación?",
        "¿Escucha activamente y responde con empatía?"
    ],
    "RESISTENCIA A LA FATIGA": [
        "¿Mantiene el rendimiento a lo largo de toda la guardia?",
        "¿Evita mostrar signos de cansancio o desánimo?",
        "¿Se mantiene alerta y disponible hasta el final?",
        "¿No reduce su implicación aunque esté fatigado?"
    ]
}

total_puntos = 0
total_preguntas = 0

st.divider()
for seccion, preguntas in secciones.items():
    st.header(seccion)
    respuestas = []
    for pregunta in preguntas:
        respuesta = st.checkbox(pregunta, key=pregunta)
        respuestas.append(respuesta)

    puntos = sum(respuestas)
    nota = round((puntos / len(preguntas)) * 10, 2)

    if nota >= 9:
        letra = "A"
    elif nota >= 7:
        letra = "B"
    elif nota >= 5:
        letra = "C"
    else:
        letra = "D"

    st.markdown(f"📝 **Nota en {seccion}:** {nota} — **Calificación:** {letra}")
    st.divider()
    total_puntos += puntos
    total_preguntas += len(preguntas)

# Nota final
st.subheader("Resumen final de la Evaluación")
nota_total = round((total_puntos / total_preguntas) * 10, 2)

if nota_total >= 9:
    letra_final = "A"
elif nota_total >= 7:
    letra_final = "B"
elif nota_total >= 5:
    letra_final = "C"
else:
    letra_final = "D"

st.markdown(f"### ✅ Nota final: {nota_total}")
st.markdown(f"### 🔠 Calificación final: **{letra_final}**")
