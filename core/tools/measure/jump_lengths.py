from skmob.measures.individual import jump_lengths as jl
from ..utils import file_utils as fu

def jump_lengths(
    input_file : str,
    output_file : str
):
    """
    This function compute the jump lengths (in kilometers) of a set of individuals. A jump length (or trip distance) is defined as the geographic distance between two consecutive points. 

    Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with indivisual id and corresponding list of jump lengths.
    """
    tdf = fu.load_tdf(input_file)
    jldf = jl(tdf, show_progress=False, merge=False)
    fu.df_save_csv(jldf, output_file)
    return jldf.to_numpy()