from .compression_tool import CompressionTool
from .filtering_tool import FilteringTool
from .stop_detection_tool import StopDetectionTool
from .json_tool import JsonTool
from .home_location_tool import HomeLocationTool
from .max_distance_tool import MaxDistanceTool
from .gyration_tool import RadiusGyrationTool, KRadiusGyrationTool
from .jump_lengths_tool import JumpLengthsTool


def collect_tools():
    return [CompressionTool(), FilteringTool(), StopDetectionTool(), HomeLocationTool(), JsonTool(), MaxDistanceTool(), RadiusGyrationTool(), KRadiusGyrationTool(), JumpLengthsTool()]