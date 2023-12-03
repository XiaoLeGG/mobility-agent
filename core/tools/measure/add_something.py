import movingpandas as mpd
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from ..utils import file_utils as fu


def add_speed(
        input_file: str,
        output_file: str
):
    """
    calculate the speed for each data point

    Warnings: only measure one trajectory one time

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A (n+1)-dimension numpy array indicating the input data and speed for each data point.
    """
    df = fu.load_df(input_file)
    df['geometry'] = df.apply(lambda row: Point(row.lng, row.lat), axis=1)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    gdf = gpd.GeoDataFrame(df, geometry='geometry')
    gdf.crs = "EPSG:4326"
    toy_traj = mpd.Trajectory(gdf, 1)
    toy_traj.add_speed(overwrite=True)
    toy_traj.df.drop('traj_id', axis=1, inplace=True)
    fu.save_csv(toy_traj.df, output_file)
    return toy_traj.df


def add_direction(
        input_file: str,
        output_file: str
):
    """
    calculate the direction for each data point

    Warnings: only measure one trajectory one time

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A (n+1)-dimension numpy array indicating the input data and direction for each data point.
    """
    df = fu.load_df(input_file)
    df['geometry'] = df.apply(lambda row: Point(row.lng, row.lat), axis=1)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    gdf = gpd.GeoDataFrame(df, geometry='geometry')
    gdf.crs = "EPSG:4326"
    toy_traj = mpd.Trajectory(gdf, 1)
    toy_traj.add_direction(overwrite=True)
    toy_traj.df.drop('traj_id', axis=1, inplace=True)
    fu.save_csv(toy_traj.df, output_file)
    return toy_traj.df


def add_acceleration(
        input_file: str,
        output_file: str
):
    """
    calculate the acceleration for each data point

    Warnings: only measure one trajectory one time

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A (n+1)-dimension numpy array indicating the input data and acceleration for each data point.
    """
    df = fu.load_df(input_file)
    df['geometry'] = df.apply(lambda row: Point(row.lng, row.lat), axis=1)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    gdf = gpd.GeoDataFrame(df, geometry='geometry')
    gdf.crs = "EPSG:4326"
    toy_traj = mpd.Trajectory(gdf, 1)
    toy_traj.add_acceleration(overwrite=True)
    toy_traj.df.drop('traj_id', axis=1, inplace=True)
    fu.save_csv(toy_traj.df, output_file)
    return toy_traj.df
