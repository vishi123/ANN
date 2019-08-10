#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

import plotly 
plotly.tools.set_credentials_file(username='vishiGupta', api_key='b8y60TS4wjV1lEbhTDML')

# Importing the dataset
dataset = pd.read_csv('stir.csv')
X = dataset.iloc[:, 0:3].values
y1 = dataset.iloc[:, 3].values
y2 = dataset.iloc[:, 4].values
y1=np.reshape(y1, (-1,1))
y2=np.reshape(y2, (-1,1))
dataset= dataset.drop(axis=1, columns=["Unnamed: 5"])

#scattermatrix
data1 = go.Splom(dimensions=[dict(label='Rotational speed',
                                 values=dataset['Rotational speed(RPM)']),
                            dict(label='Wield speed',
                                 values=dataset['Weilding speed(mm/min)']),
                            dict(label='Axial-load',
                                 values=dataset['Axial load(kN)']),
                            dict(label='Tensile elongation (%)',
                                 values=dataset['Tensile elongation (%)']),
                            dict(label='tensile strength(MPa)',
                                 values=dataset['ultimate tensile strength(MPa)']) ],
                 
                            marker=dict( color='rgb(255, 8, 0)',
                            size=7,
                            showscale=False,
                            line=dict(width=0.5, color='rgb(280,180,230)')))
                
axis = dict(showline=True,
       zeroline=False,
       gridcolor='#fff',
       ticklen=4)

layout = go.Layout(
    title='Friction stir Weilding data set',
    dragmode='select',
    width=1000,
    height=1000,
    autosize=False,
    plot_bgcolor='rgba(240,240,240, 0.95)',
    xaxis1=dict(axis),
    xaxis2=dict(axis),
    xaxis3=dict(axis),
    xaxis4=dict(axis),
    yaxis1=dict(axis),
    yaxis2=dict(axis),
    yaxis3=dict(axis),
    yaxis4=dict(axis))

fig1 = dict(data=[data1], layout=layout)
py.iplot(fig1, filename='FSW1')

#3D plots
data = [go.Scatter3d(
    x=dataset['Rotational speed(RPM)'],
    y=dataset['Weilding speed(mm/min)'],
    z=dataset['ultimate tensile strength(MPa)'],
    mode='markers',
    marker=dict( size=12,
                line=dict(color='rgba(217, 217, 217, 0.14)',width=0.5),
                opacity=0.8 ))]
    
    

layout = go.Layout( margin=dict(l=0, r=0, b=0, t=0))

fig = go.Figure( data=data, layout=layout)
py.iplot(fig, filename='simple-3d-scatter')

data = [go.Scatter3d(
    x=dataset['Rotational speed(RPM)'],
    y=dataset['Weilding speed(mm/min)'],
    z=dataset['Tensile elongation (%)'],
    mode='markers',
    marker=dict( size=12,
                line=dict(color='rgba(217, 217, 217, 0.14)',width=0.5),
                opacity=0.8 ))]
    
layout = go.Layout( margin=dict( l=0, r=0, b=0, t=0 ))

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='simple-3d-scatter2')

#correlation heatmap
corrs = dataset.corr()
figure = ff.create_annotated_heatmap(
    z=corrs.values,
    x=list(corrs.columns),
    y=list(corrs.index),
    annotation_text=corrs.round(2).values,
    showscale=True)
py.iplot(figure, filename='heatmap')


df1=dataset.drop(axis=1, columns=["Axial load(kN)","Tensile elongation (%)"])
df2=dataset.drop(axis=1, columns=["Axial load(kN)", "ultimate tensile strength(MPa)"])



#3D surface plots
#1
data = [go.Surface(x=dataset['Rotational speed(RPM)'],
    y=dataset['Weilding speed(mm/min)'],
    z=df1.values.tolist(), colorscale='Viridis')]

layout = go.Layout(
    width=800,
    height=700,
    autosize=False,
    title='Friction Stir Weilding dataset',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
))

fig = go.Figure( data=data, layout=layout)
py.iplot(fig, filename='simple-3d-surface1')

#2
data = [go.Surface(x=dataset['Rotational speed(RPM)'],
    y=dataset['Weilding speed(mm/min)'],
    z=df2.values.tolist(), colorscale='Viridis')]

layout = go.Layout(
    width=800,
    height=700,
    autosize=False,
    title='Friction Stir Weilding dataset',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True, 
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
))

fig = go.Figure( data=data, layout=layout)
py.iplot(fig, filename='simple-3d-surface2')

