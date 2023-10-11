import pandas as pd
from skmob.preprocessing import detection
from skmob.preprocessing import filtering
from skmob.core.trajectorydataframe import TrajDataFrame


tdf = TrajDataFrame.from_file('geolife_sample.txt.gz', latitude='lat', longitude='lon', user_id='user', datetime='datetime')

# Preprocess the trajectory data by filtering out noise
tdf = filtering.filter(tdf, max_speed_kmh=100)
stdf = detection.stay_locations(tdf, stop_radius_factor=0.5, minutes_for_a_stop=20.0, spatial_radius_km=0.2,
                                    leaving_time=True)
print(stdf.head())