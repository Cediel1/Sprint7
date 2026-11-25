import streamlit as st
import pandas as pd
import plotly.graph_objects as go

## leer los datos
df = pd.read_csv("vehicles_us.csv")


st.header('vehículos en Estados Unidos')
## crear un boton para mostrar los datos
hist_button = st.checkbox('Construir histograma')
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=df['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro',
                      xaxis_title='Lectura del Odómetro',
                      yaxis_title='Frecuencia')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.checkbox('construir diagrama de dispersión')
if disp_button:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un diagrama de dispersión utilizando plotly.graph_objects
    fig_disp = go.Figure(data=go.Scatter(x=df['model_year'], y=df['price'], mode='markers'))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_disp.update_layout(title_text='Diagrama de Dispersión: Año vs Precio',
                           xaxis_title='Año del Modelo',
                          yaxis_title='Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig_disp, use_container_width=True)