import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Завантаження даних про ціну акцій
df = pd.read_csv('stock_prices.csv')

# Ініціалізація Dash додатку
app = dash.Dash(__name__)

# Створення графіка залежності ціни акцій від часу
fig = px.line(df, x='Date', y='Price')

# Додавання компонентів управління
app.layout = html.Div([
    html.H1('Графік ціни акцій'),
    dcc.Graph(id='stock-chart', figure=fig),
    html.Label('Виберіть період часу:'),
    dcc.RangeSlider(
        id='date-slider',
        min=df['Date'].min(),
        max=df['Date'].max(),
        value=[df['Date'].min(), df['Date'].max()],
        marks={str(date): str(date) for date in df['Date'].unique()},
        step=None
    )
])

# Визначення функції зворотного виклику для оновлення графіка на основі вибраного періоду часу
@app.callback(
    Output('stock-chart', 'figure'),
    [Input('date-slider', 'value')]
)
def update_chart(selected_dates):
    filtered_df = df[df['Date'].between(selected_dates[0], selected_dates[1])]
    fig = px.line(filtered_df, x='Date', y='Price')
    return fig

# Запуск додатку
if __name__ == '__main__':
    app.run_server(debug=True)
