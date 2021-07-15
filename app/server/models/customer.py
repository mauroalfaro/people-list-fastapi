from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class CustomerSchema(BaseModel):
    name: str = Field(...)
    surname: str = Field(...)
    loyalty_id: str = Field(...)
    address: str = Field(...)
    phone: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Walter",
                "surname": "White",
                "loyalty_id": "123456",
                "address": "308 Negra Arroyo Lane",
                "phone": "541234125",
                "email": "wwhite@heisenberg.io"
            }
        }


class UpdateCustomerModel(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    loyalty_id: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]

    class Config:
        schema_extra = {
            "example": {
                "name": "Walter",
                "surname": "White",
                "loyalty_id": "123456",
                "address": "308 Negra Arroyo Lane",
                "phone": "541234125",
                "email": "wwhite@heisenberg.io"
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