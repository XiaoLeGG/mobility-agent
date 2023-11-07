from skmob.measures.individual import frequency_rank as fr
from skmob.measures.individual import location_frequency as lf
from ..utils import file_utils as fu


def frequency_rank(
        input_file: str,
        output_file: str,
):
    """
    Compute the frequency rank of the location of a set of individuals in a TrajDataFrame. The frequency rank K_f(r_i) of a location r_i of an individual u is K_f(r_i)=1 if location r_i is the most visited location, it is K_f(r_i)=2 if r_i is the second-most visited location, and so on.

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A 4-dimension numpy array indicating the result table with individual id, location (latitude and longitude) and the frequency rank for each location of the individuals
    """
    tdf = fu.load_tdf(input_file)
    fr_df = fr(tdf, False)
    fu.save_csv(fr_df, output_file)
    return fr_df.to_numpy()


def location_frequency(
        input_file: str,
        output_file: str,
):
    """
    Compute the visitation frequency of each location, for a set of individuals in a TrajDataFrame.  Given an individual `u`, the visitation frequency of a location r_i is the number of visits to that location by `u`.  The higher the value, the more frequently u is located at r_i.

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A 4-dimension numpy array indicating the result table with individual id, location (latitude and longitude) and the location frequency  for each location of the individuals.
    """
    tdf = fu.load_tdf(input_file)
    lf_df = lf(tdf, False, False, False)
    fu.save_csv(lf_df, output_file)
    return lf_df.to_numpy()
