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


@router.post("/", response_description="Store data added into the database")
async def add_store_data(store: StoreSchema = Body(...)):
    store = jsonable_encoder(store)
    new_store = await add_store(store)
    return ResponseModel(new_store, "Store added successfully.")


@router.get("/", response_description="Stores retrieved")
async def get_stores():
    stores = await retrieve_stores()
    if stores:
        return ResponseModel(stores, "Stores data retrieved successfully")
    return ResponseModel(stores, "Empty list returned")


@router.get("/{id}", response_description="Store data retrieved")
async def get_store_data(id):
    store = await retrieve_store(id)
    if store:
        return ResponseModel(store, "Store data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Store doesn't exist.")


@router.put("/{id}")
async def update_store_data(id: str, req: UpdateStoreModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_store = await update_store(id, req)
    if updated_store:
        return ResponseModel(
            "Store with ID: {} name update is successful".format(id),
            "Store name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the store data.",
    )


@router.delete("/{id}", response_description="Store data deleted from the database")
async def delete_store_data(id: str):
    deleted_store = await delete_store(id)
    if deleted_store:
        return ResponseModel(
            "Store with ID: {} removed".format(id), "Store deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Store with id {0} doesn't exist".format(id)
    )
