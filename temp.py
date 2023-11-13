# Importing necessary libraries
import pandas as pd
from fuzzywuzzy import process

# Reading the CSV file
file_path = 'Ethics Project Form (Responses) - Form Responses 1.csv'
insurance_col = pd.read_csv(file_path, usecols=["What’s your healthcare insurance provider?"])

# Dictionary created for local Lafayette Hosptials and what insurances they cover
hospital_insurance_mapping = {
    "IU Arnett": [
        "Aetna",
        "Anthem",
        "Blue Cross and Blue Shield",
        "CareSource Managed Medicaid - HHW & HIP",
        "CareSource Marketplace",
        "CIGNA HealthCare PPO/HMO",
        "Cofinity (Aetna) PPOM/PPO",
        "Community Health Alliance",
        "Community Health Direct Gold/Sliver",
        "Deaconess OneCare",
        "Encore Health Network PPO",
        "EncoreCombined",
        "First Health Network",
        "Humana ChoiceCare",
        "Humana Medicare Advantage HMO/PPO",
        "IU Health Plans",
        "IU Health Plans Medicare Advantage HMO",
        "IU Health Plans - IU Health Employee Plan",
        "Lutheran Preferred",
        "Medicaid (Traditional)",
        "Medicare (Traditional)",
        "MultiPlan/PHCS",
        "Parkview Signature Care PPO/EPO",
        "Pakota Valley",
        "Physicians Health Plan of Northern Indiana (PHP)",
        "Sagamore Health Network",
        "SHO Direct",
        "Southern Indiana Health Organization (SIHO) Inspire/PPO",
        "UnitedHealthCare",
        "UnitedHealthCare Medicare Advantage HMO/POS/PPO",
        "VA Community Care Network"
    ],
    "Franciscan": [
        "Aetna",
        "Aetna Whole Health",
        "Coordinated Care Ambetter",
        "BridgeSpan (RealValue)",
        "CHPW -Cascade Select",
        "Kitsap County - Specialist only",
        "Cigna",
        "Coventry/First Health",
        "First Choice Health Network",
        "Humana/ChoiceCare",
        "Kaiser Permanente Core",
        "Partial",
        "Kaiser Permanente CoreSelect",
        "Kaiser Permanente Virtual Plus",
        "Kaiser Permanente Access PPO",
        "Kaiser Permanente Summit PPO",
        "LifeWise",
        "LifeWise Primary",
        "LifeWise Preferred",
        "Molina Marketplace",
        "Multiplan/PHCS",
        "Premera Blue Cross",
        "Premera Heritage Prime",
        "Kitsap Co. Clinics",
        "Premera Heritage Signature",
        "Regence Blue Shield",
        "Regence VMFH AHN",
        "Regence Individual & Family",
        "Uniform Medical Plan (UMP)",
        "UMP Plus - PSHVN",
        "United Healthcare (UHC)",
        "UHC Doctors Plan",
        "UHC Nexus ACO",
        "UHC Navigate",
        "UHC Charter"
    ],
    "Purdue PUSH": [
        "United Healthcare",
        "Anthem",
        "Blue Cross and Blue Shield"
    ]
}

# Finds the closest match for user_input in insurance_options.
def find_best_insurance_match(user_input, insurance_options, threshold=60):
    best_match, score = process.extractOne(user_input, insurance_options)
    if score < threshold:
        return None
    return best_match

# Given an insurance provider, return a list of hospitals that accept this insurance.
def get_hospitals_for_insurance(insurance, mapping):
    if insurance is None:
        return "Emergency Care"
    
    hospitals = []
    for hospital, insurances in mapping.items():
        if insurance in insurances:
            hospitals.append(hospital)

    if not hospitals:
        return "Emergency Care"
    return hospitals

user_input = input("Enter your healthcare insurance provider: ")
insurance_options = sum(hospital_insurance_mapping.values(), [])  # Flatten the list of all insurances
best_insurance_match = find_best_insurance_match(user_input, insurance_options)
hospitals = get_hospitals_for_insurance(best_insurance_match, hospital_insurance_mapping)

if best_insurance_match is None:
    print("No close match found for your insurance. Suggested option: Emergency Care")
else:
    print("Best insurance match:", best_insurance_match)
    print("Hospitals that accept this insurance:", hospitals)

