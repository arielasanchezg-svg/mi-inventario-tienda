import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Ariel Hub", page_icon="🚀", layout="wide")

# CSS PREMIUM (dark executive look)
st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #0f172a, #1e2937);}
    .stCard {background: rgba(255,255,255,0.08); backdrop-filter: blur(20px); border-radius: 20px; border: 1px solid rgba(255,215,0,0.2);}
    h1 {color: #ffd700; text-shadow: 0 0 20px #ffd700;}
    .metric {font-size: 2.2rem; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Ariel Hub - Mi Vida Ejecutiva 2026")
st.caption("Ariel Alejandro • 26 • Ejecutivo de Cuenta • Zapopan")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Dashboard", "💰 Finanzas", "🚗 Spark 115k", "👥 CRM Banco", "📰 Noticias"])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("💰 Ingresos", "$30,000", "✅ +comisiones")
    with col2: st.metric("🚗 Km Spark", "115,432", "⚠️ +1,200")
    with col3: st.metric("👥 Pipeline", "78%", "↑ 12%")
    with col4: st.metric("📰 Última novedad", "Ciencia", "hace 2h")
    
    st.subheader("📈 Resumen Marzo 2026")
    df = pd.DataFrame({"Mes": ["Ene","Feb","Mar"], "Ahorro": [7200,8500,9800]})
    fig = px.line(df, x="Mes", y="Ahorro", markers=True, title="Ahorro mensual")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("💰 Mis 30k - Finanzas")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Gastos totales", "$17,200", "-8% vs mes pasado")
        gastos = {"Gasolina Spark": 2800, "Salidas con novia": 4200, "Comida": 3800, "Otros": 6400}
        fig = px.pie(values=list(gastos.values()), names=list(gastos.keys()), title="¿Dónde se fue el dinero?")
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.progress(0.42)
        st.write("**Meta Noviazgo / Boda** $120,000 → 42% completado")
        st.success("Si sigues así, en 14 meses tienes el enganche del depa 🔥")

with tab3:
    st.subheader("🚗 Spark 115k - Mi Carro")
    st.image("https://source.unsplash.com/800x400/?chevrolet-spark-silver", use_column_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Kilometraje actual", "115,432 km")
        st.metric("Costo por km", "$2.15")
    with col2:
        st.metric("Próximo servicio", "en 1,200 km", "¡Cambio de aceite!")
        st.metric("Gasolina este mes", "$2,800")
    fig = px.line(x=["Ene","Feb","Mar"], y=[2400,2600,2800], title="Consumo gasolina")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("👥 CRM Banco - Pipeline")
    st.metric("Cerrados este mes", "$420,000", "7 clientes")
    data = {"Cliente": ["Juan Pérez", "María López", "Carlos Ruiz"], "Próxima acción": ["Llamar mañana", "Enviar contrato", "Seguimiento"], "Monto": [85000,120000,215000]}
    st.dataframe(pd.DataFrame(data), use_container_width=True)
    st.success("Proyección comisiones: **$6,800 extra** este mes 💰")

with tab5:
    st.subheader("📰 Noticias que te interesan")
    cine, poli, cien = st.tabs(["🎥 Cine", "🗳️ Política", "🔬 Ciencia"])
    with cine:
        st.image("https://source.unsplash.com/600x300/?movie-premiere", use_column_width=True)
        st.write("**Dune 3 ya tiene fecha** – Primer tráiler rompe récords")
        st.caption("Estreno diciembre 2026 | Fuente: CinePremiere")
    with poli:
        st.image("https://source.unsplash.com/600x300/?mexico-politics", use_column_width=True)
        st.write("**Reforma judicial avanza en Cámara** – ¿Qué significa para tu crédito?")
        st.caption("Actualizado hace 4h | Fuente: El Financiero")
    with cien:
        st.image("https://source.unsplash.com/600x300/?james-webb-telescope", use_column_width=True)
        st.write("**James Webb descubre galaxia más antigua** – Cambia todo lo que sabíamos")
        st.caption("NASA • 1 marzo 2026")

st.caption("App hecha con ❤️ por Grok • Actualiza la página para ver animaciones Plotly")
