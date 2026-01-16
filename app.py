# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': "#1A726C",
    'text': "#AFDDF0"
}

# Load Data
df = pd.read_csv("final_data.csv")
df["date"] = pd.to_datetime(df["date"])

# group sales by date
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
    

    html.Div([
        dcc.RadioItems(
            options=['south', 'east', 'north', 'west', 'all'],
            value='all',
            id='xaxis-type',
            inline=True
        )
    ]),

    dcc.Graph(
        id='example-graph-3',
        figure=fig
    )
])


@callback(
    Output('example-graph-3', 'figure'),
    Input('xaxis-type', 'value')
)
def update_graph(selected_region):
    # Filter regions
    if selected_region != 'all':
        filtered_df = df[df['region'] == selected_region]
    else:
        filtered_df = df
    
    # Group Sales by date
    grouped_df = (
        filtered_df
        .groupby('date', as_index=False)['sales']
        .sum()
    )

    # Create new figure
    fig = px.line(
        grouped_df,
        x='date',
        y='sales',
        title=f'pink morsel sales - {selected_region}'
    )

    # Apply styling
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)