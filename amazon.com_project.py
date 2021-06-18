from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import dash
import pandas as pd
import numpy as np

import time
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options









app.layout = html.Div(children=[
    html.H1(children='amazon cart'),

    

    
   dcc.Input(
    id = "input_x",
    value = 0,
    placeholder = "Please enter product"),

  

    html.Button(
    "Submit",
    id = "submit",
    n_clicks = 0 ),

   html.Div(id = "result")

])




@app.callback(
  Output("result","children"),
  Input("submit","n_clicks"),
  Input("input_x","value")
  )


def update_result(submit,input_x):
  
  changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
  if "submit" in changed_id:
    driver = webdriver.Chrome('chromedriver')
    driver.get("https://www.amazon.com/")
    time.sleep(3) # open a new chrome page
    search_bar = driver.find_element_by_name("field-keywords")
    time.sleep(3)# search where is located the search bar from google
    search_bar.send_keys(input_x)
    time.sleep(3)# write "getting started with python" on google
    search_bar.send_keys(Keys.RETURN) 
    try:
        main = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "a-page"))
        )
        header1 = main.find_elements_by_class_name("sg-col-inner")
        for header2 in header1:
            header3 = header2.find_elements_by_tag_name("h2")
            for header in header3:
                header.click()
                break
            main1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "a-page"))
            )
            if (main1!=main):
                break


        add2cart = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-button"))
        )
        add2cart.click()

    finally:
        print("suces")

  


if __name__ == '__main__':
    app.run_server(debug=True)