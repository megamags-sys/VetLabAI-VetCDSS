from datetime import datetime
from modules.analysis_id import generate_analysis_id
from modules.report_generator import generate_report
from models.patient import Patient

def main():
    print("VetLabAI Vet-CDSS V0.1.0-alpha")
    mrn = input("MRN: ").strip()
    name = input("Patient Name: ").strip()
    species = input("Species: ").strip()
    breed = input("Breed: ").strip()
    age = input("Age: ").strip()
    sex = input("Sex: ").strip()
    weight = float(input("Body Weight (kg): ") or 0)

    patient = Patient(mrn, name, species, breed, age, sex, weight)
    analysis_id = generate_analysis_id(mrn)
    report = generate_report(patient, analysis_id)

    path = f"reports/{analysis_id}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nCreated: {path}")

if __name__ == "__main__":
    main()
