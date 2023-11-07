from skmob.core.trajectorydataframe import TrajDataFrame
import pandas as pd

def load_tdf(
    input_file : str      
):
    return TrajDataFrame.from_file(input_file, latitude='lat', longitude='lon', user_id='user', datetime='datetime')

def save_csv(
    frame : TrajDataFrame,
    output_file : str
):
    frame.to_csv(output_file)

def df_save_csv(
    df : pd.DataFrame,
    output_file : str
):
    df.to_csv(output_file)