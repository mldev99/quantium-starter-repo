import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the formatted sales data
df = pd.read_csv("formatted_sales.csv")

# Ensure Date is datetime type
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Initialize Dash app
app = Dash(__name__)

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",  # Optional: separates lines per region
    title="Pink Morsel Sales Over Time",
    labels={"Sales": "Total Sales ($)", "Date": "Date"}
)

# Layout
app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=fig),
    html.P(
        "Compare sales before and after the price increase on 15th Jan 2021.",
        style={"textAlign": "center"}
    )
])

# Run the app (latest Dash version)
if __name__ == "__main__":
    app.run(debug=True)

