import plotly.graph_objs as go
import pandas as pd
import json


def plot_scatter(input_file: str, output_file: str, existing_map_file: str = None):
    """
    This function plots the scatter points on a plotly map, with different points
    for each unique 'uid' in the data.
    If existing_map_file is provided, it loads the existing map and adds the new trajectories.(else is None)
    If 'uid' column is not present, it plots all data as a single set of points.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The output graph file path (a json file).
    existing_map_file : str, optional
        The path to an existing map file to update with new scatter points (default is None).
    """
    tdf = pd.read_csv(input_file)

    # Check if 'uid' column exists in the DataFrame
    if 'uid' in tdf.columns:
        grouped = tdf.groupby('uid')
        traces = []

        for uid, group in grouped:
            trace = go.Scattermapbox(
                lon=group['lng'],
                lat=group['lat'],
                mode='markers',
                marker=dict(size=9),
                name=f"UID: {uid}"
            )
            traces.append(trace)
    else:
        trace = go.Scattermapbox(
            lon=tdf['lng'],
            lat=tdf['lat'],
            mode='markers',
            marker=dict(size=9, color='red'),
            name="All Points"
        )
        traces = [trace]

    # If an existing map file is provided, load it and add the new traces
    if existing_map_file:
        with open(existing_map_file, 'r') as f:
            existing_map_data = json.load(f)
        fig = go.Figure(data=existing_map_data['data'] + traces, layout=existing_map_data['layout'])
    else:
        # Define layout with Mapbox settings
        layout = go.Layout(
            title='Scatter Plot with Mapbox',
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
            autosize=True,
            showlegend=True
        )
        fig = go.Figure(data=traces, layout=layout)

    # Write the figure to a JSON file
    fig.write_json(output_file)
