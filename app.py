import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# Configuración
st.set_page_config(page_title="Mi Tienda - Inventario", page_icon="📦", layout="wide")
st.title("📦 Sistema de Inventario - Tienda Pequeña (Zapopan edition)")

# Base de datos
conn = sqlite3.connect('inventario.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS productos 
             (id INTEGER PRIMARY KEY, nombre TEXT, stock INTEGER, precio REAL, minimo INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS ventas 
             (id INTEGER PRIMARY KEY, fecha TEXT, producto TEXT, cantidad INTEGER, total REAL)''')
conn.commit()

# Login simple (para demo)
if 'logged' not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.subheader("🔑 Inicia sesión")
    password = st.text_input("Contraseña (demo: 1234)", type="password")
    if st.button("Entrar") and password == "1234":
        st.session_state.logged = True
        st.rerun()
    st.info("Usa 1234 para entrar (cámbiala después)")
else:
    # Menú
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Productos", "🛒 Registrar Venta", "📊 Dashboard", "⚠️ Alertas"])

    with tab1:
        st.subheader("Agregar / Ver Productos")
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre del producto")
            stock = st.number_input("Stock actual", min_value=0, value=10)
            precio = st.number_input("Precio $", min_value=0.0, value=99.0)
            minimo = st.number_input("Stock mínimo para alerta", min_value=1, value=5)
            if st.button("Agregar producto"):
                c.execute("INSERT INTO productos (nombre, stock, precio, minimo) VALUES (?, ?, ?, ?)",
                          (nombre, stock, precio, minimo))
                conn.commit()
                st.success("✅ Producto agregado")
        
        # Lista de productos
        df = pd.read_sql_query("SELECT * FROM productos", conn)
        if not df.empty:
            st.dataframe(df, use_container_width=True)
            # Editar stock rápido
            producto_edit = st.selectbox("Editar stock de:", df['nombre'])
            nuevo_stock = st.number_input("Nuevo stock", min_value=0)
            if st.button("Actualizar stock"):
                c.execute("UPDATE productos SET stock = ? WHERE nombre = ?", (nuevo_stock, producto_edit))
                conn.commit()
                st.rerun()

    with tab2:
        st.subheader("Registrar Venta")
        productos = pd.read_sql_query("SELECT nombre, stock, precio FROM productos", conn)
        if not productos.empty:
            prod = st.selectbox("Producto vendido", productos['nombre'])
            cantidad = st.number_input("Cantidad", min_value=1, max_value=int(productos[productos['nombre']==prod]['stock'].values[0]))
            if st.button("💰 Registrar venta"):
                precio_unit = productos[productos['nombre']==prod]['precio'].values[0]
                total = precio_unit * cantidad
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
                c.execute("INSERT INTO ventas (fecha, producto, cantidad, total) VALUES (?, ?, ?, ?)",
                          (fecha, prod, cantidad, total))
                # Restar stock
                c.execute("UPDATE productos SET stock = stock - ? WHERE nombre = ?", (cantidad, prod))
                conn.commit()
                st.success(f"✅ Venta registrada por ${total:.2f}")
                st.rerun()

    with tab3:
        st.subheader("📈 Dashboard")
        ventas_df = pd.read_sql_query("SELECT fecha, total FROM ventas", conn)
        if not ventas_df.empty:
            st.line_chart(ventas_df.set_index('fecha')['total'])
        
        productos_df = pd.read_sql_query("SELECT nombre, stock FROM productos", conn)
        st.bar_chart(productos_df.set_index('nombre')['stock'])

    with tab4:
        st.subheader("⚠️ Alertas de stock bajo")
        bajos = pd.read_sql_query("SELECT nombre, stock, minimo FROM productos WHERE stock < minimo", conn)
        if not bajos.empty:
            st.error("🚨 Productos con stock crítico:")
            st.dataframe(bajos)
            st.info("En la versión Heavy real esto enviaría email automático 😉")
        else:
            st.success("✅ Todo bien, ningún producto crítico")

    if st.button("Cerrar sesión"):
        st.session_state.logged = False
        st.rerun()
