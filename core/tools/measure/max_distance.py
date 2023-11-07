from skmob.measures.individual import maximum_distance as md
from skmob.measures.individual import max_distance_from_home as mdfh
from ..utils import file_utils as fu

def max_distance(
        input_file : str,
        output_file : str,
):
    """
    Compute the maximum distance (in kilometers) traveled by a set of individuals. The maximum distance is defined as the maximum distance between two data point for every individual.

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with individual id and the maximum distance for this individual.
    """
    tdf = fu.load_tdf(input_file)
    mddf = md(tdf,False)
    fu.save_csv(mddf, output_file)
    return mddf.to_numpy()


def home_location_from_home(
        input_file: str,
        output_file: str,
        start_night_time: str = '22:00',
        end_night_time: str = '06:00',
):
    """
    Compute the maximum distance (in kilometers) traveled from their home location by a set of individuals in a TrajDataFrame. The most frequency location in nighttime is the location of home.

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.
    start_night_time : str, optional
        The start time of the night. The default is '22:00'.
    end_night_time : str, optional
        The end time of the night. The default is '06:00'.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with individual id and the max distance from home.
    """
    tdf = fu.load_tdf(input_file)
    mdfh_df = mdfh(tdf, start_night_time, end_night_time,False)
    fu.save_csv(mdfh_df, output_file)
    return mdfh_df.to_numpy()