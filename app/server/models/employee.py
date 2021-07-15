from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class EmployeeSchema(BaseModel):
    name: str = Field(...)
    surname: str = Field(...)
    address: str = Field(...)
    phone: str = Field(...)
    email: EmailStr = Field(...)
    dateHired: str = Field(...)
    role: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Geralt",
                "surname": "De Rivia",
                "address": "Somewhere in Rivia",
                "phone": "541234125",
                "email": "geralt@witcher.dev",
                "dateHired": "04/25/1708",
                "role": "Witcher"
            }
        }


class UpdateEmployeeModel(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    loyalty_id: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    dateHired: Optional[str]
    role: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Geralt",
                "surname": "De Rivia",
                "address": "Somewhere in Rivia",
                "phone": "541234125",
                "email": "geralt@witcher.dev",
                "dateHired": "04/25/1708",
                "role": "Witcher"
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