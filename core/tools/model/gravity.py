from skmob.models.gravity import Gravity
from skmob.utils import utils, constants
import geopandas as gpd
from ..utils import file_utils as fu


def gravity_model(
        input_file,
        output_file
):
    """
    simulate or predict flow data from the input flow data by using Gravity Model.

    The Gravity model of human migration posits that the probability \(T_{ij}\) of moving from location \(i\) to \(j\) is proportional to \(\frac{P_i P_j}{r_{ij}}\), where \(P_i\) and \(P_j\) are the populations of locations \(i\) and \(j\), and \(r_{ij}\) is the distance between them. This model assumes that the number of trips leaving \(i\) is proportional to its population, the attractiveness of \(j\) is proportional to its population, and there is a cost effect in terms of distance traveled.

    A generalized form of this model is \(T_{ij} = K m_i m_j f(r_{ij})\), where \(K\) is a constant, \(m_i\) and \(m_j\) relate to the number of trips, and \(f(r_{ij})\) is a decreasing function of distance.

    Constrained gravity models address limitations. In a singly constrained model, the number of people originating from \(i\) is a known quantity \(O_i\), and the model estimates the destination: \[ T_{ij} = K_i O_i m_j f(r_{ij}) = O_i \frac{m_i f(r_{ij})}{\sum_k m_k f(r_{ik})} \]

    Proportionality constants \(K_i\) depend on the origin's location. A doubly-constrained model, fixing the total travelers arriving at \(j\) as \(D_j\), calculates: \[ T_{ij} = K_i O_i L_j D_j f(r_{ij}) \]

    Parameters
    ----------
    input_file : str
        The input data file path
    output_file : str
        The file path where store generated data.
    Returns
    -------
    ndarray
        A 3-dimension numpy array indicating the result table with origin area, destination area and flow.
    """

    fdf = fu.load_fdf(input_file)
    tessellation = gpd.read_file(input_file).rename(columns={'tile_id': 'tile_ID'})
    tot_outflows = fdf[fdf['origin'] != fdf['destination']].groupby(by='origin', axis=0)[['flow']].sum().fillna(0)
    tessellation = tessellation.merge(tot_outflows, left_on='tile_ID', right_on='origin').rename(
        columns={'flow': constants.TOT_OUTFLOW})
    g = Gravity(gravity_type='singly constrained')
    g.fit(fdf, relevance_column='population')
    g_df = g.generate(tessellation, tile_id_column='tile_ID',
                      tot_outflows_column='tot_outflow',
                      relevance_column='population',
                      out_format='flows')
    return g_df.to_numpy()
