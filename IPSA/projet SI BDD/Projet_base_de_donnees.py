import sqlite3
from typing import Dict, Any, List, Union
from iam import authenticate_user, has_access

# Function to connect to the database
def connect_database():
    connection = sqlite3.connect("CABINETMEDICAL.db")
    cursor = connection.cursor()
    return connection, cursor

# Generic function to add an entity
def add_entity(user: str, entity: str, data: Dict[str, Any]):
    if not authenticate_user(user):
        print("Authentication failed.")
        return
    if not has_access(user, "add", entity):
        print("Access denied.")
        return
    connection, cursor = connect_database()
    try:
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data.values()])
        query = f"INSERT INTO {entity} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, tuple(data.values()))
        connection.commit()
        print(f"{entity.capitalize()} added successfully.")
    except Exception as e:
        print(f"Error adding {entity}: {e}")
        raise
    finally:
        connection.close()

# Generic function to retrieve all entities
def get_all_entities(user: str, entity: str) -> List[Dict[str, Any]]:
    if not authenticate_user(user):
        print("Authentication failed.")
        return []
    if not has_access(user, "view", entity):
        print("Access denied.")
        return []
    connection, cursor = connect_database()
    try:
        query = f"SELECT * FROM {entity}"
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        return [dict(zip(column_names, row)) for row in rows]
    except Exception as e:
        print(f"Error retrieving {entity}s: {e}")
        raise
    finally:
        connection.close()

# Generic function to retrieve an entity by ID
def get_entity_by_id(user: str, entity: str, entity_id: int, id_column: str = "ID"):
    if not authenticate_user(user):
        print("Authentication failed.")
        return None
    if not has_access(user, "view", entity):
        print("Access denied.")
        return None
    connection, cursor = connect_database()
    try:
        query = f"SELECT * FROM {entity} WHERE {id_column} = ?"
        cursor.execute(query, (entity_id,))
        row = cursor.fetchone()
        if row:
            column_names = [description[0] for description in cursor.description]
            return dict(zip(column_names, row))
        return None
    except Exception as e:
        print(f"Error retrieving {entity} with ID {entity_id}: {e}")
        raise
    finally:
        connection.close()

# Generic function to update an entity
def update_entity(user: str, entity: str, entity_id: int, data: Dict[str, Any], id_column: str = "ID"):
    if not authenticate_user(user):
        print("Authentication failed.")
        return
    if not has_access(user, "update", entity):
        print("Access denied.")
        return
    connection, cursor = connect_database()
    try:
        updates = ", ".join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {entity} SET {updates} WHERE {id_column} = ?"
        cursor.execute(query, tuple(data.values()) + (entity_id,))
        connection.commit()
        print(f"{entity.capitalize()} with ID {entity_id} updated successfully.")
    except Exception as e:
        print(f"Error updating {entity} with ID {entity_id}: {e}")
        raise
    finally:
        connection.close()

# Generic function to delete an entity
def delete_entity(user: str, entity: str, entity_id: int, id_column: str = "ID"):
    if not authenticate_user(user):
        print("Authentication failed.")
        return
    if not has_access(user, "delete", entity):
        print("Access denied.")
        return
    connection, cursor = connect_database()
    try:
        query = f"DELETE FROM {entity} WHERE {id_column} = ?"
        cursor.execute(query, (entity_id,))
        connection.commit()
        print(f"{entity.capitalize()} with ID {entity_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting {entity} with ID {entity_id}: {e}")
        raise
    finally:
        connection.close()