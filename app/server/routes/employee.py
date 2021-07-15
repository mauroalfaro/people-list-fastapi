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


@router.post("/", response_description="Employee data added into the database")
async def add_employee_data(employee: EmployeeSchema = Body(...)):
    employee = jsonable_encoder(employee)
    new_employee = await add_employee(employee)
    return ResponseModel(new_employee, "Employee added successfully.")


@router.get("/", response_description="Employees retrieved")
async def get_employees():
    employees = await retrieve_employees()
    if employees:
        return ResponseModel(employees, "Employees data retrieved successfully")
    return ResponseModel(employees, "Empty list returned")


@router.get("/{id}", response_description="Employee data retrieved")
async def get_employee_data(id):
    employee = await retrieve_employee(id)
    if employee:
        return ResponseModel(employee, "Employee data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Employee doesn't exist.")


@router.put("/{id}")
async def update_employee_data(id: str, req: UpdateEmployeeModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_employee = await update_employee(id, req)
    if updated_employee:
        return ResponseModel(
            "Employee with ID: {} name update is successful".format(id),
            "Employee name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the employee data.",
    )


@router.delete("/{id}", response_description="Employee data deleted from the database")
async def delete_employee_data(id: str):
    deleted_employee = await delete_employee(id)
    if deleted_employee:
        return ResponseModel(
            "Employee with ID: {} removed".format(id), "Employee deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Employee with id {0} doesn't exist".format(id)
    )
