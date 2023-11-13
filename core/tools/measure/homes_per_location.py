from skmob.measures.collective import homes_per_location as hpl
from ..utils import file_utils as fu


def homes_per_location(
        input_file: str,
        output_file: str,
):
    """
    This function computes the number of home locations in each location. The number of home locations in a location is computed as: N_{homes}(j) = |\{h_u | h_u = j, u \in U \}| where indicates the home location of an individual and is the set of individuals. The result(output file) of this measure is as follows:

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.

    Returns
    -------
    ndarray
        A 3-dimension numpy array indicating the result table with location (latitude and longitude) and the number of homes in this location. (sorted by num_of_homes)
    """
    tdf = fu.load_tdf(input_file)
    hpldf= hpl(tdf)
    fu.save_csv(hpldf, output_file)
    return hpldf.to_numpy()
