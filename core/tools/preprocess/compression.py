from skmob.preprocessing import compression as comp
from ..utils import file_utils as fu

def compression(
        input_file: str,
        output_file: str,
        radius: float=0.2
) -> int:
    """
    This function compress the consecutive points.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.
    radius : float, optional
        The minimum distance(km) between consecutive points of the compressed trajectory.
    
    Returns
    -------
    int
        The number of compressed points.
    """
    tdf = fu.load_tdf(input_file)
    ctdf = comp.compress(tdf, spatial_radius_km=radius)
    fu.save_csv(ctdf, output_file)
    return len(ctdf)
