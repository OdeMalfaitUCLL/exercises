import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import *
#sut = system under test

@pytest.fixture
def sut(calendar):
    return TaskList(calendar)
@pytest.fixture
def calendar(today):
    return CalendarStub(today)
@pytest.fixture
def today():
    return date(2024,1,2)
@pytest.fixture 
def tomorrow(today):
    return today + timedelta(days=1)
@pytest.fixture 
def yesterday(today):
    return today - timedelta(days=1)

def test_task_becomes_overdue(sut,today,calendar,tomorrow):
    #Arrange
    next_week = today + timedelta(weeks=1)
    task = Task('some description',tomorrow)
    sut.add_task(task)
    #Act
    calendar.today = next_week
    #Assert
    assert [task] == sut.overdue_tasks

def test_creation(sut):
    #Assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_date_in_future(sut,tomorrow):
    #Arrange
    task = Task("some description",tomorrow)
    sut.add_task(task)
    #Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_date_in_past(sut,yesterday):
    #Arrange
    task = Task("some description",yesterday)
    #Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)
    assert [] == sut.due_tasks

def test_task_becomes_finished(sut,tomorrow):
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
