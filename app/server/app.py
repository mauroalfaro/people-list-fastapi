from fastapi import FastAPI

from app.server.routes.customer import router as CustomerRouter
from app.server.routes.employee import router as EmployeeRouter
from app.server.routes.store import router as StoreRouter


app = FastAPI()

app.include_router(CustomerRouter, tags=["Customer"], prefix="/customer")
app.include_router(EmployeeRouter, tags=["Employee"], prefix="/employee")
app.include_router(StoreRouter, tags=["Store"], prefix="/store")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Root endpoint for people-list application in Python"}