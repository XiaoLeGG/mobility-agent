from skmob.core.trajectorydataframe import TrajDataFrame
from skmob.core.flowdataframe import FlowDataFrame
import pandas as pd


def load_tdf(
        input_file: str
):
    return TrajDataFrame.from_file(input_file, latitude='lat', longitude='lon', user_id='user', datetime='datetime')


def load_fdf(
        input_file: str
):
    return FlowDataFrame.from_file(input_file, origin='origin', destination='destination', datetime='datetime')


def load_df(
        input_file: str
):
    return pd.read_csv(input_file)


def save_csv(
        frame: pd.DataFrame,
        output_file: str
):
    if frame.empty:
        return
    frame.to_csv(output_file, index=False)
