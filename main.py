from typing import List
from bson import ObjectId
from fastapi import FastAPI, HTTPException

from configurations import test_collection
from models import Model, ModelCollection

app = FastAPI()

@app.get(
    "/api/v1/catalog",
    response_description="List of all models",
    response_model=ModelCollection,
    response_model_by_alias=False,
)
async def list_models():
    """
    List all usdz model metadata files
    """
    return ModelCollection(models=await test_collection.find().to_list(1000))

@app.get(
    "/api/v1/catalog/{file_id}",
    response_description="Get a single file",
    response_model=Model,
    response_model_by_alias=False,
)
async def show_file(id: str):
    """
    Get the saved metadata file for a specific UUID.
    """
    if (
        file := await test_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return file

    raise HTTPException(status_code=404, detail=f"File {id} not found")

# @app.post("/api/v1/catalog", response_model=Model)
# def add_file(user: Model):
#     db.append(user)
#     return {"user_id": user.id}

