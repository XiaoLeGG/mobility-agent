from skmob.measures.individual import random_entropy as rand_e
from skmob.measures.individual import real_entropy as real_e
from skmob.measures.individual import uncorrelated_entropy as une
from skmob.measures.collective import random_location_entropy as rle
from skmob.measures.collective import uncorrelated_location_entropy as ule
from ..utils import file_utils as fu


def random_entropy(
        input_file: str,
        output_file: str,
):
    """
    Compute the random entropy of a set of individuals. In this tool, we think every location is visited with equal probability, and the random entropy is defined as E_rand(u)=log2(N_u) , where N_u is the number of distinct locations visited by individual `u`. The more places the user went, the higher the value.

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with individual id and the random entropy for this individual.
    """
    tdf = fu.load_tdf(input_file)
    rand_pd = rand_e(tdf, False)
    fu.save_csv(rand_pd, output_file)
    return rand_pd.to_numpy()


def real_entropy(
        input_file: str,
        output_file: str,
):
    """
    Compute the real entropy of a set of individuals. The real entropy depends not only on the frequency of visitation, but also the order in which the nodes were visited and the time spent at each location, thus capturing the full spatio-temporal order present in an `u`'s mobility patterns. he random entropy of an individual `u` is defined as
    $$
    E(u) = - \sum_{T'_u}P(T'_u)log_2[P(T_u^i)]
    $$
    where P(T_u′) is the probability of finding a particular time-ordered subsequence T_u′ in the trajectory T_u.

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
        A 2-dimension numpy array indicating the result table with individual id and the real entropy for this individual.
    """
    tdf = fu.load_tdf(input_file)
    real_pd = real_e(tdf, False)
    fu.save_csv(real_pd, output_file)
    return real_pd.to_numpy()


def uncorrelated_entropy(
        input_file: str,
        output_file: str,
):
    """
    Compute the temporal-uncorrelated entropy of a set of individuals. The temporal-uncorrelated entropy of an individual `u` is defined as
    $$
    E_{unc}(u) = - \sum_{j=1}^{N_u} p_u(j) log_2 p_u(j)
    $$
    where p_u(j) is the number of distinct locations visited by `i` and p_u(j) is the historical probability that a location `j` was visited by `u`. The temporal-uncorrelated entropy characterizes the heterogeneity of `u`s visitation patterns.

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with individual id and the temporal-uncorrelated entropy for this individual.
    """
    tdf = fu.load_tdf(input_file)
    une_pd = une(tdf,False, False,)
    fu.save_csv(une_pd, output_file)
    return une_pd.to_numpy()

def random_location_entropy(
        input_file: str,
        output_file: str,
):
    """
    Compute the random location entropy of the locations. The random location entropy of a location j captures the degree of predictability of j if each individual visits it with equal probability, and it is defined as: LE_{rand}(j) = log_2(N_j) where N_j is the number of distinct individuals that visited location j. The result(output file) of this measure is as follows:

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A 3-dimension numpy array indicating the result table with location (latitude and longitude) and the random entropy of this location. (sorted by last indice)
    """
    tdf = fu.load_tdf(input_file)
    rle_pd = rle(tdf, False)
    fu.save_csv(rle_pd, output_file)
    return rle_pd.to_numpy()


def uncorrelated_location_entropy(
        input_file: str,
        output_file: str,
):
    """
    Compute the temporal-uncorrelated location entropy of the locations. The temporal-uncorrelated location entropy LE_{unc}(j) of a location j is the historical probability that j is visited by an individual $$u$$. Formally, it is defined as : LE_{unc}(j) = -\sum_{i=j}^{N_j} p_jlog_2(p_j) where N_j is the number of distinct individuals that visited j and p_j is the historical probability that a visit to location j is by individual u.

    Parameters
    ----------
    input_file : str
        The data file path to be measured.
    output_file : str
        The file path where the measured data stored.

    Returns
    -------
    ndarray
        A 3-dimension numpy array indicating the result table with location (latitude and longitude) and the uncorrelated entropy of this location. (sorted by last indice)
    """
    tdf = fu.load_tdf(input_file)
    ule_pd = ule(tdf, False, False)
    fu.save_csv(ule_pd, output_file)
    return ule_pd.to_numpy()
