
# coding: utf-8

# In[9]:

import pandas as pd
import pyproj
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as offline
import operator


# In[3]:

df_2009 = pd.read_csv("2009.csv",error_bad_lines=False,encoding ="'ISO-8859-1')")
df_2010 = pd.read_csv("2010.csv",error_bad_lines=False,encoding ="'ISO-8859-1')")
df_2011 = pd.read_csv("2011.csv",error_bad_lines=False,encoding ="'ISO-8859-1')")
df_2012 = pd.read_csv("2012.csv",error_bad_lines=False,encoding ="'ISO-8859-1')")
df_2013 = pd.read_csv("2013.csv",error_bad_lines=False,encoding ="'ISO-8859-1')")
df_2014 = pd.read_csv("2014.csv",error_bad_lines=False,encoding ="'ISO-8859-1')")
df_2015 = pd.read_csv("2015.csv",error_bad_lines=False,encoding ="'ISO-8859-1')")


# In[4]:
df_2013.columns = ['Reference Number', 'Easting', 'Northing',
       'Number of Vehicles', 'Accident Date', 'Time (24hr)', '1st Road Class',
       'Road Surface', 'Lighting Conditions', 'Weather Conditions',
       'Casualty Class', 'Unnamed: 11', 'Casualty Severity', 'Sex of Casualty',
       'Age of Casualty', 'Type of Vehicle']

df_2013 = df_2013[['Reference Number', 'Easting', 'Northing',
       'Number of Vehicles', 'Accident Date', 'Time (24hr)', '1st Road Class',
       'Road Surface', 'Lighting Conditions', 'Weather Conditions',
       'Casualty Class', 'Casualty Severity', 'Sex of Casualty',
       'Age of Casualty', 'Type of Vehicle']]
df_2014 = df_2014[['Reference Number', 'Grid Ref: Easting', 'Grid Ref: Northing',
       'Number of Vehicles', 'Accident Date', 'Time (24hr)', '1st Road Class',
       'Road Surface', 'Lighting Conditions', 'Weather Conditions',
       'Casualty Class', 'Casualty Severity', 'Sex of Casualty',
       'Age of Casualty', 'Type of Vehicle']]
df_2014.columns = ['Reference Number', 'Easting', 'Northing',
       'Number of Vehicles', 'Accident Date', 'Time (24hr)', '1st Road Class',
       'Road Surface', 'Lighting Conditions', 'Weather Conditions',
       'Casualty Class', 'Casualty Severity', 'Sex of Casualty',
       'Age of Casualty', 'Type of Vehicle']
df_2015.columns = ['Reference Number', 'Easting', 'Northing',
       'Number of Vehicles', 'Accident Date', 'Time (24hr)', '1st Road Class',
       'Road Surface', 'Lighting Conditions', 'Weather Conditions',
       'Casualty Class', 'Casualty Severity', 'Sex of Casualty',
       'Age of Casualty', 'Type of Vehicle']


# In[5]:

df = pd.concat([df_2009,df_2010,df_2011,df_2012,df_2013,df_2015])


# In[6]:



# In[7]:

bng = pyproj.Proj(init='epsg:27700')
wgs84 = pyproj.Proj(init='epsg:4326')
u,v = df.shape
latitude = []
longitude = []
for df_selected in [df_2009,df_2010,df_2011,df_2012,df_2013,df_2014,df_2015]:
    
    for index,row in df_selected.iterrows():
        if pd.notnull(row["Easting"]) and pd.notnull(row["Northing"]):
            lon,lat = pyproj.transform(bng,wgs84, row["Easting"], row["Northing"])
            latitude.append(lat)
            longitude.append(lon)
    df_selected['latitude'] = latitude
    df_selected['longitude'] = longitude
    latitude = []
    longitude = []
    df_selected.drop(["Easting","Northing","Reference Number"], axis=1, inplace=True)
    df_selected.fillna(value = 0,inplace = True)



# In[18]:

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np




# IPython notebook





# In[12]:

def selectYear(year,df_2009=df_2009,df_2010=df_2010,df_2011=df_2011,df_2012=df_2012,df_2013=df_2013,df_2014=df_2014,df_2015=df_2015):
    print(year)
    if year == 2009:
        return df_2009
    elif year == 2010:
        return df_2010
    elif year == 2011:
        return df_2011
    elif year == 2012:
        return df_2012
    elif year == 2013:
        return df_2013
    elif year == 2014:
        return df_2014
    else: 
        return df_2015
def boxAgeSeverityCasultyClass(df_year_selected):
    data = []
    #x = df["Casualty Severity"]
    for i in df_year_selected["Casualty Class"].unique():
        data.append(go.Box(
        x = df_year_selected[df_year_selected["Casualty Class"]==i]["Casualty Severity"],
        y = df_year_selected["Age of Casualty"],
        name = i

        ))


    layout = go.Layout(
        yaxis=dict(
            title='Age of Casualty',
            zeroline=False
        ),
        boxmode='group'
    )
    fig = go.Figure(data=data,layout=layout)

    return fig



# In[54]:


import plotly.plotly as py
from plotly.graph_objs import *


def generateBarChartsOneColumn(df, column, title, xAxis, yAxis):
    
    values_dict = dict(df[column].value_counts())

    sorted_x = sorted(values_dict.items(), key=operator.itemgetter(1),reverse = True)

    x = [ value_df[0] for value_df in sorted_x]
    y = [ value_df[1] for value_df in sorted_x]
    
    data = Bar(x=x, y=y, name=column, marker=dict(color='#ffcdd2'))


    layout = Layout(title=title,
                    xaxis=dict(title=xAxis),
                    yaxis=dict(title=yAxis))
    fig = Figure(data=[data], layout=layout)

    return fig


def generateBarChartsTwoColumn(df, column1, column2, title, xAxis, yAxis):
    data = []
    for value1 in df[column1].unique():
        values_dict = dict((df[df[column1]==value1][column2]).value_counts())
        values_dict = sorted(values_dict.items(), key=operator.itemgetter(0),reverse = True)

        data.append(Bar(
        x = [ value_df[0] for value_df in values_dict] ,
        y = [ value_df[1] for value_df in values_dict],
        name = value1

        ))
        

    layout = Layout(title=title,
                    xaxis=dict(title=xAxis),
                    yaxis=dict(title=yAxis))
    fig = Figure(data=data, layout=layout)
    return fig

    
mapbox_access_token = 'pk.eyJ1IjoiaGF0aW10YWNoaSIsImEiOiJjamZyZTVxNmgxM3JnMzNwbWwyYXBpNG54In0.TVh-dN8wNZS72CwGwEJswg'


def generateMap(df):
    data = []
    color = [ "rgb(255, 0, 0)","rgb(0, 0, 255)","rgb(0, 255, 0)"]
    for index,severity in enumerate(df["Casualty Severity"].unique()):
        print(df[df["Casualty Severity"] == severity]["latitude"],df[df["Casualty Severity"] == severity]["longitude"])
        map_box = Scattermapbox(
            lat=df[df["Casualty Severity"] == severity]["latitude"],
            lon=df[df["Casualty Severity"] == severity]["longitude"],
            mode='markers',
            marker=Marker(
            size=17,
            color=color[index],
            opacity=0.7
            ),
            text="test",
            hoverinfo='text'
)
        
        data.append(map_box)     
    layout = Layout(
        title='Map of accident',
        autosize=True,
        hovermode='closest',
        showlegend=False,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=51,
                lon=-0
            ),
            pitch=0,
            zoom=6,
            style='light'
        ),
    )
    fig = dict(data=data, layout=layout)
    return fig

