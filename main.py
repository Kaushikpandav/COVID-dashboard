# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# import dash
# from dash import html
# from dash import dcc
# from dash.dependencies import Input, Output
# import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt

# external_stylesheets = [
#     {
#         'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
#         'rel': 'stylesheet',
#         'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
#         'crossorigin': 'anonymous'
#     }
# ]

# patients = pd.read_csv('IndividualDetails.csv')

# total = patients.shape[0]
# active = patients[patients['current_status'] == 'Hospitalized'].shape[0]
# recovered = patients[patients['current_status'] == 'Recovered'].shape[0]
# deceased = patients[patients['current_status'] == 'Deceased'].shape[0]
# migrated = patients[patients['current_status'] == 'Migrated'].shape[0]
# detected_city = patients['detected_city'].shape[0]
# detected_district = patients['detected_district'].shape[0]
# detected_state = patients['detected_state'].shape[0]
# current_status = patients['current_status'].shape[0]

# options = [
#     {'label': 'All', 'value': 'All'},
#     {'label': 'Hospitalized', 'value': 'Hospitalized'},
#     {'label': 'Recovered', 'value': 'Recovered'},
#     {'label': 'Deceased', 'value': 'Deceased'}
# ]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server

# app.layout = html.Div([
#     html.Div([], className='row mt-3'),
#     html.H1("Corona Virus Dashboard", style={'text-align': 'center', 'padding': '1px'}),
#     html.Div([], className='row mt-3'),

#     html.Div([
#         html.Div([
#             html.Div([
#                 html.Div([
#                     html.H3("Total Cases", className='text-light'),
#                     html.H4(total, className='text-light')
#                 ], className='card-body')
#             ], className='card bg-primary mb-4')
#         ], className='col-md-3'),

#         html.Div([
#             html.Div([
#                 html.Div([
#                     html.H3("Active", className='text-light'),
#                     html.H4(active, className='text-light')
#                 ], className='card-body')
#             ], className='card bg-info mb-4')
#         ], className='col-md-3'),

#         html.Div([
#             html.Div([
#                 html.Div([
#                     html.H3("Recovered", className='text-light'),
#                     html.H4(recovered, className='text-light')
#                 ], className='card-body')
#             ], className='card bg-success mb-4')
#         ], className='col-md-3'),

#         html.Div([
#             html.Div([
#                 html.Div([
#                     html.H3("Deaths", className='text-light'),
#                     html.H4(deceased, className='text-light')
#                 ], className='card-body')
#             ], className='card bg-warning mb-4')
#         ], className='col-md-3')
#     ], className='row'),

#     html.Div([
#         html.Div([
#             html.Div([
#                 html.H1("State Total Counts", style={'text-align': 'center'}),
#                 dcc.Dropdown(id='picker', options=options, value='All'),
#                 dcc.Graph(id='bar')
#             ], className='card-body p-4')
#         ], className='card col-md-12')
#     ], className='row mt-4'),

#     html.Div([
#         html.Div([
#             html.Div([
#                 html.H1("City Total Counts", style={'text-align': 'center'}),
#                 dcc.Graph(id='bar-city')
#             ], className='card-body p-4')
#         ], className='card col-md-12')
#     ], className='row mt-4'),

#     html.Div([
#         html.Div([
#             html.Div([
#                 html.H1("District Total Counts", style={'text-align': 'center'}),
#                 dcc.Graph(id='bar-district')
#             ], className='card-body p-4')
#         ], className='card col-md-12')
#     ], className='row mt-4'),
    
#     html.Div([
#         html.Div([
#             html.Div([
#                 html.H1("State Total Counts", style={'text-align': 'center'}),
#                 dcc.Graph(id='bar-state')
#             ], className='card-body p-4')
#         ], className='card col-md-12')
#     ], className='row mt-4'),
    
#     html.Div([
#         html.Div([
#             html.Div([
#                 html.H1("Age Distribution", style={'text-align': 'center'}),
#                 dcc.Graph(id="pie-chart")
#             ], className='card-body p-4')
#         ], className='card col-md-12')
#     ], className='row mt-4'),

#     html.Div([
#         html.Div([
#             html.Div([
#                 html.H1("Gender Distribution", style={'text-align': 'center'}),
#                 dcc.Graph(id="gender-pie-chart")
#             ], className='card-body p-4')
#         ], className='card col-md-12')
#     ], className='row mt-4'),
    
#     html.Div([
#         html.Div([
#             html.Div([
#                 html.H1("Current Status Distribution", style={'text-align': 'center'}),
#                 dcc.Graph(id="current-status-pie-chart")
#             ], className='card-body p-4')
#         ], className='card col-md-12')
#     ], className='row mt-4'),

    
# ], className='container')

# @app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
# def update_graph(status):
#     if status == 'All':
#         pbar = patients['detected_state'].value_counts().reset_index()
#     else:
#         npat = patients[patients['current_status'] == status]
#         pbar = npat['detected_state'].value_counts().reset_index()
#     pbar.columns = ['detected_state', 'count']

#     return {
#         'data': [go.Bar(x=pbar['detected_state'], y=pbar['count'])]
#     }

# @app.callback(
#     Output("pie-chart", "figure"),
#     [Input("pie-chart", "id")]
# )
# def generate_chart(id):
#     age_distribution = [
#         {"Age Group": "0-9", "Percentage": 3.8},
#         {"Age Group": "10-19", "Percentage": 21.1},
#         {"Age Group": "20-29", "Percentage": 24.9},
#         {"Age Group": "30-39", "Percentage": 20.3},
#         {"Age Group": "40-49", "Percentage": 15.6},
#         {"Age Group": "50-59", "Percentage": 8.5},
#         {"Age Group": "60-69", "Percentage": 4.2},
#         {"Age Group": "70-79", "Percentage": 1.5},
#         {"Age Group": ">80", "Percentage": 0.5},
#         {"Age Group": "Missing", "Percentage": 0.5},
#     ]
    
#     fig = px.pie(age_distribution, names="Age Group", values="Percentage")
#     return fig

# @app.callback(Output('bar-city', 'figure'), [Input('bar-city', 'id')])
# def update_city_graph(id):
#     pbar = patients['detected_city'].value_counts().reset_index()
#     pbar.columns = ['detected_city', 'count']

#     # return {
#     #     'data': [go.Bar(x=pbar['detected_city'], y=pbar['count'])]
#     # }
    
#     fig = go.Figure(pbar=[go.Histogram(x=pbar)])
    
#     # fig = px.histogram(pbar, x='detected_city', y='count', nbins=len(pbar))
#     # fig.update_layout(xaxis_title='City', yaxis_title='Count')
    
#     return fig

# @app.callback(Output('bar-district', 'figure'), [Input('bar-district', 'id')])
# def update_district_graph(id):
#     pbar = patients['detected_district'].value_counts().reset_index()
#     pbar.columns = ['detected_district', 'count']

#     # return {
#     #     'data': [go.Bar(x=pbar['detected_district'], y=pbar['count'])]
#     # }
    
#     fig = go.Figure(pbar=[go.Histogram(x=pbar)])

#     # fig = px.histogram(pbar, x='detected_district', y='count', nbins=len(pbar))
#     # fig.update_layout(xaxis_title='Distict', yaxis_title='Count')
    
#     return fig

# @app.callback(Output('bar-state', 'figure'), [Input('bar-state', 'id')])
# def update_state_graph(id):
#     pbar = patients['detected_state'].value_counts().reset_index()
#     pbar.columns = ['detected_state', 'count']

#     # return {
#     #     'data': [go.Bar(x=pbar['detected_state'], y=pbar['count'])]
#     # }
    
#     fig = px.histogram(pbar, x='detected_state', y='count', nbins=len(pbar))
#     fig.update_layout(xaxis_title='State', yaxis_title='Count')
    
#     return fig

# @app.callback(
#     Output("gender-pie-chart", "figure"),
#     [Input("gender-pie-chart", "id")]
# )
# def generate_gender_chart(id):
#     gender_distribution = patients['gender'].value_counts().reset_index()
#     gender_distribution.columns = ['Gender', 'Count']

#     fig = go.Figure(data=go.Scatter(x=gender_distribution['Gender'], y=gender_distribution['Count'], mode='markers'))

#     fig.update_layout(
#         xaxis_title='Gender',
#         yaxis_title='Count'
#     )

#     return fig

# @app.callback(
#     Output("current-status-pie-chart", "figure"),
#     [Input("current-status-pie-chart", "id")]
# )
# def current_status_chart(id):
#     pbar = patients['current_status'].value_counts().reset_index()
#     pbar.columns = ['current_status', 'Count']
    
#     return {
#         'data': [go.Bar(x=pbar['detected_city'], y=pbar['count'], xaxis=1)]
#     }

#     fig = px.pie(current_status, names='current_status', values='Count')
#     return fig
    
#     # fig = px.histogram(pbar, x='current_status', y='count', nbins=len(pbar))
#     # fig.update_layout(xaxis_title='Current Status', yaxis_title='Count')
    
#     # return fig
    
# # if __name__ == "__main__":
# #     port = int(os.environ.get("PORT", 8050))
# #     app.run_server(host="0.0.0.0", port=port, debug=True, use_reloader=False)
    
# if __name__ == "__main__":
#     app.run_server(debug=True, use_reloader=False)
    
    
    
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

patients = pd.read_csv('IndividualDetails.csv')


total = patients.shape[0]
active = patients[patients['current_status'] == 'Hospitalized'].shape[0]
recovered = patients[patients['current_status'] == 'Recovered'].shape[0]
deceased = patients[patients['current_status'] == 'Deceased'].shape[0]
migrated = patients[patients['current_status'] == 'Migrated'].shape[0]
detected_city = patients['detected_city'].shape[0]
detected_district = patients['detected_district'].shape[0]
detected_state = patients['detected_state'].shape[0]
current_status = patients['current_status'].shape[0]

options = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Div([], className='row mt-3'),
    html.H1("Corona Virus Dashboard", style={'text-align': 'center', 'padding': '1px'}),
    html.Div([], className='row mt-3'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", className='text-light'),
                    html.H4(total, className='text-light')
                ], className='card-body')
            ], className='card bg-primary mb-4')
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active", className='text-light'),
                    html.H4(active, className='text-light')
                ], className='card-body')
            ], className='card bg-info mb-4')
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered", className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-success mb-4')
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Deaths", className='text-light'),
                    html.H4(deceased, className='text-light')
                ], className='card-body')
            ], className='card bg-warning mb-4')
        ], className='col-md-3')
    ], className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.H1("State Total Counts", style={'text-align': 'center'}),
                dcc.Dropdown(id='picker', options=options, value='All'),
                dcc.Graph(id='bar')
            ], className='card-body p-4')
        ], className='card col-md-12')
    ], className='row mt-4'),

    html.Div([
        html.Div([
            html.Div([
                html.H1("City Total Counts", style={'text-align': 'center'}),
                dcc.Graph(id='bar-city')
            ], className='card-body p-4')
        ], className='card col-md-12')
    ], className='row mt-4'),

    html.Div([
        html.Div([
            html.Div([
                html.H1("District Total Counts", style={'text-align': 'center'}),
                dcc.Graph(id='bar-district')
            ], className='card-body p-4')
        ], className='card col-md-12')
    ], className='row mt-4'),
    
    html.Div([
        html.Div([
            html.Div([
                html.H1("State Total Counts", style={'text-align': 'center'}),
                dcc.Graph(id='bar-state')
            ], className='card-body p-4')
        ], className='card col-md-12')
    ], className='row mt-4'),
    
    html.Div([
        html.Div([
            html.Div([
                html.H1("Age Distribution", style={'text-align': 'center'}),
                dcc.Graph(id="pie-chart")
            ], className='card-body p-4')
        ], className='card col-md-12')
    ], className='row mt-4'),

    html.Div([
        html.Div([
            html.Div([
                html.H1("Gender Distribution", style={'text-align': 'center'}),
                dcc.Graph(id="gender-pie-chart")
            ], className='card-body p-4')
        ], className='card col-md-12')
    ], className='row mt-4'),
    
    html.Div([
        html.Div([
            html.Div([
                html.H1("Current Status Distribution", style={'text-align': 'center'}),
                dcc.Graph(id="current-status-pie-chart")
            ], className='card-body p-4')
        ], className='card col-md-12')
    ], className='row mt-4'),

    
], className='container')

@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_graph(status):
    if status == 'All':
        pbar = patients['detected_state'].value_counts().reset_index()
    else:
        npat = patients[patients['current_status'] == status]
        pbar = npat['detected_state'].value_counts().reset_index()
    pbar.columns = ['detected_state', 'count']

    return {
        'data': [go.Bar(x=pbar['detected_state'], y=pbar['count'])]
    }

@app.callback(
    Output("pie-chart", "figure"),
    [Input("pie-chart", "id")]
)
def generate_chart(id):
    age_distribution = [
        {"Age Group": "0-9", "Percentage": 3.8},
        {"Age Group": "10-19", "Percentage": 21.1},
        {"Age Group": "20-29", "Percentage": 24.9},
        {"Age Group": "30-39", "Percentage": 20.3},
        {"Age Group": "40-49", "Percentage": 15.6},
        {"Age Group": "50-59", "Percentage": 8.5},
        {"Age Group": "60-69", "Percentage": 4.2},
        {"Age Group": "70-79", "Percentage": 1.5},
        {"Age Group": ">80", "Percentage": 0.5},
        {"Age Group": "Missing", "Percentage": 0.5},
    ]
    
    fig = px.pie(age_distribution, names="Age Group", values="Percentage")
    return fig

@app.callback(Output('bar-city', 'figure'), [Input('bar-city', 'id')])
def update_city_graph(id):
    pbar = patients['detected_city'].value_counts().reset_index()
    pbar.columns = ['detected_city', 'count']

    return {
        'data': [go.Bar(x=pbar['detected_city'], y=pbar['count'])]
    }

@app.callback(Output('bar-district', 'figure'), [Input('bar-district', 'id')])
def update_district_graph(id):
    pbar = patients['detected_district'].value_counts().reset_index()
    pbar.columns = ['detected_district', 'count']

    return {
        'data': [go.Bar(x=pbar['detected_district'], y=pbar['count'])]
    }
    

@app.callback(Output('bar-state', 'figure'), [Input('bar-state', 'id')])
def update_state_graph(id):
    pbar = patients['detected_state'].value_counts().reset_index()
    pbar.columns = ['detected_state', 'count']

    return {
        'data': [go.Bar(x=pbar['detected_state'], y=pbar['count'])]
    }

@app.callback(
    Output("gender-pie-chart", "figure"),
    [Input("gender-pie-chart", "id")]
)
def generate_gender_chart(id):
    gender_distribution = patients['gender'].value_counts().reset_index()
    gender_distribution.columns = ['Gender', 'Count']

    fig = px.pie(gender_distribution, names='Gender', values='Count')
    return fig

@app.callback(
    Output("current-status-pie-chart", "figure"),
    [Input("current-status-pie-chart", "id")]
)
def current_status_chart(id):
    current_status = patients['current_status'].value_counts().reset_index()
    current_status.columns = ['current_status', 'Count']

    # fig = px.pie(current_status, names='current_status', values='Count')
    # return fig
    
    fig = go.Figure(data=go.Scatter(x=current_status['current_status'], y=current_status['Count'], mode='markers'))

    fig.update_layout(
        xaxis_title='Current status',
        yaxis_title='Count'
    )

    return fig
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port, debug=True, use_reloader=False)

# if __name__ == "__main__":
#     app.run_server(debug=True, use_reloader=False)

    
    
    
    
    
    



# import seaborn as sns
import matplotlib.pyplot as plt

# # Load the dataset
# tips = sns.load_dataset('tips')

# # 1. Histogram (displot)
# sns.displot(tips['total_bill'], kde=True)
# plt.title('Histogram')
# plt.show()

# # 2. KDE Plot (kdeplot)
# sns.kdeplot(tips['total_bill'], shade=True)
# plt.title('KDE Plot')
# plt.show()

# # 3. Scatter Plot (scatterplot)
# sns.scatterplot(x='total_bill', y='tip', data=tips)
# plt.title('Scatter Plot')
# plt.show()

# # 4. Line Plot (lineplot)
# sns.lineplot(x='size', y='total_bill', data=tips)
# plt.title('Line Plot')
# plt.show()

# # 5. Box Plot (boxplot)
# sns.boxplot(x='day', y='total_bill', data=tips)
# plt.title('Box Plot')
# plt.show()

# # 6. Violin Plot (violinplot)
# sns.violinplot(x='day', y='total_bill', data=tips)
# plt.title('Violin Plot')
# plt.show()

# # 7. Bar Plot (barplot)
# sns.barplot(x='day', y='total_bill', data=tips)
# plt.title('Bar Plot')
# plt.show()

# # 8. Count Plot (countplot)
# sns.countplot(x='day', data=tips)
# plt.title('Count Plot')
# plt.show()

# # 9. Heatmap (heatmap)
# corr = tips.corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Heatmap')
# plt.show()

# # 10. Pair Plot (pairplot)
# sns.pairplot(tips)
# plt.title('Pair Plot')
# plt.show()
