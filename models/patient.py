from dataclasses import dataclass

@dataclass
class Patient:
    mrn: str
    name: str
    species: str
    breed: str = ""
    age: str = ""
    sex: str = ""
    weight: float = 0.0
