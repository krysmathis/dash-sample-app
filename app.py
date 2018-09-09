# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from stock_reader import get_yahoo_data #local file
from datetime import datetime, timedelta

app = dash.Dash()

colors = {
    'background': 'white',
    'text': 'black'
}

markdown_text="""
# Big Text
## H2
### H3
"""




app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Input(id='input', value='', type='text'),
    
    
    html.Div([
        dcc.Markdown(children=markdown_text)
    ], style={'textAlign': 'center', 'color': colors['text']}),

    html.Div(id='output-graph'),
    
    
])

@app.callback(
        Output(component_id='output-graph', component_property='children'),
        [Input(component_id='input', component_property='value')]
    )

def update_graph(input_data):
    
    _symbols = [input_data]

    start_date = datetime.today() - timedelta(days=720)
    start_date = start_date.strftime('%Y-%m-%d')

    end_date = datetime.today().strftime('%Y-%m-%d')
    end_date
    # df_test = yf.download('AAPL', start_date, end_date, usecols=['Adj Close'])

    df = get_yahoo_data(_symbols, start_date, end_date)

    return dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': df.index, 'y': df[_symbols[0]], 'type': 'line', 'name': _symbols[0]},
                # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'title': "Adj Close for : {}".format(_symbols[0]),
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)