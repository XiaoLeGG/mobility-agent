import plotly.graph_objs as go
import pandas as pd


def plot_scatter(input_file: str, output_file: str):
    """
        This function plots the scatter points on a plotly map.

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

    # Create a Scattermapbox trace for the points
    points_trace = go.Scattermapbox(
        lon=lon,
        lat=lat,
        mode='markers',
        marker=dict(size=9, color='red'),
    )

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
        autosize=True
    )

    # Create a Figure with data and layout
    fig = go.Figure(data=[points_trace], layout=layout)
    fig.write_json(output_file)


