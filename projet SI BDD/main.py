from typing import Union

from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import Projet_base_de_donnees as projet
from pydantic import BaseModel

app = FastAPI()
connection, cursor = projet.connect_database()



@app.get("/")
def read_root():
    return {"Hello": "World"} 


@app.get("/api/data")
def get_data():
    return {"message": "Hello from FastAPI!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/add_doctor")
def add_doctor_route(
    ID_DOCTEUR: int = projet.generate_unique_id("DOCTEUR","ID_DOCTEUR",cursor),
    NOM_DOC: str = Form(...),
    PRENOM_DOC: str = Form(...),
    TITRE_DOC: str = Form(...),
    SPE_DOC: str = Form(...),
    EXPERTISES_DOC: str = Form(...),
    MDP_DOC: str = Form(...),
    ):

    doctor_data = {
        'ID_DOCTEUR': ID_DOCTEUR,
        'NOM_DOC': NOM_DOC,
        'PRENOM_DOC': PRENOM_DOC,
        'TITRE_DOC': TITRE_DOC,
        'SPE_DOC': SPE_DOC,
        'EXPERTISES_DOC': EXPERTISES_DOC,
        'MDP_DOC': MDP_DOC,
    }

    # Call the asynchronous add_doctor function with doctor_data
    projet.add_doctor(doctor_data)

    return {"message": "Doctor added successfully"}

@app.get("/get_all_doctors")
def get_all_doctors():
    return projet.get_all_doctors()

@app.get("/get_doctor_by_id")
def get_doctor_by_id(doctor_id):
    return projet.get_doctor_by_id(doctor_id)

@app.put("/update_doctor/{doctor_id}")
def update_doctor_route(
    doctor_id: int,
    NOM_DOC: str = None,
    PRENOM_DOC: str = None,
    TITRE_DOC: str = None,
    SPE_DOC: str = None,
    EXPERTISES_DOC: str = None,
    MDP_DOC: str = None
):
    try:
        # Call the function to update the doctor's information
        projet.update_doctor(
            doctor_id,
            {
                "NOM_DOC": NOM_DOC,
                "PRENOM_DOC": PRENOM_DOC,
                "TITRE_DOC": TITRE_DOC,
                "SPE_DOC": SPE_DOC,
                "EXPERTISES_DOC": EXPERTISES_DOC,
                "MDP_DOC": MDP_DOC,
            }
        )

        return {"message": "Doctor updated successfully"}
    except Exception as e:
        # Handle exceptions, such as doctor not found
        return {"ERROR 404 : Doctor not found ! "}

@app.delete("/delete_doctor/{doctor_id}")
def delete_doctor_route(doctor_id: int):
    try:
        # Call the function to delete the doctor
        projet.delete_doctor(doctor_id)
        return {"message": "Doctor deleted successfully"}
    except Exception as e:
        # Handle exceptions, such as doctor not found
        return {"ERROR 404 : Doctor not found ! "}

@app.post("/add_patient")
def add_patient_route(
    ID_PATIENT: int = projet.generate_unique_id("PATIENT", "ID_PATIENT", cursor),
    NOM_PATIENT: str = Form(...),
    PRENOM_PATIENT: str = Form(...),
    DATE_NAISSANCE: str = Form(...),
    N_SS: str = Form(...),
    N_MUTUELLE: str = Form(...),
    ADRESSE: str = Form(...),
    CP: str = Form(...),
    VILLE: str = Form(...),
    CEDEX: str = Form(...),
    TELEPHONE: str = Form(...),
    ADRESSE_MAIL: str = Form(...),
    NOM_MEDECIN_TRAITANT: str = Form(...),
):
    try:
        # Prepare patient data
        patient_data = {
            'ID_PATIENT': ID_PATIENT,
            'NOM_PATIENT': NOM_PATIENT,
            'PRENOM_PATIENT': PRENOM_PATIENT,
            'DATE_NAISSANCE': DATE_NAISSANCE,
            'N_SS': N_SS,
            'N_MUTUELLE': N_MUTUELLE,
            'ADRESSE': ADRESSE,
            'CP': CP,
            'VILLE': VILLE,
            'CEDEX': CEDEX,
            'TELEPHONE': TELEPHONE,
            'ADRESSE_MAIL': ADRESSE_MAIL,
            'NOM_MEDECIN_TRAITANT': NOM_MEDECIN_TRAITANT,
        }

        # Add the patient to the database
        projet.add_patient(patient_data)

        return {"message": "Patient added successfully"}
    except Exception as e:
        # Handle exceptions, such as validation errors or database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_patients")
def get_all_patients():
    return projet.get_all_patients()

@app.get("/get_patient/{patient_id}")
async def get_patient_by_id(patient_id: int):
    try:
        # Call the function to get patient information by ID
        connection, cursor = projet.connect_database()
        patient = projet.get_entity_by_id("PATIENT", "ID_PATIENT", patient_id, cursor)

        if patient:
            # Return patient information
            return patient
        else:
            # If patient is not found, raise HTTP 404
            raise HTTPException(status_code=404, detail="Patient not found")
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_patient/{patient_id}")
def update_patient_route(
    patient_id: int,
    NOM_PATIENT: str = Form(None),
    PRENOM_PATIENT: str = Form(None),
    DATE_NAISSANCE: str = Form(None),
    N_SS: str = Form(None),
    N_MUTUELLE: str = Form(None),
    ADRESSE: str = Form(None),
    CP: str = Form(None),
    VILLE: str = Form(None),
    CEDEX: str = Form(None),
    TELEPHONE: str = Form(None),
    ADRESSE_MAIL: str = Form(None),
    NOM_MEDECIN_TRAITANT: str = Form(None),
):
    try:
        # Prepare updated data
        updated_data = {
            'NOM_PATIENT': NOM_PATIENT,
            'PRENOM_PATIENT': PRENOM_PATIENT,
            'DATE_NAISSANCE': DATE_NAISSANCE,
            'N_SS': N_SS,
            'N_MUTUELLE': N_MUTUELLE,
            'ADRESSE': ADRESSE,
            'CP': CP,
            'VILLE': VILLE,
            'CEDEX': CEDEX,
            'TELEPHONE': TELEPHONE,
            'ADRESSE_MAIL': ADRESSE_MAIL,
            'NOM_MEDECIN_TRAITANT': NOM_MEDECIN_TRAITANT,
        }

        # Call the function to update patient data
        projet.update_patient(patient_id, updated_data)

        return {"message": "Patient updated successfully"}
    except Exception as e:
        # Handle exceptions, such as validation errors or database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_patient/{patient_id}")
def delete_patient_route(patient_id: int):
    try:
        # Call the function to delete the doctor
        projet.delete_patient(patient_id)
        return {"message": "Patient deleted successfully"}
    except Exception as e:
        # Handle exceptions, such as doctor not found
        return {"ERROR 404 : Patient not found ! "}
    


@app.post("/add_receptionist")
async def add_receptionist_route(
    NOM_RECEP: str = Form(...),
    PRENOM_RECEP: str = Form(...),
    MDP_RECEP: str = Form(...),
):
    try:
        # Prepare receptionist data
        receptionist_data = {
            'ID_RECEPTIONNISTE': None,  # Assuming ID is generated automatically
            'NOM_RECEP': NOM_RECEP,
            'PRENOM_RECEP': PRENOM_RECEP,
            'MDP_RECEP': MDP_RECEP,
        }

        # Call the function to add a receptionist
        projet.add_receptionist(receptionist_data)

        return {"message": "Receptionist added successfully"}
    except Exception as e:
        # Handle exceptions, such as validation errors or database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_receptionists")
async def get_all_receptionists_route():
    try:
        # Call the function to get all receptionists
        receptionists = projet.get_all_receptionists()

        return {"receptionists": receptionists}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_receptionist/{receptionist_id}")
async def get_receptionist_route(receptionist_id: int):
    try:
        # Call the function to get a receptionist by ID
        receptionist = projet.get_receptionist_by_id(receptionist_id)

        return {"receptionist": receptionist}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_receptionist/{receptionist_id}")
async def update_receptionist_route(
    receptionist_id: int,
    NOM_RECEP: str = Form(None),
    PRENOM_RECEP: str = Form(None),
    MDP_RECEP: str = Form(None),
):
    try:
        # Prepare updated data
        updated_data = {
            'NOM_RECEP': NOM_RECEP,
            'PRENOM_RECEP': PRENOM_RECEP,
            'MDP_RECEP': MDP_RECEP,
        }

        # Call the function to update a receptionist
        projet.update_receptionist(receptionist_id, updated_data)

        return {"message": "Receptionist updated successfully"}
    except Exception as e:
        # Handle exceptions, such as validation errors or database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_receptionist/{receptionist_id}")
async def delete_receptionist_route(receptionist_id: int):
    try:
        # Call the function to delete a receptionist
        projet.delete_receptionist(receptionist_id)

        return {"message": "Receptionist deleted successfully"}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/add_rdv")
def add_rdv_route(
    DATE_RDV: str = Form(...),
    HEURE_RDV: str = Form(...),
    ETAT_RDV: str = Form(...),
    SALLE_EXAMEN: str = Form(...),
    ID_PATIENT: int = Form(...),
    ID_DOCTEUR: int = Form(...),
):
    try:
        # Prepare rdv data
        rdv_data = {
            'ID_RDV': None,  # Assuming ID is generated automatically
            'DATE_RDV': DATE_RDV,
            'HEURE_RDV': HEURE_RDV,
            'ETAT_RDV': ETAT_RDV,
            'SALLE_EXAMEN': SALLE_EXAMEN,
            'ID_PATIENT': ID_PATIENT,
            'ID_DOCTEUR': ID_DOCTEUR,
        }

        # Call the function to add an rdv
        projet.add_rdv(rdv_data)

        return {"message": "Rendez-vous added successfully"}
    except Exception as e:
        # Handle exceptions, such as validation errors or database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_rdvs")
def get_all_rdvs_route():
    try:
        # Call the function to get all rdvs
        rdvs = projet.get_all_rdvs()

        return {"rdvs": rdvs}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_rdv/{rdv_id}")
def get_rdv_route(rdv_id: int):
    try:
        # Call the function to get an rdv by ID
        rdv = projet.get_rdv_by_id(rdv_id)

        return {"rdv": rdv}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_rdv/{rdv_id}")
def update_rdv_route(
    rdv_id: int,
    DATE_RDV: str = Form(None),
    HEURE_RDV: str = Form(None),
    ETAT_RDV: str = Form(None),
    SALLE_EXAMEN: str = Form(None),
    ID_PATIENT: int = Form(None),
    ID_DOCTEUR: int = Form(None),
):
    try:
        # Prepare updated data
        updated_data = {
            'DATE_RDV': DATE_RDV,
            'HEURE_RDV': HEURE_RDV,
            'ETAT_RDV': ETAT_RDV,
            'SALLE_EXAMEN': SALLE_EXAMEN,
            'ID_PATIENT': ID_PATIENT,
            'ID_DOCTEUR': ID_DOCTEUR,
        }

        # Call the function to update an rdv
        projet.update_rdv(rdv_id, updated_data)

        return {"message": "Rendez-vous updated successfully"}
    except Exception as e:
        # Handle exceptions, such as validation errors or database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_rdv/{rdv_id}")
def delete_rdv_route(rdv_id: int):
    try:
        # Call the function to delete an rdv
        projet.delete_rdv(rdv_id)

        return {"message": "Rendez-vous deleted successfully"}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/add_message")
def add_message_route(
    DATE_MESSAGE: str = Form(...),
    QUESTION: str = Form(...),
    REPONSE: str = Form(...),
    ID_PATIENT: int = Form(...),
):
    try:
        # Prepare message data
        message_data = {
            'ID_MESSAGE': None,  # Assuming ID is generated automatically
            'DATE_MESSAGE': DATE_MESSAGE,
            'QUESTION': QUESTION,
            'REPONSE': REPONSE,
            'ID_PATIENT': ID_PATIENT,
        }

        # Call the function to add a message
        projet.add_message(message_data)

        return {"message": "Message added successfully"}
    except Exception as e:
        # Handle exceptions, such as validation errors or database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_messages")
def get_all_messages_route():
    try:
        # Call the function to get all messages
        messages = projet.get_all_messages()

        return {"messages": messages}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_message/{message_id}")
def get_message_route(message_id: int):
    try:
        # Call the function to get a message by ID
        message = projet.get_message_by_id(message_id)

        return {"message": message}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_message/{message_id}")
def update_message_route(
    message_id: int,
    DATE_MESSAGE: str = Form(None),
    QUESTION: str = Form(None),
    REPONSE: str = Form(None),
    ID_PATIENT: int = Form(None),
):
    try:
        # Prepare updated data
        updated_data = {
            'DATE_MESSAGE': DATE_MESSAGE,
            'QUESTION': QUESTION,
            'REPONSE': REPONSE,
            'ID_PATIENT': ID_PATIENT,
        }

        # Call the function to update a message
        projet.update_message(message_id, updated_data)

        return {"message": "Message updated successfully"}
    except Exception as e:
        # Handle exceptions, such as validation errors or database issues
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_message/{message_id}")
def delete_message_route(message_id: int):
    try:
        # Call the function to delete a message
        projet.delete_message(message_id)

        return {"message": "Message deleted successfully"}
    except Exception as e:
        # Handle exceptions, such as database issues
        raise HTTPException(status_code=500, detail=str(e))
    

# Reponse routes
@app.post("/add_reponse")
def add_reponse_route(
    DATE_REPONSE: str = Form(...),
    QUESTION: str = Form(...),
    REPONSE: str = Form(...),
    ID_PATIENT: int = Form(...),
):
    try:
        reponse_data = {
            'ID_REPONSE': None,
            'DATE_REPONSE': DATE_REPONSE,
            'QUESTION': QUESTION,
            'REPONSE': REPONSE,
            'ID_PATIENT': ID_PATIENT,
        }

        projet.add_reponse(reponse_data)

        return {"message": "Reponse added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get_all_reponses")
def get_all_reponses_route():
    try:
        reponses = projet.get_all_reponses()
        return {"reponses": reponses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get_reponse_by_id")
def get_reponse_by_id_route(reponse_id: int):
    try:
        reponse = projet.get_reponse_by_id(reponse_id)
        if reponse:
            return {"reponse": reponse}
        else:
            raise HTTPException(status_code=404, detail="Reponse not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_reponse/{reponse_id}")
def update_reponse_route(reponse_id: int, updated_data: dict):
    try:
        projet.update_reponse(reponse_id, updated_data)
        return {"message": "Reponse updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_reponse/{reponse_id}")
def delete_reponse_route(reponse_id: int):
    try:
        projet.delete_reponse(reponse_id)
        return {"message": "Reponse deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Repondre routes
@app.post("/add_repondre")
def add_repondre_route(
    ID_DOCTEUR: int = Form(...),
    ID_MESSAGE: int = Form(...),
):
    try:
        repondre_data = {
            'ID_DOCTEUR': ID_DOCTEUR,
            'ID_MESSAGE': ID_MESSAGE,
        }

        projet.add_repondre(repondre_data)

        return {"message": "Repondre added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_repondre")
def get_all_repondre_route():
    try:
        repondre_relations = projet.get_all_repondre()
        return {"repondre_relations": repondre_relations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_repondre/{docteur_id}/{message_id}")
def delete_repondre_route(docteur_id: int, message_id: int):
    try:
        projet.delete_repondre(docteur_id, message_id)
        return {"message": "Repondre relation deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Prise de sang routes
@app.post("/add_prise_sang")
def add_prise_sang_route(
    ID_PRISE_SANG: int = Form(...),
    DATE_PRISE_SANG: str = Form(...),
    GROUPE_SANGUIN: str = Form(...),
    HEMOGRAMME: str = Form(...),
    DOSAGE_FERRITINE: str = Form(...),
    VS: str = Form(...),
    CRP: str = Form(...),
    GLYCEMIE: str = Form(...),
    LDL: str = Form(...),
    HDL: str = Form(...),
    CHOLESTEROL_TOTAL: str = Form(...),
    BILAN_RENAL: str = Form(...),
    BILAN_HEPATIQUE: str = Form(...),
    ID_DOCTEUR: int = Form(...),
    ID_FACTURE_PS: int = Form(...),
    ID_PATIENT: int = Form(...),
):
    try:
        prise_sang_data = {
            'ID_PRISE_SANG': ID_PRISE_SANG,
            'DATE_PRISE_SANG': DATE_PRISE_SANG,
            'GROUPE_SANGUIN': GROUPE_SANGUIN,
            'HEMOGRAMME': HEMOGRAMME,
            'DOSAGE_FERRITINE': DOSAGE_FERRITINE,
            'VS': VS,
            'CRP': CRP,
            'GLYCEMIE': GLYCEMIE,
            'LDL': LDL,
            'HDL': HDL,
            'CHOLESTEROL_TOTAL': CHOLESTEROL_TOTAL,
            'BILAN_RENAL': BILAN_RENAL,
            'BILAN_HEPATIQUE': BILAN_HEPATIQUE,
            'ID_DOCTEUR': ID_DOCTEUR,
            'ID_FACTURE_PS': ID_FACTURE_PS,
            'ID_PATIENT': ID_PATIENT,
        }

        projet.add_prise_sang(prise_sang_data)

        return {"message": "Prise de sang added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_prises_sang")
def get_all_prises_sang_route():
    try:
        prises_sang = projet.get_all_prises_sang()
        return {"prises_sang": prises_sang}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_prise_sang/{prise_sang_id}")
def get_prise_sang_by_id_route(prise_sang_id: int):
    try:
        prise_sang = projet.get_prise_sang_by_id(prise_sang_id)
        if not prise_sang:
            raise HTTPException(status_code=404, detail="Prise de sang not found")
        return {"prise_sang": prise_sang}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_prise_sang/{prise_sang_id}")
def update_prise_sang_route(prise_sang_id: int, updated_data: dict):
    try:
        projet.update_prise_sang(prise_sang_id, updated_data)
        return {"message": "Prise de sang updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_prise_sang/{prise_sang_id}")
def delete_prise_sang_route(prise_sang_id: int):
    try:
        projet.delete_prise_sang(prise_sang_id)
        return {"message": "Prise de sang deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Facture prise sang routes
@app.post("/add_facture_prise_sang")
def add_facture_prise_sang_route(
    ID_FACTURE_PS: int = Form(...),
    MONTANT: float = Form(...),
    DATE_FACTURATION: str = Form(...),
    MODE_REGLEMENT: str = Form(...),
    EXAMENS_REMBOURSES: str = Form(...),
    EXAMENS_NON_REMBOURSES: str = Form(...),
    PART_SS: float = Form(...),
    PART_MUTUELLE: float = Form(...),
    RESTE_A_CHARGE: float = Form(...),
):
    try:
        facture_data = {
            'ID_FACTURE_PS': ID_FACTURE_PS,
            'MONTANT': MONTANT,
            'DATE_FACTURATION': DATE_FACTURATION,
            'MODE_REGLEMENT': MODE_REGLEMENT,
            'EXAMENS_REMBOURSES': EXAMENS_REMBOURSES,
            'EXAMENS_NON_REMBOURSES': EXAMENS_NON_REMBOURSES,
            'PART_SS': PART_SS,
            'PART_MUTUELLE': PART_MUTUELLE,
            'RESTE_A_CHARGE': RESTE_A_CHARGE,
        }

        projet.add_facture_prise_sang(facture_data)

        return {"message": "Facture prise de sang added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_factures_prise_sang")
def get_all_factures_prise_sang_route():
    try:
        factures_prise_sang = projet.get_all_factures_prise_sang()
        return {"factures_prise_sang": factures_prise_sang}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_facture_prise_sang/{facture_id}")
def get_facture_prise_sang_by_id_route(facture_id: int):
    try:
        facture_prise_sang = projet.get_facture_prise_sang_by_id(facture_id)
        if not facture_prise_sang:
            raise HTTPException(status_code=404, detail="Facture prise de sang not found")
        return {"facture_prise_sang": facture_prise_sang}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_facture_prise_sang/{facture_id}")
def update_facture_prise_sang_route(facture_id: int, updated_data: dict):
    try:
        projet.update_facture_prise_sang(facture_id, updated_data)
        return {"message": "Facture prise de sang updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_facture_prise_sang/{facture_id}")
def delete_facture_prise_sang_route(facture_id: int):
    try:
        projet.delete_facture_prise_sang(facture_id)
        return {"message": "Facture prise de sang deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Test ECBU routes
@app.post("/add_test_ecbu")
def add_test_ecbu_route(
    ID_FLACON_URINE: int = Form(...),
    DATE_ECBU: str = Form(...),
    QTE_LEUCOCYTES: int = Form(...),
    QTE_HEMATIES: int = Form(...),
    QTE_CELLULES_EPITHELIALES: int = Form(...),
    QTE_CRISTAUX: int = Form(...),
    QTE_HYALINS: int = Form(...),
    QTE_GERMES_URINES: int = Form(...),
    ANTIBIOGRAMME: str = Form(...),
    BACTERIURIE: str = Form(...),
    ID_DOCTEUR: int = Form(...),
    ID_FACTURE_ECBU: int = Form(...),
    ID_PATIENT: int = Form(...),
):
    try:
        test_data = {
            'ID_FLACON_URINE': ID_FLACON_URINE,
            'DATE_ECBU': DATE_ECBU,
            'QTE_LEUCOCYTES': QTE_LEUCOCYTES,
            'QTE_HEMATIES': QTE_HEMATIES,
            'QTE_CELLULES_EPITHELIALES': QTE_CELLULES_EPITHELIALES,
            'QTE_CRISTAUX': QTE_CRISTAUX,
            'QTE_HYALINS': QTE_HYALINS,
            'QTE_GERMES_URINES': QTE_GERMES_URINES,
            'ANTIBIOGRAMME': ANTIBIOGRAMME,
            'BACTERIURIE': BACTERIURIE,
            'ID_DOCTEUR': ID_DOCTEUR,
            'ID_FACTURE_ECBU': ID_FACTURE_ECBU,
            'ID_PATIENT': ID_PATIENT,
        }

        projet.add_test_ecbu(test_data)

        return {"message": "Test ECBU added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_tests_ecbu")
def get_all_tests_ecbu_route():
    try:
        tests_ecbu = projet.get_all_tests_ecbu()
        return {"tests_ecbu": tests_ecbu}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_test_ecbu/{test_id}")
def get_test_ecbu_by_id_route(test_id: int):
    try:
        test_ecbu = projet.get_test_ecbu_by_id(test_id)
        if not test_ecbu:
            raise HTTPException(status_code=404, detail="Test ECBU not found")
        return {"test_ecbu": test_ecbu}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_test_ecbu/{test_id}")
def update_test_ecbu_route(test_id: int, updated_data: dict):
    try:
        projet.update_test_ecbu(test_id, updated_data)
        return {"message": "Test ECBU updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_test_ecbu/{test_id}")
def delete_test_ecbu_route(test_id: int):
    try:
        projet.delete_test_ecbu(test_id)
        return {"message": "Test ECBU deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Facture ECBU routes
@app.post("/add_facture_ecbu")
def add_facture_ecbu_route(
    ID_FACTURE_ECBU: int = Form(...),
    MONTANT: float = Form(...),
    DATE_FACTURATION: str = Form(...),
    EXAMENS_REMBOURSES: str = Form(...),
    EXAMENS_NON_REMBOURSES: str = Form(...),
    MODE_REGLEMENT: str = Form(...),
    PART_SS: float = Form(...),
    PART_MUTUELLE: float = Form(...),
    RESTE_A_CHARGE: float = Form(...),
):
    try:
        facture_data = {
            'ID_FACTURE_ECBU': ID_FACTURE_ECBU,
            'MONTANT': MONTANT,
            'DATE_FACTURATION': DATE_FACTURATION,
            'EXAMENS_REMBOURSES': EXAMENS_REMBOURSES,
            'EXAMENS_NON_REMBOURSES': EXAMENS_NON_REMBOURSES,
            'MODE_REGLEMENT': MODE_REGLEMENT,
            'PART_SS': PART_SS,
            'PART_MUTUELLE': PART_MUTUELLE,
            'RESTE_A_CHARGE': RESTE_A_CHARGE,
        }

        projet.add_facture_ecbu(facture_data)

        return {"message": "Facture ECBU added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_factures_ecbu")
def get_all_factures_ecbu_route():
    try:
        factures_ecbu = projet.get_all_factures_ecbu()
        return {"factures_ecbu": factures_ecbu}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_facture_ecbu/{facture_id}")
def get_facture_ecbu_by_id_route(facture_id: int):
    try:
        facture_ecbu = projet.get_facture_ecbu_by_id(facture_id)
        if not facture_ecbu:
            raise HTTPException(status_code=404, detail="Facture ECBU not found")
        return {"facture_ecbu": facture_ecbu}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_facture_ecbu/{facture_id}")
def update_facture_ecbu_route(facture_id: int, updated_data: dict):
    try:
        projet.update_facture_ecbu(facture_id, updated_data)
        return {"message": "Facture ECBU updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_facture_ecbu/{facture_id}")
def delete_facture_ecbu_route(facture_id: int):
    try:
        projet.delete_facture_ecbu(facture_id)
        return {"message": "Facture ECBU deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Test COVID routes
@app.post("/add_test_covid")
def add_test_covid_route(
    ID_TEST_COVID: int = Form(...),
    DATE_TEST_COVID: str = Form(...),
    HEURE_TEST_COVID: str = Form(...),
    ORIGINE_PRELEVEMENT: str = Form(...),
    METHODE_TEST: str = Form(...),
    PAYS_TEST: str = Form(...),
    RESULTAT_TEST_COVID: str = Form(...),
    ID_DOCTEUR: int = Form(...),
    ID_FACTURE_COVID: int = Form(...),
    ID_PATIENT: int = Form(...),
):
    try:
        test_data = {
            'ID_TEST_COVID': ID_TEST_COVID,
            'DATE_TEST_COVID': DATE_TEST_COVID,
            'HEURE_TEST_COVID': HEURE_TEST_COVID,
            'ORIGINE_PRELEVEMENT': ORIGINE_PRELEVEMENT,
            'METHODE_TEST': METHODE_TEST,
            'PAYS_TEST': PAYS_TEST,
            'RESULTAT_TEST_COVID': RESULTAT_TEST_COVID,
            'ID_DOCTEUR': ID_DOCTEUR,
            'ID_FACTURE_COVID': ID_FACTURE_COVID,
            'ID_PATIENT': ID_PATIENT,
        }

        projet.add_test_covid(test_data)

        return {"message": "Test COVID added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_tests_covid")
def get_all_tests_covid_route():
    try:
        tests_covid = projet.get_all_tests_covid()
        return {"tests_covid": tests_covid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_test_covid/{test_id}")
def get_test_covid_by_id_route(test_id: int):
    try:
        test_covid = projet.get_test_covid_by_id(test_id)
        if not test_covid:
            raise HTTPException(status_code=404, detail="Test COVID not found")
        return {"test_covid": test_covid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_test_covid/{test_id}")
def update_test_covid_route(test_id: int, updated_data: dict):
    try:
        projet.update_test_covid(test_id, updated_data)
        return {"message": "Test COVID updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_test_covid/{test_id}")
def delete_test_covid_route(test_id: int):
    try:
        projet.delete_test_covid(test_id)
        return {"message": "Test COVID deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Facture Test COVID routes
@app.post("/add_facture_test_covid")
def add_facture_test_covid_route(
    ID_FACTURE_COVID: int = Form(...),
    MONTANT: float = Form(...),
    DATE_FACTURATION: str = Form(...),
    EXAMENS_REMBOURSES: str = Form(...),
    EXAMENS_NON_REMBOURSES: str = Form(...),
    MODE_REGLEMENT: str = Form(...),
    PART_SS: float = Form(...),
    PART_MUTUELLE: float = Form(...),
    RESTE_A_CHARGE: float = Form(...),
):
    try:
        facture_data = {
            'ID_FACTURE_COVID': ID_FACTURE_COVID,
            'MONTANT': MONTANT,
            'DATE_FACTURATION': DATE_FACTURATION,
            'EXAMENS_REMBOURSES': EXAMENS_REMBOURSES,
            'EXAMENS_NON_REMBOURSES': EXAMENS_NON_REMBOURSES,
            'MODE_REGLEMENT': MODE_REGLEMENT,
            'PART_SS': PART_SS,
            'PART_MUTUELLE': PART_MUTUELLE,
            'RESTE_A_CHARGE': RESTE_A_CHARGE,
        }

        projet.add_facture_test_covid(facture_data)

        return {"message": "Facture Test COVID added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_factures_test_covid")
def get_all_factures_test_covid_route():
    try:
        factures_test_covid = projet.get_all_factures_test_covid()
        return {"factures_test_covid": factures_test_covid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_facture_test_covid/{facture_id}")
def get_facture_test_covid_by_id_route(facture_id: int):
    try:
        facture_test_covid = projet.get_facture_test_covid_by_id(facture_id)
        if not facture_test_covid:
            raise HTTPException(status_code=404, detail="Facture Test COVID not found")
        return {"facture_test_covid": facture_test_covid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_facture_test_covid/{facture_id}")
def update_facture_test_covid_route(facture_id: int, updated_data: dict):
    try:
        projet.update_facture_test_covid(facture_id, updated_data)
        return {"message": "Facture Test COVID updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_facture_test_covid/{facture_id}")
def delete_facture_test_covid_route(facture_id: int):
    try:
        projet.delete_facture_test_covid(facture_id)
        return {"message": "Facture Test COVID deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 



# Test Allergie routes
@app.post("/add_test_allergie")
def add_test_allergie_route(
    ID_TEST_ALLERGIE: int = Form(...),
    DATE_TEST_ALLERGIE: str = Form(...),
    HEURE_TEST_ALLERGIE: str = Form(...),
    TYPE_TEST: str = Form(...),
    ALLERGENE_TESTE: str = Form(...),
    DOSAGE_LGE_SANG: float = Form(...),
    RESULTATS: str = Form(...),
    TYPE_ALLERGIE: str = Form(...),
    ID_DOCTEUR: int = Form(...),
    ID_FACTURE_ALLERGIE: int = Form(...),
    ID_PATIENT: int = Form(...),
):
    try:
        test_data = {
            'ID_TEST_ALLERGIE': ID_TEST_ALLERGIE,
            'DATE_TEST_ALLERGIE': DATE_TEST_ALLERGIE,
            'HEURE_TEST_ALLERGIE': HEURE_TEST_ALLERGIE,
            'TYPE_TEST': TYPE_TEST,
            'ALLERGENE_TESTE': ALLERGENE_TESTE,
            'DOSAGE_LGE_SANG': DOSAGE_LGE_SANG,
            'RESULTATS': RESULTATS,
            'TYPE_ALLERGIE': TYPE_ALLERGIE,
            'ID_DOCTEUR': ID_DOCTEUR,
            'ID_FACTURE_ALLERGIE': ID_FACTURE_ALLERGIE,
            'ID_PATIENT': ID_PATIENT,
        }

        projet.add_test_allergie(test_data)

        return {"message": "Test Allergie added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_tests_allergie")
def get_all_tests_allergie_route():
    try:
        tests_allergie = projet.get_all_tests_allergie()
        return {"tests_allergie": tests_allergie}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_test_allergie/{test_id}")
def get_test_allergie_by_id_route(test_id: int):
    try:
        test_allergie = projet.get_test_allergie_by_id(test_id)
        if not test_allergie:
            raise HTTPException(status_code=404, detail="Test Allergie not found")
        return {"test_allergie": test_allergie}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_test_allergie/{test_id}")
def update_test_allergie_route(test_id: int, updated_data: dict):
    try:
        projet.update_test_allergie(test_id, updated_data)
        return {"message": "Test Allergie updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_test_allergie/{test_id}")
def delete_test_allergie_route(test_id: int):
    try:
        projet.delete_test_allergie(test_id)
        return {"message": "Test Allergie deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Facture Test Allergie routes
@app.post("/add_facture_test_allergie")
def add_facture_test_allergie_route(
    ID_FACTURE_ALLERGIE: int = Form(...),
    MONTANT: float = Form(...),
    DATE_FACTURATION: str = Form(...),
    EXAMENS_REMBOURSES: str = Form(...),
    EXAMENS_NON_REMBOURSES: str = Form(...),
    MODE_REGLEMENT: str = Form(...),
    PART_SS: float = Form(...),
    PART_MUTUELLE: float = Form(...),
    RESTE_A_CHARGE: float = Form(...),
):
    try:
        facture_data = {
            'ID_FACTURE_ALLERGIE': ID_FACTURE_ALLERGIE,
            'MONTANT': MONTANT,
            'DATE_FACTURATION': DATE_FACTURATION,
            'EXAMENS_REMBOURSES': EXAMENS_REMBOURSES,
            'EXAMENS_NON_REMBOURSES': EXAMENS_NON_REMBOURSES,
            'MODE_REGLEMENT': MODE_REGLEMENT,
            'PART_SS': PART_SS,
            'PART_MUTUELLE': PART_MUTUELLE,
            'RESTE_A_CHARGE': RESTE_A_CHARGE,
        }

        projet.add_facture_test_allergie(facture_data)

        return {"message": "Facture Test Allergie added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_factures_test_allergie")
def get_all_factures_test_allergie_route():
    try:
        factures_test_allergie = projet.get_all_factures_test_allergie()
        return {"factures_test_allergie": factures_test_allergie}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_facture_test_allergie/{facture_id}")
def get_facture_test_allergie_by_id_route(facture_id: int):
    try:
        facture_test_allergie = projet.get_facture_test_allergie_by_id(facture_id)
        if not facture_test_allergie:
            raise HTTPException(status_code=404, detail="Facture Test Allergie not found")
        return {"facture_test_allergie": facture_test_allergie}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_facture_test_allergie/{facture_id}")
def update_facture_test_allergie_route(facture_id: int, updated_data: dict):
    try:
        projet.update_facture_test_allergie(facture_id, updated_data)
        return {"message": "Facture Test Allergie updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_facture_test_allergie/{facture_id}")
def delete_facture_test_allergie_route(facture_id: int):
    try:
        projet.delete_facture_test_allergie(facture_id)
        return {"message": "Facture Test Allergie deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve the HTML file
app.mount("/", StaticFiles(directory=".", html=True), name="static")