from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
from ..tools.utils import geo_decode, file_utils as fu
import pandas as pd;


class GeoDecodeSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True
    input_file: str = Field(description="The data file path to be processed.")
    output_file: str = Field(description="The file path where the processed data stored.")


class GeoDecodeTool(BaseTool):
    name = "geo_decode"
    description = str(
        "Transfer the latitude and longitude to specific address with its relative information."
        "This can help you to better understand the location and wrap a range of location to a specific address."
        "This tool add a new column named 'address_info' to the data table."
        "The format of the address_info is 'address_name-function_type-class-province,city,district'."
    )
    args_schema: Type[GeoDecodeSchema] = GeoDecodeSchema
    def _run(
            self,
            input_file: str,
            output_file: str,
    ) -> None:
        """Use the tool."""
        data = fu.load_tdf(input_file)
        for i in range(len(data)):
            data.loc[i, 'address_info'] = geo_decode(data.loc[i, 'lat'], data.loc[i, 'lng'])
        fu.save_csv(data, output_file)