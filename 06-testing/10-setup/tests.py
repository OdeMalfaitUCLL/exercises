import pytest
from datetime import date
from tasks import Task, TaskList
from calendars import *
#sut = system under test
def setup_function():
    global today
    global tomorrow
    global yesterday
    global calendar
    global sut
    today = date(2024,1,2)
    tomorrow = date(2024,1,3)
    yesterday = date(2024,1,1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)

def test_task_becomes_overdue():
    #Arrange
    next_month = date(2024,2,2)
    task = Task('some description',tomorrow)
    sut.add_task(task)
    #Act
    calendar.today = next_month
    #Assert
    assert [task] == sut.overdue_tasks

def test_creation():
    #Assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_date_in_future():
    #Arrange
    task = Task("some description",tomorrow)
    sut.add_task(task)
    #Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_date_in_past():
    #Arrange
    task = Task("some description",yesterday)
    #Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)
    assert [] == sut.due_tasks

def test_task_becomes_finished():
    #Arrange
    task = Task("some description",tomorrow)
    sut.add_task(task)
    #Act
    task.finished = True
    #Assert
    assert 1 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [task] == sut.finished_tasks
