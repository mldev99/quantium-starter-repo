import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Load the formatted sales data
df = pd.read_csv("formatted_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Define price increase date for highlight
price_increase_date = pd.to_datetime("2021-01-15")

# Initialize Dash app
app = Dash(__name__)

# Layout with styling
app.layout = html.Div(
    style={"font-family": "Arial, sans-serif", "backgroundColor": "#f0f2f5", "padding": "30px"},
    children=[
        html.H1(
            "Soul Foods Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#2c3e50", "margin-bottom": "30px"}
        ),
        html.Div([
            html.Label("Select Region:", style={"fontWeight": "bold", "fontSize": "18px", "color": "#34495e"}),
            dcc.RadioItems(
                id="region-radio",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"}
                ],
                value="all",
                inline=True,
                labelStyle={"margin-right": "20px", "fontSize": "16px", "color": "#34495e"}
            )
        ], style={"margin-bottom": "20px", "textAlign": "center"}),
        dcc.Graph(id="sales-graph"),
        html.P(
            "Hover over the lines to see sales per date. The vertical line marks the price increase on 15th Jan 2021.",
            style={"textAlign": "center", "color": "#7f8c8d", "margin-top": "20px", "fontSize": "16px"}
        )
    ]
)

# Callback to update graph based on selected region
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-radio", "value")
)
def update_graph(selected_region):
    if selected_region != "all":
        filtered_df = df[df["Region"].str.lower() == selected_region]
    else:
        filtered_df = df

    # Create line chart
    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region" if selected_region == "all" else None,
        labels={"Sales": "Total Sales ($)", "Date": "Date"},
        template="plotly_white"
    )
    
    fig.update_layout(
        title=f"Pink Morsel Sales Over Time ({selected_region.title()})",
        title_x=0.5,
        plot_bgcolor="#ffffff",
        paper_bgcolor="#f0f2f5",
        font=dict(family="Arial", size=14, color="#2c3e50")
    )

    # Add vertical line for price increase
    fig.add_vline(
        x=price_increase_date,
        line_width=3,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top right",
        annotation_font_color="red"
    )

    # Add markers for data points
    fig.update_traces(mode="lines+markers")

    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
