from skmob.measures.individual import individual_mobility_network as imn
from ..utils import file_utils as fu


def individual_mobility_network(
        input_file: str,
        output_file: str,
):
    """
    Compute the individual mobility network of a set of individuals in a TrajDataFrame. An Individual Mobility Network (aka IMN) of an individual `u` is a directed graph `G_u=(V,E)`, where `V` is the set of nodes and `E` is the set of edges. Nodes indicate locations visisted by `u`, and edges indicate trips between two locations by `u`.  The weight of edges is the number of travel performed by `u` on that edge.

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
        A 5-dimension numpy array indicating the result table with indivisual id, origin_location (latitude and longitude), dest_location (latitude and longitude) and the trip_id.
    """
    tdf = fu.load_tdf(input_file)
    imn_df = imn(tdf, False, False)
    fu.save_csv(imn_df, output_file)
    return imn_df.to_numpy()
