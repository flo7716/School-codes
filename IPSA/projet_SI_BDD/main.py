from typing import Dict, Any
from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
import Projet_base_de_donnees as projet

app = FastAPI()
connection, cursor = projet.connect_database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

# Generic CRUD operations
@app.post("/add/{entity}")
def add_entity(entity: str, data: Dict[str, Any] = Form(...)):
    try:
        # Add the entity to the database
        projet.add_entity(entity, data)
        return {"message": f"{entity.capitalize()} added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all/{entity}")
def get_all_entities(entity: str):
    try:
        # Retrieve all entities from the database
        entities = projet.get_all_entities(entity)
        return {f"{entity}s": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get/{entity}/{entity_id}")
def get_entity_by_id(entity: str, entity_id: int):
    try:
        # Retrieve a specific entity by ID
        result = projet.get_entity_by_id(entity, entity_id)
        if not result:
            raise HTTPException(status_code=404, detail=f"{entity.capitalize()} not found")
        return {entity: result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update/{entity}/{entity_id}")
def update_entity(entity: str, entity_id: int, data: Dict[str, Any] = Form(...)):
    try:
        # Update the entity in the database
        projet.update_entity(entity, entity_id, data)
        return {"message": f"{entity.capitalize()} updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete/{entity}/{entity_id}")
def delete_entity(entity: str, entity_id: int):
    try:
        # Delete the entity from the database
        projet.delete_entity(entity, entity_id)
        return {"message": f"{entity.capitalize()} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


## main

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


