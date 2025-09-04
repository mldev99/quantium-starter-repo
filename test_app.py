import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Fixture to start Dash app with ChromeDriver
@pytest.fixture
def dash_app(dash_duo):
    app = import_app("app")  # Replace "app" with your Dash app filename if different
    # Setup Chrome driver automatically
    driver = webdriver.Chrome(ChromeDriverManager().install())
    dash_duo.start_server(app, driver=driver)
    return dash_duo

# Test that header is present
def test_header_present(dash_app):
    dash_app.wait_for_text_to_equal("#header", "Pink Morsel Sales Visualiser")
    assert dash_app.find_element("#header").text == "Pink Morsel Sales Visualiser"

# Test that line chart is present
def test_graph_present(dash_app):
    dash_app.wait_for_element("#sales-graph")  # Replace with your graph's id
    graph = dash_app.find_element("#sales-graph")
    assert graph is not None

# Test that region picker is present
def test_region_picker_present(dash_app):
    dash_app.wait_for_element("#region-picker")  # Replace with your radio id
    picker = dash_app.find_element("#region-picker")
    assert picker is not None
