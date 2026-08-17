from dataclasses import dataclass
from datetime import datetime

@dataclass
class Analysis:
    mrn: str
    analysis_id: str
    visit_no: int = 1
    created_at: datetime = datetime.now()
    status: str = "Initial Analysis"
