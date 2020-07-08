from dataclasses import dataclass
from typing import Dict


@dataclass
class Face:
    image_url: str
    face_id: str
    face_rectangle: Dict
    size: int
    face_attr: Dict