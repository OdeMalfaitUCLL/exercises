import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import *
#sut = system under test

def today():
    return date(2024,1,2)

def tomorrow():
    return today() + timedelta(days=1)

def yesterday():
    return today() - timedelta(days=1)

def create_calendar():
    return CalendarStub(today())

def create_empty_tasklist(calendar=None):
    calendar = calendar or create_calendar()
    return TaskList(calendar)

def create_task(*,description="description",due_date=None,finished=False):
    due_date = due_date or date(2024,4,2)
    task = Task(description,due_date)
    if finished:
        task.finished = True
    return task

def test_task_becomes_overdue():
     # Arrange
    next_week = today() + timedelta(weeks=1)
    task = create_task(due_date=tomorrow())
    calendar = create_calendar()
    sut = create_empty_tasklist(calendar=calendar)

    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks

def test_creation():
    sut = create_empty_tasklist()
    #Assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_date_in_future():
    #Arrange
    sut = create_empty_tasklist()
    task = create_task(due_date = tomorrow())
    #Act
    sut.add_task(task)
    #Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_date_in_past():
    #Arrange
    sut = create_empty_tasklist()
    task = create_task(due_date=yesterday())
    #Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)

def test_task_becomes_finished():
    #Arrange
    sut = create_empty_tasklist()
    task = create_task(due_date=tomorrow())
    sut.add_task(task)
    #Act
    task.finished = True
    #Assert
    assert 1 == len(sut)
    assert [task] == sut.finished_tasks
