"""
Module that execute queries on the database.
"""

from model.tasks import Task
from .init import conn, curs


if curs is not None and conn is not None:
    curs.execute(
        """create table if not exists tasks(
    id integer primary key autoincrement,
    name text,
    description text,
    status text)"""
    )
    conn.commit()


def row_to_model(row: tuple):
    """
    Function that converts a row or a tuple into a model.
    """
    task_id, name, description, status = row
    return Task(task_id=task_id, name=name, description=description, status=status)


def model_to_dict(task: Task) -> dict:
    """
    Function that converts a model into a dict.
    """
    return task.model_dump()


def create_task(task) -> Task | None:
    """
    Function that creates a task record in the database.
    """
    qry = """insert into tasks (name, description, status)  values
        (:name, :description, :status)"""
    params = model_to_dict(task)
    if curs is not None and conn is not None:
        response = curs.execute(qry, params)
        conn.commit()
        return get_one_task(response.lastrowid)
    return None


def get_one_task(task_id) -> Task | None:
    """
    Function that returns a task record.
    """
    qry = "select * from tasks where id=:task_id"
    params = {"task_id": task_id}
    if curs is not None and conn is not None:
        curs.execute(qry, params)
        conn.commit()

        return row_to_model(curs.fetchone())

    return None


def get_all_task() -> list | None:
    """
    Function that returns a task record.
    """
    qry = "select * from tasks"
    if curs is not None and conn is not None:
        curs.execute(qry)
        conn.commit()

        return [row_to_model(row) for row in curs.fetchall()]

    return None
