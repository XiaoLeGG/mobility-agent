from skmob.measures.collective import mean_square_displacement as msd
from ..utils import file_utils as fu


def mean_square_displacement(
        input_file: str,
        output_file: str,
        days: int = 0
):
    """
    Compute the mean square displacement across the individuals. The mean squared displacement is a measure of the deviation of the position of an object with respect to a reference position over time. It is defined as: MSD = \langle |r(t) - r(0)| \\rangle = \\frac{1}{N} \sum_{i = 1}^N |r^{(i)}(t) - r^{(i)}(0)|^2 where N is the number of individuals to be averaged, vector x^{(i)}(0) is the reference position of the i-th individual, and vector x^{(i)}(t) is the position of the i-th individual at time t.

    Warnings: The input TrajDataFrame must be sorted in ascending order by datetime.

    Parameters
    ----------
    input_file : str
        The data file path to be processed.
    output_file : str
        The file path where the processed data stored.
    days : int, optional
        the days since the starting time. The default is 0.

    Returns
    -------
    double
        the result after compute(it's a double!! not array)
    """
    tdf = fu.load_tdf(input_file)
    msd_result = msd(tdf, days)
    # fu.save_csv(msd_result, output_file) // 加一个save函数？
    return msd_result
