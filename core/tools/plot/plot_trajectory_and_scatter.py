import pandas as pd
import plotly.graph_objs as go
import json


def plot_trajectory_and_scatter(
        trajectory_input_file: str,
        scatter_input_file: str,
        output_file: str,
        existing_map_file: str = None):
    """
    This function plots the trajectories and scatter points on a plotly map, with different colors
    for each unique 'uid' in the data. If 'uid' column is not present, it plots all data
    as a single trajectory and a single set of scatter points.
    If existing_map_file is provided, it loads the existing map and adds the new trajectories.(else is None)

    Parameters
    ----------
    trajectory_input_file : str
        The trajectory data file path to be processed.
    scatter_input_file : str
        The scatter points data file path to be processed.
    output_file : str
        The output graph file path (a json file).
    existing_map_file : str, optional
        The path to an existing map file to update with new trajectory and scatter points (default is None).
    """
    tdf = pd.read_csv(trajectory_input_file)
    sdf = pd.read_csv(scatter_input_file)
    traces = []

    # Check if 'uid' column exists in the trajectory DataFrame
    if 'uid' in tdf.columns:
        # Group the DataFrame by 'uid'
        grouped = tdf.groupby('uid')

        # Loop through each group and create a Scattermapbox trace for the trajectory
        for uid, group in grouped:
            trajectory_lon = group['lng']
            trajectory_lat = group['lat']

            trajectory_trace = go.Scattermapbox(
                lon=trajectory_lon,
                lat=trajectory_lat,
                mode='lines',
                line=dict(width=3),
                name=f"Trajectory UID: {uid}"
            )
            traces.append(trajectory_trace)
    else:
        # If 'uid' column does not exist, plot all data as a single trajectory
        trajectory_lon = tdf['lng']
        trajectory_lat = tdf['lat']
        trajectory_trace = go.Scattermapbox(
            lon=trajectory_lon,
            lat=trajectory_lat,
            mode='lines',
            line=dict(width=3, color='blue'),
            name='Trajectory'
        )
        traces.append(trajectory_trace)

    # Check if 'uid' column exists in the scatter DataFrame
    if 'uid' in sdf.columns:
        # Group the DataFrame by 'uid'
        grouped = sdf.groupby('uid')

        # Loop through each group and create a Scattermapbox trace for the scatter points
        for uid, group in grouped:
            scatter_lon = group['lng']
            scatter_lat = group['lat']

            scatter_trace = go.Scattermapbox(
                lon=scatter_lon,
                lat=scatter_lat,
                mode='markers',
                marker=dict(size=9),
                name=f"Scatter UID: {uid}"
            )
            traces.append(scatter_trace)
    else:
        # If 'uid' column does not exist, plot all data as a single set of scatter points
        scatter_lon = sdf['lng']
        scatter_lat = sdf['lat']
        scatter_trace = go.Scattermapbox(
            lon=scatter_lon,
            lat=scatter_lat,
            mode='markers',
            marker=dict(size=9, color='red'),
            name='Scatter Points'
        )
        traces.append(scatter_trace)

    # If an existing map file is provided, load it and add the new traces
    if existing_map_file:
        with open(existing_map_file, 'r') as f:
            existing_map_data = json.load(f)
        fig = go.Figure(data=existing_map_data['data'] + traces, layout=existing_map_data['layout'])
    else:
        # Define the center of the map
        center_lat = (tdf['lat'].mean() + sdf['lat'].mean()) / 2
        center_lon = (tdf['lng'].mean() + sdf['lng'].mean()) / 2

        # Define layout with Mapbox settings
        layout = go.Layout(
            title='Trajectory and Scatter Plot with Mapbox',
            mapbox=dict(
                style="open-street-map",
                bearing=0,
                center=dict(
                    lat=center_lat,
                    lon=center_lon
                ),
                pitch=0,
                zoom=10
            ),
            autosize=True,
            showlegend=True
        )
        fig = go.Figure(data=traces, layout=layout)

    # Write the figure to a JSON file
    fig.write_json(output_file)

# Example usage:
# plot_trajectory_and_scatter('trajectory_data.csv', 'scatter_data.csv', 'output_data.json')
