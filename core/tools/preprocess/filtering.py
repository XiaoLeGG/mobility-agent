from skmob.preprocessing import filtering
from ..utils import file_utils as fu

def noise_filtering(
    input_file: str,
    output_file: str,
    max_speed: float=200,
    include_loop: bool=True,
    loop_intensity: float=1
) -> int:
    """This function help filter the useless or unreasonable points such as object suddenly moves too fast or object moves in a short and fast circles.
    
    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.
    max_speed : float, optional
        Indicate that the points with a speed(km/h) from previous point that beyond the max_speed will be deleted.
    include_loop : bool, optional
        Indicate whether to delete short and fast loops in the trajectories.
    loop_intensity : float, optional
        Indicate the intensity of deleting loops.

    Returns
    -------
    int
        The number of deleted points.
    """
    tdf = fu.load_tdf(input_file)
    ntdf = filtering.filter(tdf, max_speed_kmh=max_speed, include_loops=include_loop, speed_kmh=loop_intensity * 5, max_loop=int(loop_intensity * 6), ratio_max=loop_intensity * 0.25)
    fu.save_csv(ntdf, output_file)
    return len(tdf) - len(ntdf)