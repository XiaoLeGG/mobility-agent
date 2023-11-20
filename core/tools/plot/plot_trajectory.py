import plotly.graph_objs as go
import pandas as pd


def plot_trajectory(
        input_file: str,
        output_file: str):
    """
    This function plots the trajectories on a plotly map.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The output graph file path(a json file).

    """
    tdf = pd.read_csv(input_file)
    # Extract longitude and latitude from the DataFrame
    lon = tdf['lng']  # Assuming longitude is stored in 'lng'
    lat = tdf['lat']  # Assuming latitude is stored in 'lat'

    # Create a Scattermapbox trace for the trajectory
    trajectory_trace = go.Scattermapbox(
        lon=lon,
        lat=lat,
        mode='lines',
        line=dict(width=3, color='blue'),
    )

    # Define layout with Mapbox settings
    layout = go.Layout(
        mapbox=dict(
            style="open-street-map",
            bearing=0,
            center=dict(
                lat=lat.mean(),
                lon=lon.mean()
            ),
            pitch=0,
            zoom=10
        ),
    )

    # Create a Figure with data and layout
    fig = go.Figure(data=[trajectory_trace], layout=layout)
    fig.write_json(output_file)
