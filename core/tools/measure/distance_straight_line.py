from skmob.measures.individual import distance_straight_line as dsl
from ..utils import file_utils as fu


def distance_straight_line(
        input_file: str,
        output_file: str,
):
    """
    Compute the distance (in kilometers) travelled straight line by a set of individuals in a TrajDataFrame. The distance straight d<sub>SL</sub> travelled by an individual `u` is computed as the sum of the distances travelled `u`.

    Warning: The input TrajDataFrame must be sorted in ascending order by datetime.

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A 2-dimension array indicating the result table with individual id and corresponding list of distance straight line.
    """
    tdf = fu.load_tdf(input_file)
    dsl_df = dsl(tdf, False)
    fu.save_csv(dsl_df, output_file)
    return dsl_df.to_numpy()
