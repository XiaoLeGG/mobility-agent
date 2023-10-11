import os

os.environ["OPENAI_API_KEY"] = ""

from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, Tool
from langchain.agents import AgentType, initialize_agent
from pydantic import BaseModel, Field
from skmob import TrajDataFrame
from skmob.preprocessing import detection
from typing import Optional, Type


class StayLocationSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    tdf: TrajDataFrame = Field(description="the input trajectories of the individuals.")
    stop_radius_factor: float = Field(
        description="if argument `spatial_radius_km` is `None`, the spatial_radius used is"
                    "the value specified in the TrajDataFrame properties ("
                    "\"spatial_radius_km\" assigned by a `preprocessing.compression` "
                    "function) multiplied by this argument, `stop_radius_factor`. The "
                    "default is `0.5`.")
    minutes_for_a_stop: float = Field(description="the minimum stop duration, in minutes. The default is `20.0`.")
    spatial_radius_km: float = Field(description="the radius of the ball enclosing all trajectory points within the "
                                                 "stop location. The default is `0.2`")
    leaving_time: bool = Field(description="if `True`, a new column 'leaving_datetime' is added with the departure "
                                           "time from the stop location. The default is `True`")
    no_data_for_minutes: float = Field(description="if the number of minutes between two consecutive points is larger "
                                                   "than `no_data_for_minutes`,then this is interpreted as missing "
                                                   "data and does not count as a stop. The default is `1e12`.")
    min_speed_kmh: float = Field(description="if not `None`, remove the points at the end of a stop if their speed is "
                                             "larger than `min_speed_kmh` km/h. The default is `None`.")


class StayLocationTool(BaseTool):

    name = "stay_locations"
    description = "Detect the stay locations (or stops) for each individual in a TrajDataFrame. A stop is detected " \
                      "when the individual spends at least `minutes_for_a_stop` minutes within a distance " \
                      "`stop_radius_factor * spatial_radius` km from a given trajectory point. The stop's coordinates are " \
                      "the median latitude and longitude values of the points found within the specified distance."
    args_schema: Type[StayLocationSchema] = StayLocationSchema



    def _run(
            self,
            tdf: TrajDataFrame,
            stop_radius_factor: float,
            minutes_for_a_stop: float,
            spatial_radius_km: float,
            leaving_time: bool,
            no_data_for_minutes: float,
            min_speed_kmh: float,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> TrajDataFrame:
        """Use the tool."""
        return detection.stay_locations(tdf, stop_radius_factor, minutes_for_a_stop, spatial_radius_km, leaving_time,
                                        no_data_for_minutes, min_speed_kmh)



llm = ChatOpenAI(temperature=0)
tools = [StayLocationTool()]


agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent.run(
    "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"
)
