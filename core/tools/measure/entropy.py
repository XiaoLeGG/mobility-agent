from skmob.measures.individual import random_entropy as rand_e
from skmob.measures.individual import real_entropy as real_e
from skmob.measures.individual import uncorrelated_entropy as une
from ..utils import file_utils as fu


def random_entropy(
        input_file: str,
        output_file: str,
):
    """
    Compute the random entropy of a set of individuals in a TrajDataFrame. In this tool, we think every location is visited with equal probability, and the random entropy is defined as E_rand(u)=log2(N_u) , where N_u is the number of distinct locations visited by individual `u`. The more places the user went, the higher the value.

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
    fu.df_save_csv(rand_pd, output_file)
    return rand_pd.to_numpy()


def real_entropy(
        input_file: str,
        output_file: str,
):
    """
    Compute the real entropy of a set of individuals in a TrajDataFrame. The real entropy depends not only on the frequency of visitation, but also the order in which the nodes were visited and the time spent at each location, thus capturing the full spatio-temporal order present in an `u`'s mobility patterns. he random entropy of an individual `u` is defined as
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
    fu.df_save_csv(real_pd, output_file)
    return real_pd.to_numpy()


def uncorrelated_entropy(
        input_file: str,
        output_file: str,
):
    """
    Compute the temporal-uncorrelated entropy of a set of individuals in a TrajDataFrame. The temporal-uncorrelated entropy of an individual `u` is defined as
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
    fu.df_save_csv(une_pd, output_file)
    return une_pd.to_numpy()