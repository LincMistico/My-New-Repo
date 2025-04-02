import pandas as pd
import plotly.express as px
import streamlit as st
        
# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Análisis de datos de vehículos')

# Casillas de verificación
build_histogram = st.checkbox('Mostrar histograma de kilometraje')
build_scatter = st.checkbox('Mostrar diagrama de dispersión (precio vs kilometraje)')

# Generar histograma si la casilla está seleccionada
if build_histogram:
    st.write('Distribución de kilometraje de los vehículos')
    fig_hist = px.histogram(car_data, x="odometer", 
                           title="Distribución de Kilometraje",
                           labels={"odometer": "Kilometraje"},
                           color_discrete_sequence=['blue'])
    st.plotly_chart(fig_hist, use_container_width=True)

# Generar diagrama de dispersión si la casilla está seleccionada
if build_scatter:
    st.write('Relación entre precio y kilometraje de los vehículos')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", 
                            title="Precio vs Kilometraje",
                            labels={"odometer": "Kilometraje", "price": "Precio ($)"},
                            color_discrete_sequence=['red'])
    st.plotly_chart(fig_scatter, use_container_width=True)

# Mostrar datos brutos si el usuario lo desea
if st.checkbox('Mostrar datos brutos'):
    st.write(car_data)