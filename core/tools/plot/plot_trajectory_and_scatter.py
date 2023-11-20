import pandas as pd
import plotly.graph_objs as go


def plot_trajectory_and_scatter(
        trajectory_input_file: str,
        scatter_input_file: str,
        output_file: str):
    """
    This function plots the trajectories and scatter points on a plotly map.

    Parameters
    ----------
    trajectory_input_file : str
        The trajectory data file path to be processed.
    scatter_input_file : str
        The scatter points data file path to be processed.
    output_file : str
        The output graph file path(a json file).
    """
    tdf = pd.read_csv(trajectory_input_file)
    # Extract trajectory longitude and latitude
    trajectory_lon = tdf['lng']  # Assuming longitude is stored in 'lng'
    trajectory_lat = tdf['lat']  # Assuming latitude is stored in 'lat'

    sdf = pd.read_csv(scatter_input_file)
    # Extract scatter points longitude and latitude
    scatter_lon = sdf['lng']  # Assuming longitude is stored in 'lng'
    scatter_lat = sdf['lat']  # Assuming latitude is stored in 'lat'

    # Create a Scattermapbox trace for the trajectory
    trajectory_trace = go.Scattermapbox(
        lon=trajectory_lon,
        lat=trajectory_lat,
        mode='lines',
        line=dict(width=3, color='blue'),
        name='Trajectory'
    )

    # Create a Scattermapbox trace for the scatter points
    scatter_trace = go.Scattermapbox(
        lon=scatter_lon,
        lat=scatter_lat,
        mode='markers',
        marker=dict(size=9, color='red'),
        name='Scatter Points'
    )

    # Define layout with Mapbox settings
    layout = go.Layout(
        title='Trajectory and Scatter Plot with Mapbox',
        mapbox=dict(
            style="open-street-map",
            bearing=0,
            center=dict(
                lat=(trajectory_lat.mean() + scatter_lat.mean()) / 2,
                lon=(trajectory_lon.mean() + scatter_lon.mean()) / 2
            ),
            pitch=0,
            zoom=10
        ),
        autosize=True
    )

    # Create a Figure with data and layout
    fig = go.Figure(data=[trajectory_trace, scatter_trace], layout=layout)
    fig.write_json(output_file)