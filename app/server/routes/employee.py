from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_employee,
    delete_employee,
    retrieve_employee,
    retrieve_employees,
    update_employee,
)
from app.server.models.employee import (
    ErrorResponseModel,
    ResponseModel,
    EmployeeSchema,
    UpdateEmployeeModel,
)

router = APIRouter()