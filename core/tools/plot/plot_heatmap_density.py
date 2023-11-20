import plotly.graph_objs as go
import pandas as pd



def plot_heatmap_density(
        input_file: str,
        output_file: str):
    """
    This function plots the heatmap from a series of trajectories on a plotly map.
    This function requires the density values to be stored in the input file.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The output graph file path(a json file).

    """
    tdf = pd.read_csv(input_file)
    # Extract trajectory longitude and latitude
    lon = tdf['lng']  # Assuming longitude is stored in 'lng'
    lat = tdf['lat']  # Assuming latitude is stored in 'lat'

    # Create the base figure
    fig = go.Figure(
        go.Densitymapbox(
            lon=lon,
            lat=lat,
            z=tdf['density'],  # Assuming density values are stored in 'density'
            radius=10  # Adjust the radius as needed
        )
    )

    # Set up the layout with Mapbox details
    fig.update_layout(
        mapbox={
            'style': "open-street-map",
            'center': {'lon': lon.mean(), 'lat': lat.mean()},
            'zoom': 10
        },
        margin={'l': 0, 'r': 0, 't': 0, 'b': 0}
    )
    fig.write_json(output_file)