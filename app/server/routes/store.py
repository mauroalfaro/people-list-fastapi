from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_store,
    delete_store,
    retrieve_store,
    retrieve_stores,
    update_store,
)
from app.server.models.store import (
    ErrorResponseModel,
    ResponseModel,
    StoreSchema,
    UpdateStoreModel,
)

router = APIRouter()