import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import create_graph as cg
import tools as tls
from dash.dependencies import Input, Output
import firstPage as fp
import secondPage as sp 
import thridPage as tp
app = dash.Dash()


app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True



colors = {
    'background': '#FFFFFF',
    'text': '#0E2F44'
}
app.layout = html.Div([
    dcc.Tabs(
        tabs=[
            {'label': "Relation en âge, position et type de blessure", 'value': 1},
            {'label': "Graphe une colonne", 'value': 2},
            {'label': 'Graphe deux colonnes', 'value': 3}
        ],
        value=1,
        id='tabs'
    ),
    html.Div(id='tab-output')
], style={
    'width': '100%',
    'margin-left': 'auto',
    'margin-right': 'auto',
    'backgroundColor': colors['background'],
    'textAlign': 'center'
})


@app.callback(
    Output('tab-output', 'children'),
    [Input('tabs', 'value')])
def display_content(value):
    if value is 1:
        return fp.page()
    elif value is 2:
        return sp.page()
    elif value is 3:
        return tp.page()


"""
    CallBack de la page First page
"""

@app.callback(
    Output(component_id='box_Year', component_property='children'),
    [Input(component_id='id_Year_DropDown', component_property='value')])

def update_figure_year(year):
    fig = cg.boxAgeSeverityCasultyClass(cg.selectYear(year))
    return html.Div([dcc.Graph(id='box_plot',figure=fig)])



@app.callback(
    Output(component_id='chart_one', component_property='children'),
    [Input(component_id='id_Year_DropDown_Chart_One', component_property='value'),
    Input(component_id='id_Column_DropDown_Chart_One', component_property='value')])

def update_figure_year_column(year,column):
    
    print(year, " YEAR COLUMN", column)
    
    fig2 = cg.generateBarChartsOneColumn(cg.selectYear(year), column, column , column, "counts" )
    print (fig2)
    return html.Div([dcc.Graph(id='chart_One',figure=fig2)])



@app.callback(
    Output(component_id='chart_two', component_property='children'),
    [Input(component_id='id_Year_DropDown_Charts_One', component_property='value'),
    Input(component_id='id_Column_DropDown_Charts_One', component_property='value'),
    Input(component_id='id_Column_DropDown_Charts_Two', component_property='value')])

def update_figure_year_columns(year,column1,column2):
    
    column = column1  + " " + column2
    fig2 = cg.generateBarChartsTwoColumn(cg.selectYear(year), column1, column2 ,column, column, "counts" )
    return html.Div([dcc.Graph(id='chart_Two',figure=fig2)])

@app.callback(
    Output(component_id='map_box', component_property='children'),
    [Input(component_id='id_Year_DropDown_Charts_One', component_property='value')])

def update_figure_map(year):
    fig = cg.generateMap(cg.selectYear(year))
    return html.Div([dcc.Graph(id='mapox',figure=fig)])




if __name__ == '__main__':
    app.run_server()
