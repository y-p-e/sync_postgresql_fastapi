from sqlalchemy.orm import Session
import api.models.task as task_model
import api.schemas.task as task_schema


def get_tasks(db: Session):
    tasks = db.query(task_model.Task).all()
    return tasks

def get_task(db: Session, task_id):
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    return task

def create_task(db: Session, task_create: task_schema.TaskCreate):
    task = task_model.Task(title=task_create.title)
    db.add(task)
    db.commit()
    return task

def update_task(db: Session, task_id, task_create: task_schema.TaskCreate):
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    task.title = task_create.title
    db.add(task)
    db.commit()
    return task

def delete_task(db: Session, task_id):
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).delete()
    db.commit()
    return task