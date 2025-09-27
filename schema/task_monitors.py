from pydantic import BaseModel,Field
from typing import Optional, Annotated
from datetime import date
from decimal import Decimal

# define alias for constrained decimal
HoursLogged = Annotated[Decimal, Field(max_digits=4, decimal_places=2)]

class TaskMonitorBase(BaseModel):
    task_id         :int
    employees_id    : str
    project_id      : int
    date            : date
    task_completed  : int = 0
    task_inprogress : int = 0
    task_reworked   : int = 0
    task_approved   : int = 0
    task_rejected   : int = 0
    task_reviewed   : int = 0
    hours_logged    : HoursLogged = 0.00  # matches DECIMAL(4,2)


class TaskMonitorCreate(BaseModel):
    """Schema for creating new task monitor entry"""
    employees_id    : str
    project_id      : int
    date            : date
    task_completed  : int = 0
    task_inprogress : int = 0
    task_reworked   : int = 0
    task_approved   : int = 0
    task_rejected   : int = 0
    task_reviewed   : int = 0
    hours_logged    : HoursLogged = 0.00  # matches DECIMAL(4,2)



class TaskMonitorUpdate(BaseModel):
    """Schema for updating task monitor entry (all fields optional)"""
    employees_id    : str
    project_id      : int
    date            : date
    task_completed  : Optional[int] = None
    task_inprogress : Optional[int] = None
    task_reworked   : Optional[int] = None
    task_approved   : Optional[int] = None
    task_rejected   : Optional[int] = None
    task_reviewed   : Optional[int] = None
    hours_logged    : Optional[HoursLogged] = None



