from skmob.preprocessing import detection
from ..utils import file_utils as fu

def stop_detection(
        input_file: str,
        output_file: str,
        stay_time: float=20,
        radius: float=1.0
) -> int:
    """
    Find the points in trajectory that can represent point-of-interest such as schools, restaurants, and bars, or user-specific places such as home and work locations.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.
    stay_time : float, optional
        The minimum minutes that the object stays in the point.
    radius : float, optional
        The radius(km) to represent the maximum size of a point.
    
    Returns
    -------
    int
        The number of detected points.
    """
    tdf = fu.load_tdf(input_file)
    stdf = detection.stay_locations(tdf, minutes_for_a_stop=stay_time, spatial_radius_km=radius, leaving_time=False, no_data_for_minutes=1e12, min_speed_kmh=2)
    fu.save_csv(stdf, output_file)
    return len(stdf)