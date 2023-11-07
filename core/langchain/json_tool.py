from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import json

class JsonSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True
    content: str = Field(description="The JSON format data.")
    output_file: str = Field(description="The file path to store json.")
    
class JsonTool(BaseTool):
    name = "json"
    description = "Store the JSON format data in the output file."
    args_schema: Type[JsonSchema] = JsonSchema
    def _run(
            self,
            content: str,
            output_file: str
    ) -> int:
        """Store json."""
        json_data = json.loads(content)
        json.dump(json_data, open(output_file, "w"))