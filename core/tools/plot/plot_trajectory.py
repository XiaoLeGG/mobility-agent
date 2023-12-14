import plotly.graph_objs as go
import pandas as pd
import json


def plot_trajectory(input_file: str, output_file: str, existing_map_file: str = None):
    """
    This function plots the trajectories on a plotly map, with different trajectories
    for each unique 'uid' in the data.
    If existing_map_file is provided, it loads the existing map and adds the new trajectories.(else is None)
    If 'uid' column is not present, it plots all data
    as a single trajectory.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The output graph file path (a json file).
    existing_map_file : str
        The existing map file path (a json file).
    """
    # Load the CSV data
    tdf = pd.read_csv(input_file)

    # Initialize traces list
    traces = []

    # Check if 'uid' column exists and create traces accordingly
    if 'uid' in tdf.columns:
        grouped = tdf.groupby('uid')
        for uid, group in grouped:
            trace = go.Scattermapbox(
                lon=group['lng'],
                lat=group['lat'],
                mode='lines+markers',
                marker=dict(size=5),
                line=dict(width=3),
                name=f"UID: {uid}",
            )
            traces.append(trace)
    else:
        trace = go.Scattermapbox(
            lon=tdf['lng'],
            lat=tdf['lat'],
            mode='lines+markers',
            marker=dict(size=5),
            line=dict(width=3),
            name="Single Trajectory"
        )
        traces = [trace]

    # Load existing map if provided
    if existing_map_file and existing_map_file != 'null':
        with open(existing_map_file, 'r') as f:
            existing_map_data = json.load(f)
        fig = go.Figure(data=existing_map_data['data'] + traces, layout=existing_map_data['layout'])
    else:
        # Create new map figure with traces
        layout = go.Layout(
            mapbox=dict(
                style="open-street-map",
                bearing=0,
                center=dict(
                    lat=tdf['lat'].mean(),
                    lon=tdf['lng'].mean()
                ),
                pitch=0,
                zoom=10
            ),
            showlegend=True
        )
        fig = go.Figure(data=traces, layout=layout)

    # Save the updated map to the output JSON file
    fig.write_json(output_file)
