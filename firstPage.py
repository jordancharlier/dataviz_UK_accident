import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import create_graph as cg
import tools as tls
from dash.dependencies import Input, Output

app = dash.Dash()
colors = {
    'background': '#FFFFFF',
    'text': '#0E2F44'
}


def page():
    return html.Div(style={'backgroundColor': colors['background']}, children=[
            html.Div([
                html.Label(children='Année',
                           style={
                               'textAlign': 'center',
                               'color': colors['text']
                           }
                           ),
                dcc.Dropdown(
                    id='id_Year_DropDown',
                    options=tls.getListYears(),
                    value=tls.getListYears()[0]['value']
                )],
                style={'width': '48%', 'float': 'left', 'display': 'inline-block'}),
                        html.Hr(),

                html.Div(id='box_Year',style={'width': '100%', 'float': 'left', 'display': 'inline-block'})
            
        
                    ])











    
