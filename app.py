import streamlit as st

st.title("Evaluación Guardia CAES")

st.header("POLICÍA")
p1 = st.checkbox("¿Cuida su imagen y presencia durante toda la guardia?")
p2 = st.checkbox("¿Lleva el cabello con color natural y corte uniforme o recogido en moño (si aplica)?")
p3 = st.checkbox("¿Tiene las uñas cuidadas y aseadas, sin pintar?")
p4 = st.checkbox("¿Está correctamente afeitado al entrar y salir de la guardia?")
p5 = st.checkbox("¿Tiene los tatuajes tapados conforme a la normativa?")
p6 = st.checkbox("¿Utiliza maquillaje natural, si corresponde?")
p7 = st.checkbox("¿Lleva el uniforme limpio y completo durante toda la guardia?")
p8 = st.checkbox("¿El calzado está limpio y en condiciones reglamentarias?")
p9 = st.checkbox("¿Adopta en todo momento una postura corporal adecuada y profesional?")
p10 = st.checkbox("¿Evita manipular elementos no reglamentarios (manos en bolsillos, móviles, etc.)?")
p11 = st.checkbox("¿Cumple las normas de imagen sin necesidad de advertencias previas?")
p12 = st.checkbox("¿Su presencia inspira respeto y refleja seriedad?")

respuestas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
total_preguntas = len(respuestas)
puntos = sum(respuestas)
nota_numerica = round((puntos / total_preguntas) * 10, 2)

if nota_numerica >= 9:
    letra = "A"
elif nota_numerica >= 7:
    letra = "B"
elif nota_numerica >= 5:
    letra = "C"
else:
    letra = "D"

st.subheader("Resultado")
st.write(f"✔️ Total respuestas positivas: {puntos} / {total_preguntas}")
st.write(f"📊 Nota numérica: **{nota_numerica}**")
st.write(f"🔠 Calificación: **{letra}**")
