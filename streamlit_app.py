
import json
import requests
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from CSS_styles import apply_styles
import base64
import webbrowser
from pathlib import Path
from streamlit_lottie import st_lottie
from ML import get_rating,plot_gauge
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('yelp_google_merged.csv')
st.set_page_config(layout="wide")

valores_unicos_estado = df['state'].unique().tolist()
valores_unicos_estado = [x for x in valores_unicos_estado if not pd.isna(x)]
tupla_valores_unicos_estado = tuple(valores_unicos_estado)

# Obtener las ciudades correspondientes al estado seleccionado
@st.cache_data # Utilizar caché para evitar recálculos innecesarios
def obtener_ciudades_por_estado(estado):
    ciudades = df.loc[(df['state'] == estado) & (~df['ciudad'].str.contains(r'\d', na=False)), 'ciudad'].dropna().unique().tolist()
    return tuple(ciudades)




@st.cache_data # Utilizar caché para evitar recálculos innecesarios
def obtener_ciudad_recomendada():
    df_cleaned = df.dropna(subset=['ciudad', 'sector_economico'])
    promedio_rating_estado_sector = df_cleaned.groupby(['state', 'sector_economico'])['rating'].mean()
    mejor_sector_por_estado = promedio_rating_estado_sector.groupby('state').idxmax().apply(lambda x: x[1])
    mejor_ciudad_por_estado_sector = df_cleaned.groupby(['state', 'sector_economico', 'ciudad'])['rating'].mean().groupby(['state', 'sector_economico']).idxmax().apply(lambda x: x[2])
    valores_unicos_estado = df_cleaned['state'].dropna().unique().tolist()
    valores_unicos_sector = df_cleaned['sector_economico'].dropna().unique().tolist()
    valores_unicos_estado.insert(0, "Recomendar")
    valores_unicos_sector.insert(0, "Recomendar")
    
    return valores_unicos_sector,valores_unicos_estado,mejor_sector_por_estado,mejor_ciudad_por_estado_sector





url = requests.get(
    "https://assets3.lottiefiles.com/packages/lf20_kUtZCR7Zyk.json")
url_json = dict()
if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in the URL")
    
 
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html
        
def start_capture():
        st.session_state.page_1 = 0
        st.session_state.page_2 = 1
        st.session_state.page_3 = 0
                
apply_styles()
st.markdown('<style>' + open('css/style.css').read() + '</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns((2.05,3,1))

with col1:
    st.write(' ')

with col2:
    st.markdown(img_to_html('img/logo2.png'), unsafe_allow_html=True)
with col3:
    st.write(' ')
#------------------------------


st.markdown(
"""
<style>
button[kind="primary"] {
    background: none!important;
    border: none;
    padding: 0!important;
    color: #7c7d7a !important;
    text-decoration: none;
    cursor: pointer;
    border: none !important;
    font-family: sans-serif; /* Tipo de fuente deseado */
    font-weight: bold; /* Hace la fuente en negrita (bold) */  
}
button[kind="primary"]:hover {
    text-decoration: none;
    color: #14eeab !important;
}
button[kind="primary"]:focus {
    outline: none !important;
    box-shadow: none !important;
    color: #f7faff !important;
}
</style>
""",
unsafe_allow_html=True,
)



if 'page_1' not in st.session_state:
    	st.session_state.page_1 = 1
if 'page_2' not in st.session_state:
    	st.session_state.page_2 = 0
if 'page_3' not in st.session_state:
    	st.session_state.page_3 = 0



#----------------------------------------------------------------
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

def rpage_1():

    st.markdown(
        """
        <style>
        button[kind="secondary"] {
            background: #14EEAB;
            border: none;
            color: #f7faff !important;
            text-decoration: none;
            cursor: pointer;
            border: none !important;
            font-family: sans-serif; /* Tipo de fuente deseado */
            font-size:26px !important;
            font-weight: bold; /* Hace la fuente en negrita (bold) */  
            border-radius: 50%/50%;
            height: 3em;
            width: 3em;
            
        }
        button[kind="secondary"]:hover {
            background: #12c48d;
            text-decoration: none;
            color: gray !important;
        }
        button[kind="secondary"]:focus {
            outline: none !important;
            box-shadow: none !important;
            color: #f7faff !important;

        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    bot1, bot2, bot3 = st.columns((3.33,1,3))
    with bot1:
        st.write(' ')   

    with bot2:
        st.markdown(img_to_html('img/text.png'), unsafe_allow_html=True)
    with bot3:
        st.write(' ')  


    bot1, bot2, bot3 = st.columns((3.87,1,3))
    with bot1:
        st.write(' ')   

    with bot2:
        if st.session_state.page_2 == 0:
            btun = st.button(":rocket:",type="secondary",on_click=start_capture)
            if btun:
                st.session_state.page_1 = 0
                st.session_state.page_2 = 1
                st.session_state.page_3 = 0

                
    with bot3:
        st.write(' ')   
        
    st.write(' ')
    st.write(' ')
    st.write(' ')



    st.markdown("""
    <style>
    .big-font {
        font-size:80px !important;
        font-family: sans-serif; /* Tipo de fuente deseado */
        font-weight: bold; /* Hace la fuente en negrita (bold) */  
        text-align: right;
        color: #555750; /* Color deseado (en este caso, rojo) */
        line-height: 1.1;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .big-font2 {
        font-size:16px !important;
        font-family: sans-serif; /* Tipo de fuente deseado */
        font-weight: bold; /* Hace la fuente en negrita (bold) */  
        color: #7c7d7a; /* Color deseado (en este caso, rojo) */
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .big-font3 {
        font-size:60px !important;
        font-family: sans-serif; /* Tipo de fuente deseado */
        font-weight: bold; /* Hace la fuente en negrita (bold) */  }

        
    }
    </style>
    """, unsafe_allow_html=True)

    t1, t2,t2_5,t3,t4 = st.columns((1.4,3,1,3,1))
    with t1:
        st.write(' ')       
    with t2:
        st.markdown('<p class="big-font">🢒Potencia tus negocios usando ML</p>', unsafe_allow_html=True)
        st.title(" ")

        f1,f2= st.columns((1,1))
        with f1:
            st.title(" ")
        with f2:
            st_lottie(url_json)

        
        
    with t2_5:
        st.markdown(img_to_html('img/spacer.png'), unsafe_allow_html=True) 
    with t3:
        st.markdown('<p class="big-font2"><br>Nuestro sistema de recomendación te ayuda a encontrar el lugar perfecto para abrir tu próximo local. Ingresa tus preferencias, y nuestro sistema te proporcionará una lista personalizada de lugares recomendados basados en tu perfil. Ahorra tiempo y toma decisiones informadas para tu negocio.</p>', unsafe_allow_html=True)
        f1,f2= st.columns((1,1))
        with f1:
            st.write(' ')  
            st.write(' ')  
            st.write(' ')    
            st.markdown(img_to_html('img/facs.png'), unsafe_allow_html=True)
        with f2:
            st.write(' ')  

    with t4:
        st.write(' ')   



    title_placeholder = st.empty()
    # title_placeholder.markdown("<h1 style='text-align: center;'>Bienvenido a ANALYZING!. Nuestro sistema de recomendación te ayuda a encontrar el lugar perfecto para abrir tu próximo local</h1>", unsafe_allow_html=True) 

    # title = st.text_input(" "," ")
    #-------------------------------------------------------------
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
#--------------------------------------------------------------------------------------------------------------------------------------------------

def rpage_2():
    
    st.markdown(
        """
        <style>
        button[kind="secondary"] {
            background: #14EEAB;
            border: none;
            color: #555750 !important;
            text-decoration: none;
            cursor: pointer;
            border: none !important;
            font-family: sans-serif; /* Tipo de fuente deseado */
            font-size:26px !important;
            font-weight: bold; /* Hace la fuente en negrita (bold) */  
            height: 1.8em;
            width: 7em;
            
        }
        button[kind="secondary"]:hover {
            background: #12c48d;
            text-decoration: none;
            color: white !important;
        }
        button[kind="secondary"]:focus {
            outline: none !important;
            box-shadow: none !important;
            color: #555750 !important;

        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("""
        <style>
        .big-font2 {
            font-size:16px !important;
            font-family: sans-serif; /* Tipo de fuente deseado */
            font-weight: bold; /* Hace la fuente en negrita (bold) */  
            color: #7c7d7a; /* Color deseado (en este caso, rojo) */
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True
    )    
    
    st.markdown("""
        <style>
        .stSelectbox:first-of-type > div[data-baseweb="select"] > div {
            color: #555750

               
        }
        div[role="listbox"] ul {
            background-color: #555750;
         }
        </style>
    """, unsafe_allow_html=True)    
    
    st.markdown("<h5 style='text-align: center; color: #555750;'>...PREDECIR RATING PARA ESTADO,CIUDAD Y SECTOR ECONOMICO</h5>", unsafe_allow_html=True)
    st.write(' ')  
    st.write(' ')  
    st.write(' ')  

    col1, col2, col3 = st.columns(3)
    

    with col1:
        estado_seleccionado = st.selectbox(
            'ESTADO',
            tupla_valores_unicos_estado)

    with col2:
        ciudades_por_estado = obtener_ciudades_por_estado(estado_seleccionado)
        ciudad_seleccionada = st.selectbox(
            'CUIDAD',
            ciudades_por_estado)

    with col3:
        sector = st.selectbox(
            'SECTOR ECONOMICO',
            ('cuidado de la salud', 'industria de alimentos y bebidas', 'comercio',
            'industria de la belleza', 'industria de servicios automotrices',
            'hoteles'))
        
        
    st.write(' ')  
    st.write(' ')  
    st.write(' ')  
    st.write(' ')   
    
    tot1, tot2, tot3 = st.columns((3.5,3,3))

    with tot1:
        st.write(' ')   

    with tot2:
        st.markdown('<p class="big-font2"><br>(generar predicciones del rating  asociado a  estado, ciudad y sector económico determinado).</p>', unsafe_allow_html=True)
        
    with tot3:
        st.write(' ')         
                   
                   
    bot1, bot2, bot3 = st.columns((3.4,1,3))

    with bot1:
        st.write(' ')   

    with bot2:
        dbut =  st.button("**PREDECIR RATING**")  
   
    with bot3:
        st.write(' ')          

    xol1, xol2, xol3 = st.columns((3.35,3,3))
    with xol1:
        st.write(' ')           
    with xol2:        
        if dbut:
           rating = round(get_rating(sector, ciudad_seleccionada, estado_seleccionado),1)
           st.plotly_chart(plot_gauge(rating), use_container_width=True)
           
    with xol3:                
        st.write(' ')             
 
    st.markdown("""<hr style="height:2px;border:none;color:#dfcac9;background-color:#dfcac9;" /> """, unsafe_allow_html=True)
    
    #?--------------------------------------------------------------------------
    st.write(' ') 
    st.write(' ')       
    st.write(' ')       
    valores_unicos_sector,valores_unicos_estado,mejor_sector_por_estado,mejor_ciudad_por_estado_sector = obtener_ciudad_recomendada()
    st.markdown("<h5 style='text-align: center; color: #555750;'>...RECOMIENDA MEJOR LUGAR EN BASE AL RATING, ASOCIADO A ESTADO Y SECTOR ECONOMICO</h5>", unsafe_allow_html=True)
    st.write(' ')  
    st.write(' ')  
    st.write(' ')  

    col1_2, col2_2, col3_2 = st.columns(3)

    with col1_2:
        estado_seleccionado = st.selectbox(
            'ESTADO',
            valores_unicos_estado)

    with col2_2:
        if estado_seleccionado != "Recomendar":
            sector_seleccionado = st.selectbox(
                'SECTOR ECONÓMICO',
                valores_unicos_sector)
        else:
            sector_seleccionado = "Recomendar"

    with col3_2:
        if estado_seleccionado == "Recomendar":
            st.write(' ') 
            st.write(' ')                 
            st.write("Seleccione un estado y sector económico para obtener una recomendación.")
        elif sector_seleccionado == "Recomendar":
            st.write(' ') 
            st.write(' ')                 
            st.write("Seleccione un sector económico para obtener una recomendación.")
        else:
            mejor_ciudad = mejor_ciudad_por_estado_sector.loc[(estado_seleccionado, sector_seleccionado)]
            st.write(' ') 
            st.write(' ')     
            st.write(">🢒Mejor sitio para el estado '{}' y el sector económico '{}': {}".format(estado_seleccionado, sector_seleccionado, mejor_ciudad))
        
        
    st.write(' ')  
    st.write(' ')  
    st.write(' ')  
    st.write(' ')   
    
    tot1_2, tot2_2, tot3_2 = st.columns((3.5,3,3))

    with tot1_2:
        st.write(' ')   

    with tot2_2:
        st.markdown('<p class="big-font2"><br>(genera recomendaciones de lugar usando un estado y sector economico como referencia, se evalua por rating).</p>', unsafe_allow_html=True)
        
    with tot3_2:
        st.write(' ')         
                   
                   

        

def rpage_3():   
    
    tot1_2, tot2_2, tot3_2 = st.columns((1.3,3,3))

    with tot1_2:
        st.write(' ')   

    with tot2_2:
        st.markdown("""
        <iframe width="1200" height="720" src="https://app.powerbi.com/view?r=eyJrIjoiZjRjMjQxZjMtZTE5OC00NTZmLWI5MWItMjViZTU2YjNiYWNlIiwidCI6ImY1ODQzMWRmLTMyNDUtNGIyMi04NjQ1LTVmZmY5ODc0NjY3MiIsImMiOjR9" frameborder="0" style="border:0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
            
    with tot3_2:
        st.write(' ')          

        

b1, b2, b3, b4 , b5 = st.columns((6.1,0.7,0.7,0.7,6))


     
with b1:
    st.write(' ')
with b2:
    if st.button("**INICIO**", type="primary"):
          st.session_state.page_1 = 1
          st.session_state.page_2 = 0
          st.session_state.page_3 = 0          
with b3:
    if st.button("**DASHBOARD**", type="primary"):
          st.session_state.page_1 = 0
          st.session_state.page_2 = 0
          st.session_state.page_3 = 1 
with b4:
    if st.button("**GITHUB**", type="primary"):
          webbrowser.open_new_tab("https://github.com/rulomak/PF_google_Yelp")
with b4:
    st.write(' ')                                
# st.button("Another button!")
st.markdown("""<hr style="height:2px;border:none;color:#dfcac9;background-color:#dfcac9;" /> """, unsafe_allow_html=True)







if   st.session_state.page_1 == 1:
    rpage_1()
    
elif st.session_state.page_2 == 1:
    rpage_2()      
    
elif st.session_state.page_3 == 1:
    rpage_3()        
    
    
    
