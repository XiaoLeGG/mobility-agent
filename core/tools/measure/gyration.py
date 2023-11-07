from skmob.measures.individual import k_radius_of_gyration
from skmob.measures.individual import radius_of_gyration
from ..utils import file_utils as fu

def radius_gyration(
        input_file: str,
        output_file: str
):
    """
    This function compute the radius of gyration (in kilometers) of a set of individuals.

    The radius of gyration is a measure used to quantify the spatial dispersion or the spread of an individual's or object's movements over time. It provides an indication of how far an individual typically moves from their center of activity.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with individual id and corresponding gyration.
    
    """
    tdf = fu.load_tdf(input_file)
    rdf = radius_of_gyration(tdf, False)
    fu.save_csv(rdf, output_file)
    return rdf.to_numpy()


def k_radius_gyration(
        input_file: str,
        output_file: str,
        k: int=2
):
    """
    Compute the k-radii of gyration (in kilometers) of a set of individuals.

    In mobility analysis, the k-radius of gyration indicates the characteristic distance travelled by that individual as induced by their k most frequent locations.
    
    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.
    k : int
        The number of most frequent locations to consider. The default is 2. The possible range of values is [2,+inf].

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with indivisual id and corresponding gyration.
    
    """
    tdf = fu.load_tdf(input_file)
    kdf = k_radius_of_gyration(tdf, k, False)
    fu.save_csv(kdf, output_file)
    return kdf.to_numpy()
    