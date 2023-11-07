from skmob.measures.individual import recency_rank as rr
from ..utils import file_utils as fu


def recency_rank(
        input_file: str,
        output_file: str,

):
    """
    Compute the recency rank of the location of a set of individuals. The recency rank K_s(r_i>) of a location r_i of an individual u is K_s(r_i)=1 if location ri is the last visited location, it is K_s(r_i)=2 if r_i is the second-lastvisited location, and so on.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.

    Returns
    -------
    ndarray
        A 4-dimension numpy array indicating the result table with individual id, location (latitude and longitude) and the recency rank for each location of the individuals. (sorted in ascending order )
    """
    tdf = fu.load_tdf(input_file)
    rr_df = rr(tdf, False)
    fu.save_csv(rr_df, output_file)
    return rr_df.to_numpy()
