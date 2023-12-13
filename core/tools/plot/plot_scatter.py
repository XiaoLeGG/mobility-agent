import plotly.graph_objs as go
import pandas as pd

def plot_scatter(input_file: str, output_file: str):
    """
    This function plots the scatter points on a plotly map, with different points
    for each unique 'uid' in the data. If 'uid' column is not present, it plots all data
    as a single set of points.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The output graph file path (a json file).
    """
    tdf = pd.read_csv(input_file)

    # Check if 'uid' column exists in the DataFrame
    if 'uid' in tdf.columns:
        # Group the DataFrame by 'uid' if 'uid' column exists
        grouped = tdf.groupby('uid')
        traces = []

        # Loop through each group and create a Scattermapbox trace
        for uid, group in grouped:
            lon = group['lng']  # Assuming longitude is stored in 'lng'
            lat = group['lat']  # Assuming latitude is stored in 'lat'

            trace = go.Scattermapbox(
                lon=lon,
                lat=lat,
                mode='markers',
                marker=dict(size=9),
                name=f"UID: {uid}"  # Label each trace with the corresponding 'uid'
            )
            traces.append(trace)
    else:
        # If 'uid' column does not exist, plot all data as a single set of points
        lon = tdf['lng']
        lat = tdf['lat']
        trace = go.Scattermapbox(
            lon=lon,
            lat=lat,
            mode='markers',
            marker=dict(size=9, color='red'),
            name="All Points"
        )
        traces = [trace]

    # Define layout with Mapbox settings
    layout = go.Layout(
        title='Scatter Plot with Mapbox',
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
        autosize=True,
        showlegend=True
    )

    # Create a Figure with data and layout
    fig = go.Figure(data=traces, layout=layout)

    # Write the figure to a JSON file
    fig.write_json(output_file)

# Example usage:
# plot_scatter('input_data.csv', 'output_data.json')
