#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
#app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': '...........', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': '.........'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("..............."),#May include style for title
    html.Div([#TASK 2.2: Add two dropdown menus
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='...........',
            options=...................,
            value='.................',
            placeholder='.................'
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value='...................'
        )),
    html.Div([#TASK 2.3: Add a division for output display
    html.Div(id='..........', className='..........', style={.........}),])
])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='......', component_property='....'),
    Input(component_id='..........',component_property='....'))

def update_input_container(.......):
    if selected_statistics =='........': 
        return False
    else: 
        return ......

#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='...', component_property='...'),
    [Input(component_id='...', component_property='...'), Input(component_id='...', component_property='...')])


def update_output_container(....., .....):
    if ..... == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
#TASK 2.5: Create and display graphs for Recession Report Statistics

#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('...')['...'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px......(....., 
                x='....',
                y='......',
                title="Average Automobile Sales fluctuation over Recession Period"))

#Plot 2 Calculate the average number of vehicles sold by vehicle type       
        # use groupby to create relevant data for plotting
        average_sales = ...............mean().reset_index()                           
        R_chart2  = dcc.Graph(figure=px....................
        
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
        exp_rec= ....................
        R_chart3 = .............

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        ................
        ...................


        return [
            html.Div(className='..........', children=[html.Div(children=R_chart1),html.Div(children=.....)],style={.....}),
            html.Div(className='chart-item', children=[html.Div(children=...........),html.Div(.............)],style={....})
            ]

# TASK 2.6: Create and display graphs for Yearly Report Statistics
 # Yearly Statistic Report Plots                             
    elif (input_year and selected_statistics=='...............') :
        yearly_data = data[data['Year'] == ......]
                              
#TASK 2.5: Creating Graphs Yearly data
                              
#plot 1 Yearly Automobile sales using line chart for the whole period.
        yas= data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(.................))
            
# Plot 2 Total Monthly Automobile sales using line chart.
        Y_chart2 = dcc.Graph(................)

            # Plot bar chart for average number of vehicles sold during the given year
        avr_vdata=yearly_data.groupby........................
        Y_chart3 = dcc.Graph( figure.................,title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

            # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data=yearly_data.groupby(..................
        Y_chart4 = dcc.Graph(...............)

#TASK 2.6: Returning the graphs for displaying Yearly data
        return [
                html.Div(className='.........', children=[html.Div(....,html.Div(....)],style={...}),
                html.Div(className='.........', children=[html.Div(....),html.Div(....)],style={...})
                ]
        
    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
html.H1(Áutomobile Sales Statistics Dashboard),
style={'textAlign': 'center', 'çolor':'#503D36',
'font-size':24})

  dcc.Dropdown(id='dropdown-statistics', 
                   options=[
                           {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                           {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                           ],
                  placeholder='Select a report type',
                  value='Select Statistics',  
        style={
            'width': '80%',         
            'padding': '3px',       
            'fontSize': '20px',     
            'textAlignLast': 'center'  
        }
  ),
  dcc.Dropdown(
        id='select-year',
        options=[{'label': str(year), 'value': year} for year in year_list],
        placeholder='Select a year',
    ),
   html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
    ]),
 @app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_report):
    if selected_report == 'Yearly Statistics':
        return False
    else:
        return True

 @app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-year', component_property='value'),
     Input(component_id='dropdown-statistics', component_property='value')]
)
def update_output_container(selected_year, selected_report):

    if selected_report == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]
        
    elif selected_report == 'Yearly Statistics':
        yearly_data = data[data['Year'] == selected_year]

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


        # Plot 1: Automobile sales fluctuate over Recession Period (year wise) using line chart
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        chart1 = dcc.Graph(
            figure=px.line(
                yearly_rec,
                x='Year',
                y='Automobile_Sales',
                title="Automobile Sales over Recession Period (Yearly)"
            )
        )

        # Plot 2: Calculate the average number of vehicles sold by vehicle type and represent as a Bar chart
        chart2_data = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        chart2 = dcc.Graph(
            figure=px.bar(
                chart2_data,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title="Average Vehicle Sales by Vehicle Type during Recession"
            )
        )

        # Plot 3: Pie chart for total expenditure share by vehicle type during recessions
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        chart3 = dcc.Graph(
            figure=px.pie(
                exp_rec,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title="Total Expenditure Share by Vehicle Type during Recessions"
            )
        )

        # Plot 4: Develop a Bar chart for the effect of unemployment rate on vehicle type and sales
        chart4_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        chart4 = dcc.Graph(
            figure=px.bar(
                chart4_data,
                x='unemployment_rate',
                y='Automobile_Sales',
                color='Vehicle_Type',
                title="Effect of Unemployment Rate on Vehicle Type and Sales during Recession"
            )
        )
    return chart1, chart2, chart3, chart4

app.layout = html.Div([
    # Dropdowns and input container
    dcc.Dropdown(id='dropdown-statistics', ...),
    dcc.Dropdown(id='select-year', ...),
    # Output container for plots
    html.Div(id='chart1'),
    html.Div(id='chart2'),
    html.Div(id='chart3'),
    html.Div(id='chart4')
])

elif (input_year and selected_statistics == 'Yearly Statistics'):
    yearly_data = data[data['Year'] == input_year]

    # Plot 1: Yearly Automobile sales using a line chart for the whole period.
    yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
    Y_chart1 = dcc.Graph(figure=px.line(
        yas,
        x='Year',
        y='Automobile_Sales',
        title='Yearly Automobile Sales Over the Whole Period'
    ))

    # Plot 2: Total Monthly Automobile sales using a line chart.
    monthly_sales = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
    Y_chart2 = dcc.Graph(figure=px.line(
        monthly_sales,
        x='Month',
        y='Automobile_Sales',
        title='Total Monthly Automobile Sales in the Year {}'.format(input_year)
    ))

    # Plot 3: Bar chart for the average number of vehicles sold during the given year.
    avg_vehicle_data = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
    Y_chart3 = dcc.Graph(figure=px.bar(
        avg_vehicle_data,
        x='Vehicle_Type',
        y='Automobile_Sales',
        title='Average Vehicles Sold by Vehicle Type in the Year {}'.format(input_year)
    ))

    # Plot 4: Total Advertisement Expenditure for each vehicle using a pie chart
    total_advertisement = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
    Y_chart4 = dcc.Graph(figure=px.pie(
        total_advertisement,
        values='Advertising_Expenditure',
        names='Vehicle_Type',
        title='Total Advertisement Expenditure by Vehicle Type in the Year {}'.format(input_year)
    ))

    return [
        html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)],
                 style={'display': 'flex'}),
        html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)],
                 style={'display': 'flex'})
    ]

pip3.8 install setuptools
python3.8 -m pip install packaging
python3.8 -m pip install pandas dash
python3.8 DV0101EN-Final_Assign_Part_2_Questions.py
app.run_server()

python3.8 -m pip install
app.run_server(port=8080)
pip3.8 install setuptools
python3.8 -m pip install packaging
python3.8 -m pip install pandas dash
python3.8 DV0101EN-Final_Assign_Part_2_Questions.py
app.run_server()
app.run_server(port=8080)
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)

python3.8 -m pip install
app.run_server(port=8080)
pip3.8 install setuptools
python3.8 -m pip install packaging
python3.8 -m pip install pandas dash
python3.8 DV0101EN-Final_Assign_Part_2_Questions.py
app.run_server()
app.run_server(port=8080)







       
 
