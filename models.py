from pydantic import BaseModel
from uuid import UUID, uuid4

class Model(BaseModel):
    id: UUID = uuid4()
    name: str
