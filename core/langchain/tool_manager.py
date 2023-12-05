from .compression_tool import CompressionTool
from .filtering_tool import FilteringTool
from .plot_trajectory import PlotTrajectoryTool, PlotScatterTool, PlotTrajectoryAndScatterTool, PlotHeatmapDensityTool, \
    PlotHeatmapTool, PlotDynamicTrajectoryTool
from .stop_detection_tool import StopDetectionTool
from .json_tool import JsonTool
from .home_location_tool import HomeLocationTool
from .max_distance_tool import MaxDistanceTool
from .gyration_tool import RadiusGyrationTool, KRadiusGyrationTool
from .jump_lengths_tool import JumpLengthsTool
from .recency_rank_tool import RecencyRankTool
from .table_reader_tool import TableReaderTool
from langchain_experimental.tools.python.tool import PythonREPLTool
from typing import List
from langchain.tools import BaseTool


def collect_tools():
    tools: List[BaseTool] = [CompressionTool(),
            FilteringTool(),
            StopDetectionTool(),
            HomeLocationTool(),
            JsonTool(),
            MaxDistanceTool(),
            RadiusGyrationTool(),
            KRadiusGyrationTool(),
            JumpLengthsTool(),
            RecencyRankTool(),
            TableReaderTool(),
            PythonREPLTool(),
            PlotTrajectoryTool(),
            PlotScatterTool(),
            PlotHeatmapDensityTool(),
            PlotHeatmapTool(),
            PlotDynamicTrajectoryTool(),
            PlotTrajectoryAndScatterTool()
            ]
    for i in range(len(tools)):
        tools[i].handle_tool_error=lambda e: "Error occurs, you may check the existance of file and use table reader to check the data: " + str(e)
    return tools


