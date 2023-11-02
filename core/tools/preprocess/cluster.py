from skmob.preprocessing import clustering
from ..utils import file_utils as fu


def cluster(
        input_file: str,
        output_file: str,
        radius: float = 0.1
) -> int:
    """
    This function cluster the stops of each individual.
    The stops correspond to visits to the same location at different times,
    based on spatial proximity.


    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.
    radius : float, optional
        The parameter `eps` of the function sklearn.cluster.DBSCAN, in kilometers. The default is `0.1`.

    Returns
    -------
    int
        The number of clustered points.
    """
    tdf = fu.load_tdf(input_file)
    ctdf = clustering.cluster(tdf,radius)
    fu.save_csv(ctdf, output_file)
    return len(ctdf)
