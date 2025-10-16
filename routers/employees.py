from schema.employees import EmployeesList,EmployeesUpdate, EmployeesEntry
from curd.employees import EmployeesCurdOperation
from fastapi import APIRouter, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter(prefix="/employees", tags=["Employees"])

# Get all employees
@router.get("", response_model=List[EmployeesList])
async def find_all_employees():
    return await EmployeesCurdOperation.find_all_employees()

# Register employee
@router.post("", response_model=EmployeesList)
async def register_employee(employee: EmployeesList):
    return await EmployeesCurdOperation.register_employee(employee)

# Get employee by ID
@router.get("/{employeeId}", response_model=EmployeesList)
async def find_employee_by_id(employeeId: str):
    return await EmployeesCurdOperation.find_employees_by_id(employeeId)

# Update employee
@router.put("/{employeeId}", response_model=EmployeesList)
async def update_employee(employeeId: str, employee: EmployeesUpdate):
    return await EmployeesCurdOperation.update_employees(employeeId, employee)

# Delete employee
@router.delete("/{employeeId}", tags=["Employees"])
async def delete_employee(employeeId: str):
    return await EmployeesCurdOperation.delete_employee(employeeId)

# Get all employees names and ids
@router.get("/names", tags=["Employees"])
async def find_all_employees_name():
    return await EmployeesCurdOperation.find_all_employees_name()

