from skmob.measures.individual import number_of_visits as nv
from skmob.measures.individual import number_of_locations as nl
from ..utils import file_utils as fu


def number_of_visits(
        input_file: str,
        output_file: str,
):
    """
    Compute the number of visits (i.e., data points) for each individual in a TrajDataFrame.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with individual id and the number of visits for this individual.
    """
    tdf = fu.load_tdf(input_file)
    nv_df = nv(tdf, False)
    fu.df_save_csv(nv_df, output_file)
    return nv_df.to_numpy()

def number_of_locations(
        input_file: str,
        output_file: str,
):
    """
    Compute the number of distinct locations visited by a set of individuals in a TrajDataFrame.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with individual id and the number of locations for this individual.
    """
    tdf = fu.load_tdf(input_file)
    nl_df = nl(tdf, False)
    fu.df_save_csv(nl_df, output_file)
    return nl_df.to_numpy()

