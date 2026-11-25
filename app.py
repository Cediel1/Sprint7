import streamlit as st
import pandas as pd
import plotly.graph_objects as go

## leer los datos
df = pd.read_csv("vehicles_us.csv")

## crear el encabezado de la aplicación
st.header('vehículos en Estados Unidos')
## describir el tipo de datos que se están mostrando
st.write('Este conjunto de datos contiene información sobre anuncios de venta de vehiculos en Estados Unidos,' \
' incluyendo detalles como el precio, el año del modelo, la lectura del odómetro y otros atributos relevantes.')
st.markdown('---')  # Línea horizontal para separar secciones
st.write('La base de datos consta de las variables siguientes: price, model_year, model, condition,' \
'cylinders, fuel, odometer, transmission,type, paint_color, is_4wd, day_posted, day_listed')
st.write('El conjunto de datos contiene un total de 51525 registros, cada uno representando un anuncio individual de venta de un vehículo.')

## se separan las columnas numericas de las categóricas para poder hacer un análisis más detallado
columnas_numericas = ['price', 'model_year', 'cylinders', 'odometer', 'days_listed']
## crear un boton para mostrar un histograma de los datos
hist_button = st.checkbox('Construir histograma')
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    variable = st.selectbox('Elige la variable para el histograma', df.columns.tolist())  # Lista de variables para el histograma
    if variable in columnas_numericas:  # Verificar si la variable seleccionada es numérica
        st.write('La variable seleccionada es numérica. Se construirá un histograma por favor elija un rango de valores para la variable seleccionada.')
        min_val = df[variable].min()
        max_val = df[variable].max()
        rango = st.slider(f'Rango para {variable}', min_value=min_val, max_value=max_val, value=(min_val, max_val))
        df2 = df[(df[variable] >= rango[0]) & (df[variable] <= rango[1])]
    else:
        st.write('La variable seleccionada no es numérica. Se construirá un histograma de frecuencias categóricas.')
        df2 = df  # No se filtra el DataFrame si la variable no es numérica
    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=df2[variable])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del {}'.format(variable), xaxis_title=variable, yaxis_title='Frecuencia')
    st.plotly_chart(fig, use_container_width=True)

## crear un boton para mostrar un diagrama de dispersión de los datos
disp_button = st.checkbox('construir diagrama de dispersión')
if disp_button:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    eje_x = st.selectbox('Elige la columna para el eje X', columnas_numericas) # el usuario puede elegir la variable para el eje X
    eje_y = st.selectbox('Elige la columna para el eje Y', columnas_numericas) # el usuario puede elegir la variable para el eje Y
    min_x, max_x = df[eje_x].min(), df[eje_x].max() # se calculan los valores mínimo y máximo de las variables 
    min_y, max_y = df[eje_y].min(), df[eje_y].max() # seleccionadas para el eje X y el eje Y
    rango_x = st.slider('Rango para ' + eje_x, min_value=min_x, max_value=max_x, value=(min_x, max_x),key='slider_x') # el usuario puede seleccionar un rango de valores para el eje X
    rango_y = st.slider('Rango para ' + eje_y, min_value=min_y, max_value=max_y, value=(min_y, max_y),key='slider_y') # el usuario puede seleccionar un rango de valores para el eje Y
    ## se filtran los datos según los rangos seleccionados por el usuario para el eje X y el eje Y
    df_filtrado = df[(df[eje_x] >= rango_x[0]) & (df[eje_x] <= rango_x[1]) & (df[eje_y] >= rango_y[0]) & (df[eje_y] <= rango_y[1])]

    # Crear un diagrama de dispersión utilizando plotly.graph_objects
    fig_disp = go.Figure(data=go.Scatter(x=df_filtrado[eje_x], y=df_filtrado[eje_y], mode='markers'))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_disp.update_layout(title_text='Diagrama de Dispersión: {} vs {}'.format(eje_x, eje_y),
                           xaxis_title=eje_x,
                           yaxis_title=eje_y)
    st.plotly_chart(fig_disp, use_container_width=True) 

## crear un boton para mostrar la correlación entre las variables numéricas del conjunto de datos con un mapa de calor
corr_button = st.checkbox('Calcular correlación')
if corr_button:
        st.write('Cálculo de la correlación entre las variables numéricas del conjunto de datos de anuncios de venta de coches')
        # Calcular la matriz de correlación
        df_numericas = df[columnas_numericas]  # Seleccionar solo las columnas numéricas
        corr_matrix = df_numericas.corr()
        st.write('Matriz de correlación:')
        fig_heatmap = go.Figure(data=go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, 
                                                y=corr_matrix.columns, colorscale='Viridis', 
                                                text=corr_matrix.values, texttemplate='%{text:.2f}'))
        fig_heatmap.update_layout(title_text='Matriz de Correlación')

        st.plotly_chart(fig_heatmap, use_container_width=True)       # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    
