from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException

from models import Model

app = FastAPI()

db: List[Model] = [
    Model(
        name="Gesture",
    ),
    Model(
        name="Zimmer",
    ),
    Model(
        name="Tisch",
    ),
]

@app.get("/api/v1/catalog", response_model=List[Model])
def list_files(limit: int = 10):
    return db[0:limit]

# @app.post("/api/v1/catalog", response_model=Model)
# def add_file(user: Model):
#     db.append(user)
#     return {"user_id": user.id}

@app.get("/api/v1/catalog/{file_id}", response_model=Model)
def get_file(uuid: UUID):
    for file in db:
        if file.id == uuid:
            return file
    raise HTTPException(status_code=404, detail="File not found")

@app.delete("/api/v1/catalog/{file_id}", response_model=Model)
def delete_user(file_id: UUID):
    for file in db:
        if file.id == file_id:
            db.remove(file)
            return file
    raise HTTPException(status_code=404, detail="File not found")