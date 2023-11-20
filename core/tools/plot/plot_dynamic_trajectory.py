import pandas as pd
import plotly.graph_objs as go


def plot_dynamic_trajectory(input_file: str,
        output_file: str):
    """
    This function dynamically plots the trajectories on an interactively plotly map.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The output graph file path(a json file).

    """
    tdf = pd.read_csv(input_file)
    # Extract trajectory longitude and latitude
    lon = tdf['lng'].tolist()  # Assuming longitude is stored in 'lng'
    lat = tdf['lat'].tolist()  # Assuming latitude is stored in 'lat'

    # Create the base figure
    fig = go.Figure(
        go.Scattermapbox(
            mode="lines+markers",
            lon=[],
            lat=[],
            marker={'size': 10, 'color': "purple"}
        )
    )

    # Set up the layout with Mapbox details
    fig.update_layout(
        mapbox={
            'style': "open-street-map",
            'center': {'lon': lon[0], 'lat': lat[0]},
            'zoom': 10,
        },
        updatemenus=[{
            'type': 'buttons',
            'buttons': [{
                'label': 'Play',
                'method': 'animate',
                'args': [None, {'frame': {'duration': 10, 'redraw': True}, 'fromcurrent': True}]
            }, {
                'label': 'Pause',
                'method': 'animate',
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate'}]
            }]
        }]
    )

    # Create frames for the animation
    frames = []
    for i in range(1, len(lon) + 1):
        frame = go.Frame(
            data=[go.Scattermapbox(
                mode="lines+markers",
                lon=lon[:i],
                lat=lat[:i]
            )],
            name=f'frame{i}'
        )
        frames.append(frame)

    fig.frames = frames
    fig.write_json(output_file)