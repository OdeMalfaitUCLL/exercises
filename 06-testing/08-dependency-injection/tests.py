from datetime import date
from tasks import Task, TaskList
from calendars import *

def test_task_becomes_overdue():
    today = date(2024,1,1)
    tomorrow = date(2024,1,2)
    next_month = date(2024,2,1)
    task = Task('some description',tomorrow)
    calendar = CalendarStub(today)
    tasks = TaskList(calendar)
    tasks.add_task(task)
    calendar.today = next_month
    assert [task] == tasks.overdue_tasks
