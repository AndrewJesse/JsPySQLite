import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    try:
        return crud.create_task(db=db, task=task)
    except Exception as e:
        app.logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    try:
        tasks = crud.get_tasks(db, skip=skip, limit=limit)
        return tasks
    except Exception as e:
        app.logger.error(f"Error reading tasks: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")