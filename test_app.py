from app import app
from dash import html, dcc


def test_header():
    layout_children = app.layout.children
    header = [child for child in layout_children if isinstance(child, html.H1)]
    assert len(header) > 0
    assert header[0].children == 'Sales Data'


def test_graph():
    layout_children = app.layout.children
    graph = [child for child in layout_children if isinstance(child, dcc.Graph)]
    assert len(graph) > 0
    assert graph[0].id == 'sales_graph'


def test_region_buttons():
    layout_children = app.layout.children
    radio_items = [child for child in layout_children if isinstance(child, dcc.RadioItems)]
    assert len(radio_items) > 0
    assert radio_items[0].id == 'region_buttons'
    expected_options = ['south', 'east', 'north', 'west', 'all']
    assert radio_items[0].options == expected_options
    assert radio_items[0].value == 'all'