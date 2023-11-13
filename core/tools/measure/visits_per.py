from skmob.measures.collective import visits_per_location as vpl
from skmob.measures.collective import visits_per_time_unit as vptu
from ..utils import file_utils as fu


def visits_per_location(
        input_file: str,
        output_file: str,
):
    """
    Compute the number of visits to each location.

    Parameters
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndArray
        A 3-dimension numpy array indicating the result table with location (latitude and longitude) and the number of visits of this location. (sorted by last indice)
    """
    tdf = fu.load_tdf(input_file)
    vpl_df = vpl(tdf)
    fu.save_csv(vpl_df, output_file)
    return vpl_df.to_numpy()


def visits_per_time_unit(
        input_file: str,
        output_file: str,
):
    """
    Compute the number of data points per time unit (hour).

    Parameters
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndArray
        A 2-dimension numpy array indicating the result table with datatime and the number of visits of this datatime. (sorted by last indice)
    """
    tdf = fu.load_tdf(input_file)
    vptu_df = vptu(tdf)
    fu.save_csv(vptu_df, output_file)
    return vptu_df.to_numpy()
