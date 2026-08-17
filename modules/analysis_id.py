from datetime import datetime
import re

def generate_analysis_id(mrn: str, sequence: int = 1, when=None) -> str:
    when = when or datetime.now()
    safe_mrn = re.sub(r"[^A-Za-z0-9_-]", "", mrn).upper()
    return f"{safe_mrn}-{when:%Y%m%d}-{sequence:03d}"
