from dataclasses import dataclass, field
from typing import Dict

@dataclass
class LaboratoryResults:
    cbc: Dict[str, float] = field(default_factory=dict)
    chemistry: Dict[str, float] = field(default_factory=dict)
    urinalysis: Dict[str, str] = field(default_factory=dict)
