# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('shipping.csv')

fig = px.scatter(df, x="type", y="Date",
                 size="neto", color="S_City", hover_name="S_Cntry",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='shipping date vs type',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)