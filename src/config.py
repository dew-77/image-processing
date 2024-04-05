from typing import List, Optional
import os
import json
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class ResolutionPreset(BaseModel):
    name: str
    resW: int
    resH: int
    index: int
    quality: Optional[int]


class Settings(BaseModel):
    allowed_extensions: List[str]
    directory_to_save: str
    resolution_presets: List[ResolutionPreset]


def parse_presets() -> List:
    """Function to parse presets from .env to Pydantic model."""
    index = 0
    resolution_presets = []
    while True:
        preset_str = os.getenv(f'RESOLUTION_PRESETS_{index}')
        if preset_str is None:
            break
        preset_data = json.loads(preset_str)
        resolution_presets.append(ResolutionPreset(**preset_data))
        index += 1
    return resolution_presets


allowed_extensions = os.getenv('ALLOWED_EXTENSIONS').split(',')
directory_to_save = os.getenv('DIRECTORY_TO_SAVE')

settings = Settings(
    allowed_extensions=allowed_extensions,
    directory_to_save=directory_to_save,
    resolution_presets=parse_presets()
)
