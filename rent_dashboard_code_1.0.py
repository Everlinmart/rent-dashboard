import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# 1️⃣ Carregar os dados do CSV
file_path = r"C:\Users\everl\Desktop\Projetos Git\Ciencia Dados\Florianópolis\archive\full_history.csv"
df = pd.read_csv(file_path)

# 2️⃣ Remover valores faltantes nas colunas principais
df = df.dropna()

# 3️⃣ Definir colunas disponíveis para seleção
columns = [
    "bairro", "valor_total", "valor", "valor_m2", "valor_condo_m2",
    "area", "qtd_banheiros", "qtd_quartos", "qtd_vagas", "condominio"
]

# 4️⃣ Criar a aplicação Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Análise Interativa de Aluguel por Bairro", style={'textAlign': 'center'}),

    html.Label("Escolha a Coluna X (Categoria):"),
    dcc.Dropdown(
        id='x-axis',
        options=[{'label': col, 'value': col} for col in columns],
        value='bairro',  # Valor padrão
        clearable=False
    ),

    html.Label("Escolha a Coluna Y (Valor):"),
    dcc.Dropdown(
        id='y-axis',
        options=[{'label': col, 'value': col} for col in columns],
        value='valor_total',  # Valor padrão
        clearable=False
    ),

    dcc.Graph(id="graph-output")
])


# 5️⃣ Callback para atualizar o gráfico
@app.callback(
    dash.Output("graph-output", "figure"),
    [dash.Input("x-axis", "value"),
     dash.Input("y-axis", "value")]
)
def update_graph(x_col, y_col):
    if x_col == y_col:
        return px.scatter(title="Erro: Escolha colunas diferentes!")

    # Criar gráfico de barras
    fig = px.bar(df, x=x_col, y=y_col, title=f"{y_col} por {x_col}",
                 labels={x_col: x_col, y_col: y_col}, color=y_col,
                 height=600, color_continuous_scale="bluered")

    return fig


# 6️⃣ Rodar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
