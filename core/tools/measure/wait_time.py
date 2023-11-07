from skmob.measures.individual import waiting_times as wt
from ..utils import file_utils as fu


def wait_time(
        input_file: str,
        output_file: str,
):
    """
    Compute the waiting times (in seconds) between the movements of each individual. The wait time is  defined as the time between two consecutive points.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with individual id and the list record the wait time between every two consecutive points for every individual.
    """
    tdf = fu.load_tdf(input_file)
    wt_df = wt(tdf, False, False)
    fu.save_csv(wt_df, output_file)
    return wt_df.to_numpy()
