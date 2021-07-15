from typing import Optional

from pydantic import BaseModel, Field

class StoreSchema(BaseModel):
    storeName: str = Field(...)
    address: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "storeName": "Dick's Sporting Goods",
                "address": "8001 S Orange Blossom Trl Ste 1302, Orlando, FL",
            }
        }


class UpdateStoreModel(BaseModel):
    storeName: Optional[str]
    address: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "storeName": "Dick's Sporting Goods",
                "address": "8001 S Orange Blossom Trl Ste 1302, Orlando, FL",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}