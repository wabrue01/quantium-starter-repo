# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': "#116E67",
    'text': '#7FDBFF'
}

#Load Data
df = pd.read_csv("final_data.csv")
df["date"] = pd.to_datetime(df["date"])

#group sales by date
df_grouped = df.groupby("date", as_index=False)["sales"].sum()

fig = px.line(df, x="date", y="sales", title='Pink Morsel Sales')

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sales Data',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph-3',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)