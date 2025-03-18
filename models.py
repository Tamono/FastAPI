from typing import Annotated, Optional, List
from pydantic import BaseModel, BeforeValidator, Field, ConfigDict

PyObjectId = Annotated[str, BeforeValidator(str)]

class Model(BaseModel):
    """
    Container for the metadata of a single 3DModel usdz model file.
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class ModelCollection(BaseModel):
    """
    Container for a list of Models.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """
    models: List[Model]