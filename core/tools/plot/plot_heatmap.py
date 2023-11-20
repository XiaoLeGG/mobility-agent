import numpy as np
from scipy.stats import gaussian_kde
import plotly.graph_objs as go
import pandas as pd


def plot_heatmap(
        input_file: str,
        output_file: str):
    """
    This function plots the heatmap from a series of trajectories on a plotly map.
    This function calculates the density values from the intensity of points.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The output graph file path(a json file).

    """
    tdf = pd.read_csv(input_file)
    # Extract trajectory longitude and latitude
    lon = tdf['lng'].values  # Assuming longitude is stored in 'lng'
    lat = tdf['lat'].values  # Assuming latitude is stored in 'lat'

    # Calculate the point density
    xy = np.vstack([lon, lat])
    z = gaussian_kde(xy)(xy)

    # Create the base figure
    fig = go.Figure(
        go.Densitymapbox(
            lon=lon,
            lat=lat,
            z=z,
            radius=10  # Adjust the radius as needed
        )
    )

    # Set up the layout with Mapbox details
    fig.update_layout(
        mapbox={
            'style': "open-street-map",
            'center': {'lon': np.mean(lon), 'lat': np.mean(lat)},
            'zoom': 10
        },
        margin={'l': 0, 'r': 0, 't': 0, 'b': 0}
    )
    fig.write_json(output_file)