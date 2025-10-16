from fastapi import APIRouter
from typing import List
from schema.tasks_monitor import TaskMonitorBase, TaskMonitorCreate, TaskMonitorUpdate
from curd.tasks_monitor import TaskMonitorsCurd

router = APIRouter(prefix="/tasks", tags=["Task Monitors"])

# Get all Tasks
@router.get("", response_model=List[TaskMonitorBase])
async def find_all_task():
    return await TaskMonitorsCurd.find_all_task()

# Register tasks
@router.post("", response_model=TaskMonitorBase)
async def register_task(task: TaskMonitorCreate):
    return await TaskMonitorsCurd.register_task(task)

# Get project by ID
@router.get("/projects/{project_Id}", response_model=TaskMonitorBase)
async def find_project_by_id(project_Id: int):
    return await TaskMonitorsCurd.find_project_by_id(project_Id)

# Update Task
@router.put("/{task_Id}", response_model=TaskMonitorBase)
async def update_task(task_id: int, task: TaskMonitorUpdate):
    return await TaskMonitorsCurd.update_task(task_id, task)

# Delete Task
@router.delete("/{task_Id}")
async def delete_task(task_id: int):
    return await TaskMonitorsCurd.delete_task(task_id)
