from skmob.core.trajectorydataframe import TrajDataFrame
import pandas as pd

def load_tdf(
    input_file : str      
):
    return TrajDataFrame.from_file(input_file, latitude='lat', longitude='lon', user_id='user', datetime='datetime')

def save_csv(
    frame : pd.DataFrame,
    output_file : str
):
    if frame.empty:
        return
    frame.to_csv(output_file, index=False)