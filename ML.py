import plotly.graph_objects as go
import numpy as np
import pandas as pd
import joblib



def get_rating(state,city,sector_economico):
    loaded_model = joblib.load('linear_regression_model.joblib')
    loaded_column_transformer = joblib.load('column_transformer.joblib')


    datos_prediccion = pd.DataFrame([(sector_economico, city, state)], columns=['sector_economico', 'ciudad', 'state'])


    datos_prediccion_encoded = loaded_column_transformer.transform(datos_prediccion)

    prediccion = loaded_model.predict(datos_prediccion_encoded)
    return prediccion[0]
  



def plot_gauge(value):

    plot_bgcolor = 'rgb(238,20,87,0)'
    quadrant_colors = [plot_bgcolor, "#14eeab", "#14eeab", "#10d99b", "#0ec18a", "#0ca979"] 
    quadrant_text = ["", "<b>5.0</b>", "<b>2.0</b>", "<b>3.0</b>", "<b>2.0</b>", "<b>1.0</b>"]
    n_quadrants = len(quadrant_colors) - 1

    current_value = value
    min_value = 0.0
    max_value = 5.0
    hand_length = np.sqrt(2) / 4
    hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))

    fig = go.Figure(
        data=[
            go.Pie(
                values=[0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist(),
                rotation=90,
                hole=0.5,
                marker_colors=quadrant_colors,
                text=quadrant_text,
                textinfo="text",
                hoverinfo="skip",
            ),
        ],
        layout=go.Layout(
            showlegend=False,
            margin=dict(b=0,t=10,l=10,r=10),
            width=450,
            height=450,
            paper_bgcolor=plot_bgcolor,
            font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
            annotations=[
                go.layout.Annotation(
                    text=f"{current_value} de rating",
                    x=0.5, xanchor="center", xref="paper",
                    y=0.35, yanchor="bottom", yref="paper",
                    showarrow=False,bgcolor = "#555750",
                )
            ],
            shapes=[
                go.layout.Shape(
                    type="circle",
                    x0=0.48, x1=0.52,
                    y0=0.48, y1=0.52,
                    fillcolor="#ffffff",
                    line_color="#ffffff",
                ),
                go.layout.Shape(
                    type="line",
                    x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                    y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                    line=dict(color="#ffffff", width=4)
                )
            ]
        )
    )
    return fig