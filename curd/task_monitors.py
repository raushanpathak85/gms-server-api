import datetime, uuid
from schema.task_monitors import TaskMonitorBase,TaskMonitorCreate,TaskMonitorUpdate
from pg_db import database,task_monitors
from sqlalchemy import select, insert, update, delete


## Curd Operation for task_monitor Table

class TaskMonitorsCurd:

    ## All projects
    @staticmethod
    async def find_all_task():
        query = task_monitors.select()
        return await database.fetch_all(query)
    
    ## Tasks register
    @staticmethod
    async def register_task(task: TaskMonitorCreate):
        query = (
            insert(task_monitors)
            .values(
                employees_id        =task.employees_id,
                project_id          =task.project_id,
                date                =task.date,
                task_completed      =task.task_completed,
                task_inprogress     =task.task_inprogress,
                task_reworked       =task.task_reworked,
                task_approved       =task.task_approved,
                task_rejected       =task.task_rejected,
                task_reviewed       =task.task_reviewed,
                hours_logged        =task.hours_logged,
            )
            .returning(task_monitors)   # ✅ return inserted row
        )
        row = await database.fetch_one(query)
        return dict(row) if row else None

    
    ## Update task_monitors
    @staticmethod
    async def update_task(task_id: int, task: TaskMonitorUpdate):
        update_data = {k: v for k, v in task.dict().items() if v is not None}
        if not update_data:
            return {"message": "No fields to update"}

        query = (
            task_monitors.update()
            .where(task_monitors.c.task_id == task_id)
            .values(**update_data)
            .returning(task_monitors)   # ✅ return updated row directly
        )
        row = await database.fetch_one(query)  # ✅ execute and fetch row
        return dict(row) if row else {"message": "Task ID not found"}

    

