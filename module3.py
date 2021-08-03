#......................................Web Application.................................................#

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from collections import Counter
import unicodedata
import chart_studio.plotly as py
import plotly.graph_objs as go
from random import randint
import threading
import pandas as pd
import os
import base64
import joblib
from tkinter import filedialog
from tkinter import *
import module2

app = dash.Dash()
im2='https://www.logolynx.com/images/logolynx/0c/0c2207cf84a96d91ff696691c3ea08d8.jpeg'
im1='https://www.pngkey.com/png/full/172-1724401_criminal-justice-crime-justice-logo-png.png'
im3='https://thumbs.dreamstime.com/z/india-flag-handcuffed-computer-mouse-combating-crime-hackers-piracy-modern-backlit-creative-concept-139670121.jpg'
im11 ='https://smallimg.pngkey.com/png/small/874-8749433_handcuffs-crime-clip-art-crime-clip-art.png'
im12 ='https://smallimg.pngkey.com/png/small/49-498176_silhouette-theft-criminal-money-crime-gun-man-thief.png'
im13 ='https://smallimg.pngkey.com/png/small/52-527215_dead-clipart-stick-figure-crime-scene-clipart-png.png'
app.layout = html.Div([
    html.H1(children=' INDIAN CRIME PREDICTION AND ANALYSIS USING MACHINE LEARNING TECHNIQUE', style={'marginBottom': '12px'}),
    html.Div(children = [html.Img(src=im1,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im2,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im3,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'})]),
    html.H2(" Select for crime test file  ",style={'marginBottom': '6px'}),    
    html.Button(id='submit-button', n_clicks=0, children='Upload', 
    style={'marginTop': 15, 'marginBottom': 25}),
    html.Div(id='my-div'),
    html.Div(children = [html.Img(src=im13,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im12,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im11,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'})])

], style={'textAlign': 'center',"backgroundColor":"##FFFFFF"})


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')]
)
def update_output_div(n_clicks):
    if n_clicks > 0:
        root = Tk()
        path = 'D:/Final_project(CrimeAnalysis)/Testing'
        root.filename =  filedialog.askopenfilename(initialdir = path,title = "Select file",filetypes = (("crime files","*.csv"),("all files","*.*")))
        print (root.filename)
        root.destroy()
        val = module2.crime_test(root.filename)
        return html.H2(str(val))
if __name__ == '__main__':
    app.run_server()
        
