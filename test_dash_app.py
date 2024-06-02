import pytest
from dash import Dash
from dash.testing.application_runners import import_app

# Import your Dash app
@pytest.fixture
def app():
    app = import_app('app.py')  # Replace 'your_dash_app' with the name of your Dash app file without '.py'
    return app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element('h1')
    assert header.text == 'Pink Morsel Sales Analysis'

def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element('#sales-line-chart')
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element('#region-radio')
    assert region_picker is not None
