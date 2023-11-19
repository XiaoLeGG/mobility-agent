from skmob.models.markov_diary_generator import MarkovDiaryGenerator
from ..utils import file_utils as fu


def generate_diary(
        input_file,
        output_file,
        n_individuals,
        diary_length,
        start_time
):
    """
    simulate or predict trajectory data from the input trajectory (the input data must be preprocessed by cluster)data by using Markov Diary Learner and Generator. The resulting composite movement diary includes the movement of individuals between clusters.

    A Mobility Diary Learner (MDL) is a data-driven algorithm to compute a mobility diary MD from the mobility trajectories of a set of real individuals. We use a Markov model to describe the probability that an individual follows her routine and visits a typical location at the usual time, or she breaks the routine and visits another location. First, MDL translates mobility trajectory data of real individuals into abstract mobility trajectories. Second, it uses the obtained abstract trajectory data to compute the transition probabilities of the Markov model MD(t)
    Parameters
    ----------
    input_file : str
        The input data file path(the data must be preprocessed by cluster)
    output_file : str
        The file path where store generated data.
    n_individuals : int
        the number of individual in the input data
    start_time : datetime
        the starting date of the generation.
    diary_length : int
        the length of the diary in hours.
    Returns
    -------
    ndarray
        A 2-dimension numpy array indicating the result table with time and the cluster_id.
    """

    tdf = fu.load_tdf(input_file)
    if "cluster" in tdf.columns:
        markov_diary_generator = MarkovDiaryGenerator()
        markov_diary_generator.fit(tdf,n_individuals,lid='cluster')
        dairy = markov_diary_generator.generate(diary_length, start_time)
        fu.save_csv(dairy, output_file)
        return dairy
    else:
        print("The input data must be preprocessed by cluster")