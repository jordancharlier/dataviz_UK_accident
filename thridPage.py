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
                    id='id_Year_DropDown_Charts_One',
                    options=tls.getListYears(),
                    value=tls.getListYears()[0]['value']
                )],
                style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
                         html.Div([
                html.Label(children='colonne',
                           style={
                               'textAlign': 'center',
                               'color': colors['text']
                           }
                           ),
                dcc.Dropdown(
                    id='id_Column_DropDown_Charts_One',
                    options=tls.getListColumns(),
                    value=tls.getListColumns()[0]['value']
                )],
                style={'width': '33%', 'float': 'right', 'display': 'inline-block'}),
                     html.Div([
                html.Label(children='colonne',
                           style={
                               'textAlign': 'center',
                               'color': colors['text']
                           }
                           ),
                dcc.Dropdown(
                    id='id_Column_DropDown_Charts_Two',
                    options=tls.getListColumns(),
                    value=tls.getListColumns()[0]['value']
                )],
                style={'width': '33%', 'float': 'center', 'display': 'inline-block'}),

                html.Div(id='chart_two',style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
            
                     
                html.Div(id="map_box",style={'width': '100%', 'float': 'left', 'display': 'inline-block'}
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                ),      
                    ])












    
