from skmob.measures.individual import home_location as hl
from ..utils import file_utils as fu

def home_location(
    input_file : str,
    output_file : str,
    start_night_time : str='22:00',
    end_night_time : str='06:00',
):
    """
    
    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.
    start_night_time : str, optional
        The start time of the night. The default is '22:00'.
    end_night_time : str, optional
        The end time of the night. The default is '06:00'.

    Returns
    -------
    ndarray
        A 3-dimension numpy array indicating the result table with indivisual id and corresponding home location (latitude and longitude).
    """
    tdf = fu.load_tdf(input_file)
    hldf = hl(tdf, start_night_time, end_night_time, False)
    fu.save_csv(hldf, output_file)
    return hldf.to_numpy()