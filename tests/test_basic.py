from modules.analysis_id import generate_analysis_id
from models.patient import Patient

def test_analysis_id():
    value = generate_analysis_id("VH0002458")
    assert value.startswith("VH0002458-")
    assert value.endswith("-001")

def test_patient():
    p = Patient("VH1", "Lucky", "Dog", "Shiba Inu", "12Y", "MN", 10.8)
    assert p.mrn == "VH1"
    assert p.weight == 10.8
