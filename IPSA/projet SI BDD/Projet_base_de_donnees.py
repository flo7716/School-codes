import sqlite3,datetime,random

from typing import Union

from fastapi import FastAPI 

app = FastAPI()



# Fonction pour se connecter à la base de données
def connect_database():
    connection = sqlite3.connect("CABINETMEDICAL.db")
    cursor = connection.cursor()
    return connection, cursor


connection, cursor = connect_database()

# Fonction générique pour générer un ID unique pour une entité
def generate_unique_id(entity_name, id_column, cursor):
    new_id = random.randint(1, 1000)
    connection, cursor = connect_database()
    while get_entity_by_id(entity_name, id_column, new_id, cursor) is not None:
        new_id = random.randint(1, 1000)

    return new_id

# Fonction générique pour obtenir un enregistrement par ID
def get_entity_by_id(entity_name, id_column, entity_id, cursor):
    cursor.execute(f"SELECT * FROM {entity_name} WHERE {id_column}=?", (entity_id,))
    entity = cursor.fetchone()
    return entity



# Fonction pour ajouter un docteur
def add_doctor(doctor_data):
    # Add a new doctor to the database
    connection, cursor = connect_database()
    try:
        # Perform the insertion
        cursor.execute("INSERT INTO DOCTEUR (ID_DOCTEUR, NOM_DOC, PRENOM_DOC, TITRE_DOC, SPE_DOC, EXPERTISES_DOC, MDP_DOC) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (doctor_data['ID_DOCTEUR'], doctor_data['NOM_DOC'], doctor_data['PRENOM_DOC'], doctor_data['TITRE_DOC'],
                        doctor_data['SPE_DOC'], doctor_data['EXPERTISES_DOC'], doctor_data['MDP_DOC']))
        connection.commit()
        print("Doctor added successfully.")
    except Exception as e:
        print(f"Error adding doctor: {e}")
    finally:
        connection.close()

# Fonction pour sélectionner tous les docteurs
def get_all_doctors():
    # Retrieve all doctors from the database
    connection, cursor = connect_database()
    try:
        cursor.execute("SELECT * FROM DOCTEUR")
        doctors = cursor.fetchall()
        return doctors
    except Exception as e:
        print(f"Error retrieving doctors: {e}")
    finally:
        connection.close()

# Fonction pour sélectionner un docteur par ID
def get_doctor_by_id(doctor_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM DOCTEUR WHERE ID_DOCTEUR=?", (doctor_id,))
    doctor = cursor.fetchone()
    connection.close()
    return doctor




# Fonction pour mettre à jour les informations d'un docteur
def update_doctor(doctor_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE DOCTEUR SET NOM_DOC=?, PRENOM_DOC=?, TITRE_DOC=?, SPE_DOC=?, EXPERTISES_DOC=?, MDP_DOC=? WHERE ID_DOCTEUR=?",
                   (updated_data['NOM_DOC'], updated_data['PRENOM_DOC'], updated_data['TITRE_DOC'],
                    updated_data['SPE_DOC'], updated_data['EXPERTISES_DOC'], updated_data['MDP_DOC'], doctor_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer un docteur par ID
def delete_doctor(doctor_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM DOCTEUR WHERE ID_DOCTEUR=?", (doctor_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter un patient
def add_patient(patient_data):
    # Add a new patient to the database
    connection, cursor = connect_database()
    try:
        # Perform the insertion
        cursor.execute("INSERT INTO PATIENT (ID_PATIENT, NOM_PATIENT, PRENOM_PATIENT, DATE_NAISSANCE, N_SS, N_MUTUELLE, ADRESSE, CP, VILLE, CEDEX, TELEPHONE, ADRESSE_MAIL, NOM_MEDECIN_TRAITANT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (patient_data['ID_PATIENT'], patient_data['NOM_PATIENT'], patient_data['PRENOM_PATIENT'], patient_data['DATE_NAISSANCE'],
                        patient_data['N_SS'], patient_data['N_MUTUELLE'], patient_data['ADRESSE'], patient_data['CP'], patient_data['VILLE'],
                        patient_data['CEDEX'], patient_data['TELEPHONE'], patient_data['ADRESSE_MAIL'], patient_data['NOM_MEDECIN_TRAITANT']))
        connection.commit()
        print("Patient added successfully.")
    except Exception as e:
        print(f"Error adding patient: {e}")
    finally:
        connection.close()

# Fonction pour sélectionner tous les patients
def get_all_patients():
    # Retrieve all patients from the database
    connection, cursor = connect_database()
    try:
        cursor.execute("SELECT * FROM PATIENT")
        patients = cursor.fetchall()
        return patients
    except Exception as e:
        print(f"Error retrieving patients: {e}")
    finally:
        connection.close()

# Fonction pour sélectionner un patient par ID
def get_patient_by_id(patient_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM PATIENT WHERE ID_PATIENT=?", (patient_id,))
    patient = cursor.fetchone()
    connection.close()
    return patient

# Fonction pour mettre à jour les informations d'un patient
def update_patient(patient_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE PATIENT SET NOM_PATIENT=?, PRENOM_PATIENT=?, DATE_NAISSANCE=?, N_SS=?, N_MUTUELLE=?, ADRESSE=?, CP=?, VILLE=?, CEDEX=?, TELEPHONE=?, ADRESSE_MAIL=?, NOM_MEDECIN_TRAITANT=? WHERE ID_PATIENT=?",
                   (updated_data['NOM_PATIENT'], updated_data['PRENOM_PATIENT'], updated_data['DATE_NAISSANCE'], updated_data['N_SS'],
                    updated_data['N_MUTUELLE'], updated_data['ADRESSE'], updated_data['CP'], updated_data['VILLE'], updated_data['CEDEX'],
                    updated_data['TELEPHONE'], updated_data['ADRESSE_MAIL'], updated_data['NOM_MEDECIN_TRAITANT'], patient_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer un patient par ID
def delete_patient(patient_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM PATIENT WHERE ID_PATIENT=?", (patient_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter un receptionniste
def add_receptionist(receptionist_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO RECEPTIONNISTE (ID_RECEPTIONNISTE, NOM_RECEP, PRENOM_RECEP, MDP_RECEP) VALUES (?, ?, ?, ?)",
                   (receptionist_data['ID_RECEPTIONNISTE'], receptionist_data['NOM_RECEP'], receptionist_data['PRENOM_RECEP'], receptionist_data['MDP_RECEP']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner tous les receptionnistes
def get_all_receptionists():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM RECEPTIONNISTE")
    receptionists = cursor.fetchall()
    connection.close()
    return receptionists

# Fonction pour sélectionner un receptionniste par ID
def get_receptionist_by_id(receptionist_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM RECEPTIONNISTE WHERE ID_RECEPTIONNISTE=?", (receptionist_id,))
    receptionist = cursor.fetchone()
    connection.close()
    return receptionist

# Fonction pour mettre à jour les informations d'un receptionniste
def update_receptionist(receptionist_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE RECEPTIONNISTE SET NOM_RECEP=?, PRENOM_RECEP=?, MDP_RECEP=? WHERE ID_RECEPTIONNISTE=?",
                   (updated_data['NOM_RECEP'], updated_data['PRENOM_RECEP'], updated_data['MDP_RECEP'], receptionist_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer un receptionniste par ID
def delete_receptionist(receptionist_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM RECEPTIONNISTE WHERE ID_RECEPTIONNISTE=?", (receptionist_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter un rendez-vous
def add_rdv(rdv_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO RDV (ID_RDV, DATE_RDV, HEURE_RDV, ETAT_RDV, SALLE_EXAMEN, ID_PATIENT, ID_DOCTEUR) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (rdv_data['ID_RDV'], rdv_data['DATE_RDV'], rdv_data['HEURE_RDV'], rdv_data['ETAT_RDV'],
                    rdv_data['SALLE_EXAMEN'], rdv_data['ID_PATIENT'], rdv_data['ID_DOCTEUR']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner tous les rendez-vous
def get_all_rdvs():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM RDV")
    rdvs = cursor.fetchall()
    connection.close()
    return rdvs

# Fonction pour sélectionner un rendez-vous par ID
def get_rdv_by_id(rdv_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM RDV WHERE ID_RDV=?", (rdv_id,))
    rdv = cursor.fetchone()
    connection.close()
    return rdv

# Fonction pour mettre à jour les informations d'un rendez-vous
def update_rdv(rdv_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE RDV SET DATE_RDV=?, HEURE_RDV=?, ETAT_RDV=?, SALLE_EXAMEN=?, ID_PATIENT=?, ID_DOCTEUR=? WHERE ID_RDV=?",
                   (updated_data['DATE_RDV'], updated_data['HEURE_RDV'], updated_data['ETAT_RDV'], updated_data['SALLE_EXAMEN'],
                    updated_data['ID_PATIENT'], updated_data['ID_DOCTEUR'], rdv_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer un rendez-vous par ID
def delete_rdv(rdv_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM RDV WHERE ID_RDV=?", (rdv_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter un message
def add_message(message_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO MESSAGE (ID_MESSAGE, DATE_MESSAGE, QUESTION, REPONSE, ID_PATIENT) VALUES (?, ?, ?, ?, ?)",
                   (message_data['ID_MESSAGE'], message_data['DATE_MESSAGE'], message_data['QUESTION'],
                    message_data['REPONSE'], message_data['ID_PATIENT']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner tous les messages
def get_all_messages():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM MESSAGE")
    messages = cursor.fetchall()
    connection.close()
    return messages

# Fonction pour sélectionner un message par ID
def get_message_by_id(message_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM MESSAGE WHERE ID_MESSAGE=?", (message_id,))
    message = cursor.fetchone()
    connection.close()
    return message

# Fonction pour mettre à jour les informations d'un message
def update_message(message_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE MESSAGE SET DATE_MESSAGE=?, QUESTION=?, REPONSE=?, ID_PATIENT=? WHERE ID_MESSAGE=?",
                   (updated_data['DATE_MESSAGE'], updated_data['QUESTION'], updated_data['REPONSE'],
                    updated_data['ID_PATIENT'], message_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer un message par ID
def delete_message(message_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM MESSAGE WHERE ID_MESSAGE=?", (message_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter une réponse
def add_reponse(reponse_data):
    connection, cursor = connect_database()
    try:
        cursor.execute("INSERT INTO REPONSE (ID_REPONSE, DATE_REPONSE, QUESTION, REPONSE, ID_MESSAGE, ID_DOCTEUR) VALUES (?, ?, ?, ?, ?, ?)",
                       (reponse_data['ID_REPONSE'], reponse_data['DATE_REPONSE'], reponse_data['QUESTION'],
                        reponse_data['REPONSE'], reponse_data['ID_MESSAGE'], reponse_data['ID_DOCTEUR']))
        connection.commit()
    except Exception as e:
        print(f"Error adding response: {e}")
    finally:
        connection.close()

# Fonction pour sélectionner toutes les réponses
def get_all_reponses():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM REPONSE")
    reponses = cursor.fetchall()
    connection.close()
    return reponses

# Fonction pour sélectionner une réponse par ID
def get_reponse_by_id(reponse_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM REPONSE WHERE ID_REPONSE=?", (reponse_id,))
    reponse = cursor.fetchone()
    connection.close()
    return reponse

# Fonction pour mettre à jour les informations d'une réponse
def update_reponse(reponse_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE REPONSE SET DATE_REPONSE=?, QUESTION=?, REPONSE=?, ID_MESSAGE=? WHERE ID_REPONSE=?",
                   (updated_data['DATE_REPONSE'], updated_data['QUESTION'], updated_data['REPONSE'],
                    updated_data['ID_MESSAGE'], reponse_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer une réponse par ID
def delete_reponse(reponse_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM REPONSE WHERE ID_REPONSE=?", (reponse_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter une relation entre un docteur et un message (Repondre)
def add_repondre(repondre_data):
    connection, cursor = connect_database()
    try:
        # Check if the relationship already exists
        cursor.execute("SELECT * FROM REPONDRE WHERE ID_DOCTEUR = ? AND ID_MESSAGE = ?",
                       (repondre_data['ID_DOCTEUR'], repondre_data['ID_MESSAGE']))
        existing_relationship = cursor.fetchone()

        if existing_relationship:
            # Update the existing relationship (you might want to handle this differently)
            print("Relationship already exists. You might want to update it.")
        else:
            # Insert the new relationship
            cursor.execute("INSERT INTO REPONDRE (ID_DOCTEUR, ID_MESSAGE) VALUES (?, ?)",
                           (repondre_data['ID_DOCTEUR'], repondre_data['ID_MESSAGE']))
            connection.commit()
            print("Relationship added successfully.")

    except Exception as e:
        print(f"Error adding relationship: {e}")
    finally:
        connection.close()


# Fonction pour sélectionner toutes les relations Repondre
def get_all_repondre():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM REPONDRE")
    repondre_relations = cursor.fetchall()
    connection.close()
    return repondre_relations

# Fonction pour supprimer une relation Repondre par ID_DOCTEUR et ID_MESSAGE
def delete_repondre(docteur_id, message_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM REPONDRE WHERE ID_DOCTEUR=? AND ID_MESSAGE=?", (docteur_id, message_id))
    connection.commit()
    connection.close()


# Fonction pour ajouter une prise de sang
def add_prise_sang(prise_sang_data):
    connection, cursor = connect_database()
    
    # Ajout d'un print pour vérifier le type de l'ID
    print("Type de l'ID_PRISE_SANG :", type(prise_sang_data['ID_PRISE_SANG']))
    
    cursor.execute("INSERT INTO PRISE_SANG (ID_PRISE_SANG, DATE_PRISE_SANG, GROUPE_SANGUIN, HEMOGRAMME, DOSAGE_FERRITINE, "
                   "VS, CRP, GLYCEMIE, LDL, HDL, CHOLESTEROL_TOTAL, BILAN_RENAL, BILAN_HEPATIQUE, ID_DOCTEUR, ID_FACTURE_PS, "
                   "ID_PATIENT) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (prise_sang_data['ID_PRISE_SANG'], prise_sang_data['DATE_PRISE_SANG'],
                    prise_sang_data['GROUPE_SANGUIN'], prise_sang_data['HEMOGRAMME'],
                    prise_sang_data['DOSAGE_FERRITINE'], prise_sang_data['VS'],
                    prise_sang_data['CRP'], prise_sang_data['GLYCEMIE'], prise_sang_data['LDL'],
                    prise_sang_data['HDL'], prise_sang_data['CHOLESTEROL_TOTAL'],
                    prise_sang_data['BILAN_RENAL'], prise_sang_data['BILAN_HEPATIQUE'],
                    prise_sang_data['ID_DOCTEUR'], prise_sang_data['ID_FACTURE_PS'],
                    prise_sang_data['ID_PATIENT']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner toutes les prises de sang
def get_all_prises_sang():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM PRISE_SANG")
    prises_sang = cursor.fetchall()
    connection.close()
    return prises_sang

# Fonction pour sélectionner une prise de sang par ID
def get_prise_sang_by_id(prise_sang_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM PRISE_SANG WHERE ID_PRISE_SANG=?", (prise_sang_id,))
    prise_sang = cursor.fetchone()
    connection.close()
    return prise_sang

# Fonction pour mettre à jour les informations d'une prise de sang
def update_prise_sang(prise_sang_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE PRISE_SANG SET DATE_PRISE_SANG=?, GROUPE_SANGUIN=?, HEMOGRAMME=?, DOSAGE_FERRITINE=?, "
                   "VS=?, CRP=?, GLYCEMIE=?, LDL=?, HDL=?, CHOLESTEROL_TOTAL=?, BILAN_RENAL=?, BILAN_HEPATIQUE=?, "
                   "ID_DOCTEUR=?, ID_FACTURE_PS=?, ID_PATIENT=? WHERE ID_PRISE_SANG=?",
                   (updated_data['DATE_PRISE_SANG'], updated_data['GROUPE_SANGUIN'], updated_data['HEMOGRAMME'],
                    updated_data['DOSAGE_FERRITINE'], updated_data['VS'], updated_data['CRP'], updated_data['GLYCEMIE'],
                    updated_data['LDL'], updated_data['HDL'], updated_data['CHOLESTEROL_TOTAL'], updated_data['BILAN_RENAL'],
                    updated_data['BILAN_HEPATIQUE'], updated_data['ID_DOCTEUR'], updated_data['ID_FACTURE_PS'],
                    updated_data['ID_PATIENT'], prise_sang_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer une prise de sang par ID
def delete_prise_sang(prise_sang_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM PRISE_SANG WHERE ID_PRISE_SANG=?", (prise_sang_id,))
    connection.commit()
    connection.close()

# Fonction pour ajouter une facture de prise de sang
def add_facture_prise_sang(facture_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO FACTURE_PRISE_SANG (ID_FACTURE_PS, MONTANT, DATE_FACTURATION, MODE_REGLEMENT, EXAMENS_REMBOURSES, EXAMENS_NON_REMBOURSES, PART_SS, PART_MUTUELLE, RESTE_A_CHARGE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (facture_data['ID_FACTURE_PS'], facture_data['MONTANT'], facture_data['DATE_FACTURATION'],
                    facture_data['MODE_REGLEMENT'], facture_data['EXAMENS_REMBOURSES'], facture_data['EXAMENS_NON_REMBOURSES'],
                    facture_data['PART_SS'], facture_data['PART_MUTUELLE'], facture_data['RESTE_A_CHARGE']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner toutes les factures de prise de sang
def get_all_factures_prise_sang():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM FACTURE_PRISE_SANG")
    factures_prise_sang = cursor.fetchall()
    connection.close()
    return factures_prise_sang

# Fonction pour sélectionner une facture de prise de sang par ID
def get_facture_prise_sang_by_id(facture_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM FACTURE_PRISE_SANG WHERE ID_FACTURE_PS=?", (facture_id,))
    facture_prise_sang = cursor.fetchone()
    connection.close()
    return facture_prise_sang

# Fonction pour mettre à jour les informations d'une facture de prise de sang
def update_facture_prise_sang(facture_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE FACTURE_PRISE_SANG SET MONTANT=?, DATE_FACTURATION=?, MODE_REGLEMENT=?, EXAMENS_REMBOURSES=?, EXAMENS_NON_REMBOURSES=?, PART_SS=?, PART_MUTUELLE=?, RESTE_A_CHARGE=? WHERE ID_FACTURE_PS=?",
                   (updated_data['MONTANT'], updated_data['DATE_FACTURATION'], updated_data['MODE_REGLEMENT'],
                    updated_data['EXAMENS_REMBOURSES'], updated_data['EXAMENS_NON_REMBOURSES'], updated_data['PART_SS'],
                    updated_data['PART_MUTUELLE'], updated_data['RESTE_A_CHARGE'], facture_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer une facture de prise de sang par ID
def delete_facture_prise_sang(facture_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM FACTURE_PRISE_SANG WHERE ID_FACTURE_PS=?", (facture_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter un test ECBU
def add_test_ecbu(test_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO ECBU (ID_FLACON_URINE, DATE_ECBU, QTE_LEUCOCYTES, QTE_HEMATIES, QTE_CELLULES_EPITHELIALES, QTE_CRISTAUX, QTE_HYALINS, QTE_GERMES_URINES, ANTIBIOGRAMME, BACTERIURIE, ID_DOCTEUR, ID_FACTURE_ECBU, ID_PATIENT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (test_data['ID_FLACON_URINE'], test_data['DATE_ECBU'], test_data['QTE_LEUCOCYTES'],
                    test_data['QTE_HEMATIES'], test_data['QTE_CELLULES_EPITHELIALES'], test_data['QTE_CRISTAUX'],
                    test_data['QTE_HYALINS'], test_data['QTE_GERMES_URINES'], test_data['ANTIBIOGRAMME'],
                    test_data['BACTERIURIE'], test_data['ID_DOCTEUR'], test_data['ID_FACTURE_ECBU'],
                    test_data['ID_PATIENT']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner tous les tests ECBU
def get_all_tests_ecbu():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM ECBU")
    tests_ecbu = cursor.fetchall()
    connection.close()
    return tests_ecbu

# Fonction pour sélectionner un test ECBU par ID
def get_test_ecbu_by_id(test_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM ECBU WHERE ID_FLACON_URINE=?", (test_id,))
    test_ecbu = cursor.fetchone()
    connection.close()
    return test_ecbu

# Fonction pour mettre à jour les informations d'un test ECBU
def update_test_ecbu(test_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE ECBU SET DATE_ECBU=?, QTE_LEUCOCYTES=?, QTE_HEMATIES=?, QTE_CELLULES_EPITHELIALES=?, QTE_CRISTAUX=?, QTE_HYALINS=?, QTE_GERMES_URINES=?, ANTIBIOGRAMME=?, BACTERIURIE=?, ID_DOCTEUR=?, ID_FACTURE_ECBU=?, ID_PATIENT=? WHERE ID_FLACON_URINE=?",
                   (updated_data['DATE_ECBU'], updated_data['QTE_LEUCOCYTES'], updated_data['QTE_HEMATIES'],
                    updated_data['QTE_CELLULES_EPITHELIALES'], updated_data['QTE_CRISTAUX'], updated_data['QTE_HYALINS'],
                    updated_data['QTE_GERMES_URINES'], updated_data['ANTIBIOGRAMME'], updated_data['BACTERIURIE'],
                    updated_data['ID_DOCTEUR'], updated_data['ID_FACTURE_ECBU'], updated_data['ID_PATIENT'], test_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer un test ECBU par ID
def delete_test_ecbu(test_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM ECBU WHERE ID_FLACON_URINE=?", (test_id,))
    connection.commit()
    connection.close() 

# Fonction pour ajouter une facture ECBU
def add_facture_ecbu(facture_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO FACTURE_ECBU (ID_FACTURE_ECBU, MONTANT, DATE_FACTURATION, EXAMENS_REMBOURSES, EXAMENS_NON_REMBOURSES, MODE_REGLEMENT, PART_SS, PART_MUTUELLE, RESTE_A_CHARGE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (facture_data['ID_FACTURE_ECBU'], facture_data['MONTANT'], facture_data['DATE_FACTURATION'],
                    facture_data['EXAMENS_REMBOURSES'], facture_data['EXAMENS_NON_REMBOURSES'], facture_data['MODE_REGLEMENT'],
                    facture_data['PART_SS'], facture_data['PART_MUTUELLE'], facture_data['RESTE_A_CHARGE']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner toutes les factures ECBU
def get_all_factures_ecbu():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM FACTURE_ECBU")
    factures_ecbu = cursor.fetchall()
    connection.close()
    return factures_ecbu

# Fonction pour sélectionner une facture ECBU par ID
def get_facture_ecbu_by_id(facture_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM FACTURE_ECBU WHERE ID_FACTURE_ECBU=?", (facture_id,))
    facture_ecbu = cursor.fetchone()
    connection.close()
    return facture_ecbu

# Fonction pour mettre à jour les informations d'une facture ECBU
def update_facture_ecbu(facture_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE FACTURE_ECBU SET MONTANT=?, DATE_FACTURATION=?, EXAMENS_REMBOURSES=?, EXAMENS_NON_REMBOURSES=?, MODE_REGLEMENT=?, PART_SS=?, PART_MUTUELLE=?, RESTE_A_CHARGE=? WHERE ID_FACTURE_ECBU=?",
                   (updated_data['MONTANT'], updated_data['DATE_FACTURATION'], updated_data['EXAMENS_REMBOURSES'],
                    updated_data['EXAMENS_NON_REMBOURSES'], updated_data['MODE_REGLEMENT'], updated_data['PART_SS'],
                    updated_data['PART_MUTUELLE'], updated_data['RESTE_A_CHARGE'], facture_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer une facture ECBU par ID
def delete_facture_ecbu(facture_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM FACTURE_ECBU WHERE ID_FACTURE_ECBU=?", (facture_id,))
    connection.commit()
    connection.close()

# Fonction pour ajouter un test COVID
def add_test_covid(test_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO TEST_COVID (ID_TEST_COVID, DATE_TEST_COVID, HEURE_TEST_COVID, ORIGINE_PRELEVEMENT, METHODE_TEST, PAYS_TEST, RESULTAT_TEST_COVID, ID_DOCTEUR, ID_FACTURE_COVID, ID_PATIENT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (test_data['ID_TEST_COVID'], test_data['DATE_TEST_COVID'], test_data['HEURE_TEST_COVID'],
                    test_data['ORIGINE_PRELEVEMENT'], test_data['METHODE_TEST'], test_data['PAYS_TEST'],
                    test_data['RESULTAT_TEST_COVID'], test_data['ID_DOCTEUR'], test_data['ID_FACTURE_COVID'],
                    test_data['ID_PATIENT']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner tous les tests COVID
def get_all_tests_covid():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM TEST_COVID")
    tests_covid = cursor.fetchall()
    connection.close()
    return tests_covid

# Fonction pour sélectionner un test COVID par ID
def get_test_covid_by_id(test_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM TEST_COVID WHERE ID_TEST_COVID=?", (test_id,))
    test_covid = cursor.fetchone()
    connection.close()
    return test_covid

# Fonction pour mettre à jour les informations d'un test COVID
def update_test_covid(test_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE TEST_COVID SET DATE_TEST_COVID=?, HEURE_TEST_COVID=?, ORIGINE_PRELEVEMENT=?, METHODE_TEST=?, PAYS_TEST=?, RESULTAT_TEST_COVID=?, ID_DOCTEUR=?, ID_FACTURE_COVID=?, ID_PATIENT=? WHERE ID_TEST_COVID=?",
                   (updated_data['DATE_TEST_COVID'], updated_data['HEURE_TEST_COVID'],
                    updated_data['ORIGINE_PRELEVEMENT'], updated_data['METHODE_TEST'], updated_data['PAYS_TEST'],
                    updated_data['RESULTAT_TEST_COVID'], updated_data['ID_DOCTEUR'], updated_data['ID_FACTURE_COVID'],
                    updated_data['ID_PATIENT'], test_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer un test COVID par ID
def delete_test_covid(test_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM TEST_COVID WHERE ID_TEST_COVID=?", (test_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter une facture Test COVID
def add_facture_test_covid(facture_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO FACTURE_TEST_COVID (ID_FACTURE_COVID, MONTANT, DATE_FACTURATION, EXAMENS_REMBOURSES, EXAMENS_NON_REMBOURSES, MODE_REGLEMENT, PART_SS, PART_MUTUELLE, RESTE_A_CHARGE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (facture_data['ID_FACTURE_COVID'], facture_data['MONTANT'], facture_data['DATE_FACTURATION'],
                    facture_data['EXAMENS_REMBOURSES'], facture_data['EXAMENS_NON_REMBOURSES'],
                    facture_data['MODE_REGLEMENT'], facture_data['PART_SS'], facture_data['PART_MUTUELLE'],
                    facture_data['RESTE_A_CHARGE']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner toutes les factures Test COVID
def get_all_factures_test_covid():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM FACTURE_TEST_COVID")
    factures_test_covid = cursor.fetchall()
    connection.close()
    return factures_test_covid

# Fonction pour sélectionner une facture Test COVID par ID
def get_facture_test_covid_by_id(facture_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM FACTURE_TEST_COVID WHERE ID_FACTURE_COVID=?", (facture_id,))
    facture_test_covid = cursor.fetchone()
    connection.close()
    return facture_test_covid

# Fonction pour mettre à jour les informations d'une facture Test COVID
def update_facture_test_covid(facture_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE FACTURE_TEST_COVID SET MONTANT=?, DATE_FACTURATION=?, EXAMENS_REMBOURSES=?, EXAMENS_NON_REMBOURSES=?, MODE_REGLEMENT=?, PART_SS=?, PART_MUTUELLE=?, RESTE_A_CHARGE=? WHERE ID_FACTURE_COVID=?",
                   (updated_data['MONTANT'], updated_data['DATE_FACTURATION'], updated_data['EXAMENS_REMBOURSES'],
                    updated_data['EXAMENS_NON_REMBOURSES'], updated_data['MODE_REGLEMENT'], updated_data['PART_SS'],
                    updated_data['PART_MUTUELLE'], updated_data['RESTE_A_CHARGE'], facture_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer une facture Test COVID par ID
def delete_facture_test_covid(facture_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM FACTURE_TEST_COVID WHERE ID_FACTURE_COVID=?", (facture_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter un test allergie
def add_test_allergie(test_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO TEST_ALLERGIE (ID_TEST_ALLERGIE, DATE_TEST_ALLERGIE, HEURE_TEST_ALLERGIE, TYPE_TEST, ALLERGENE_TESTE, DOSAGE_LGE_SANG, RESULTATS, TYPE_ALLERGIE, ID_DOCTEUR, ID_FACTURE_ALLERGIE, ID_PATIENT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (test_data['ID_TEST_ALLERGIE'], test_data['DATE_TEST_ALLERGIE'], test_data['HEURE_TEST_ALLERGIE'],
                    test_data['TYPE_TEST'], test_data['ALLERGENE_TESTE'], test_data['DOSAGE_LGE_SANG'],
                    test_data['RESULTATS'], test_data['TYPE_ALLERGIE'], test_data['ID_DOCTEUR'],
                    test_data['ID_FACTURE_ALLERGIE'], test_data['ID_PATIENT']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner tous les tests allergie
def get_all_tests_allergie():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM TEST_ALLERGIE")
    tests_allergie = cursor.fetchall()
    connection.close()
    return tests_allergie

# Fonction pour sélectionner un test allergie par ID
def get_test_allergie_by_id(test_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM TEST_ALLERGIE WHERE ID_TEST_ALLERGIE=?", (test_id,))
    test_allergie = cursor.fetchone()
    connection.close()
    return test_allergie

# Fonction pour mettre à jour les informations d'un test allergie
def update_test_allergie(test_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE TEST_ALLERGIE SET DATE_TEST_ALLERGIE=?, HEURE_TEST_ALLERGIE=?, TYPE_TEST=?, ALLERGENE_TESTE=?, DOSAGE_LGE_SANG=?, RESULTATS=?, TYPE_ALLERGIE=?, ID_DOCTEUR=?, ID_FACTURE_ALLERGIE=?, ID_PATIENT=? WHERE ID_TEST_ALLERGIE=?",
                   (updated_data['DATE_TEST_ALLERGIE'], updated_data['HEURE_TEST_ALLERGIE'],
                    updated_data['TYPE_TEST'], updated_data['ALLERGENE_TESTE'], updated_data['DOSAGE_LGE_SANG'],
                    updated_data['RESULTATS'], updated_data['TYPE_ALLERGIE'], updated_data['ID_DOCTEUR'],
                    updated_data['ID_FACTURE_ALLERGIE'], updated_data['ID_PATIENT'], test_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer un test allergie par ID
def delete_test_allergie(test_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM TEST_ALLERGIE WHERE ID_TEST_ALLERGIE=?", (test_id,))
    connection.commit()
    connection.close()


# Fonction pour ajouter une facture Test allergie
def add_facture_test_allergie(facture_data):
    connection, cursor = connect_database()
    cursor.execute("INSERT INTO FACTURE_TEST_ALLERGIE (ID_FACTURE_ALLERGIE, MONTANT, DATE_FACTURATION, EXAMENS_REMBOURSES, EXAMENS_NON_REMBOURSES, MODE_REGLEMENT, PART_SS, PART_MUTUELLE, RESTE_A_CHARGE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (facture_data['ID_FACTURE_ALLERGIE'], facture_data['MONTANT'], facture_data['DATE_FACTURATION'],
                    facture_data['EXAMENS_REMBOURSES'], facture_data['EXAMENS_NON_REMBOURSES'],
                    facture_data['MODE_REGLEMENT'], facture_data['PART_SS'], facture_data['PART_MUTUELLE'],
                    facture_data['RESTE_A_CHARGE']))
    connection.commit()
    connection.close()

# Fonction pour sélectionner toutes les factures Test allergie
def get_all_factures_test_allergie():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM FACTURE_TEST_ALLERGIE")
    factures_test_allergie = cursor.fetchall()
    connection.close()
    return factures_test_allergie

# Fonction pour sélectionner une facture Test allergie par ID
def get_facture_test_allergie_by_id(facture_id):
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM FACTURE_TEST_ALLERGIE WHERE ID_FACTURE_ALLERGIE=?", (facture_id,))
    facture_test_allergie = cursor.fetchone()
    connection.close()
    return facture_test_allergie

# Fonction pour mettre à jour les informations d'une facture Test allergie
def update_facture_test_allergie(facture_id, updated_data):
    connection, cursor = connect_database()
    cursor.execute("UPDATE FACTURE_TEST_ALLERGIE SET MONTANT=?, DATE_FACTURATION=?, EXAMENS_REMBOURSES=?, EXAMENS_NON_REMBOURSES=?, MODE_REGLEMENT=?, PART_SS=?, PART_MUTUELLE=?, RESTE_A_CHARGE=? WHERE ID_FACTURE_ALLERGIE=?",
                   (updated_data['MONTANT'], updated_data['DATE_FACTURATION'], updated_data['EXAMENS_REMBOURSES'],
                    updated_data['EXAMENS_NON_REMBOURSES'], updated_data['MODE_REGLEMENT'], updated_data['PART_SS'],
                    updated_data['PART_MUTUELLE'], updated_data['RESTE_A_CHARGE'], facture_id))
    connection.commit()
    connection.close()

# Fonction pour supprimer une facture Test allergie par ID
def delete_facture_test_allergie(facture_id):
    connection, cursor = connect_database()
    cursor.execute("DELETE FROM FACTURE_TEST_ALLERGIE WHERE ID_FACTURE_ALLERGIE=?", (facture_id,))
    connection.commit()
    connection.close()


