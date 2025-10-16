from fastapi import APIRouter
from schema.roles import RolesList, RolesUpdate, RolesEntry
from curd.roles import RolesCurdOperation
from typing import List

router = APIRouter(prefix="/roles", tags=["Roles"])

# Get all roles
@router.get("", response_model=List[RolesList])
async def find_all_roles():
    return await RolesCurdOperation.find_all_roles()

# Register role
@router.post("", response_model=RolesList)
async def register_role(role: RolesEntry):
    return await RolesCurdOperation.register_role(role)

# Update role
@router.put("/{roleId}", response_model=RolesList)
async def update_role(roleId: str, role: RolesUpdate):
    return await RolesCurdOperation.update_role(roleId, role)

# Delete role
@router.delete("/{roleId}")
async def delete_role(roleId: str):
    return await RolesCurdOperation.delete_role(roleId)