from fastapi import FastAPI
from routes.TodoRoute import router as TodoRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI(title="CRUD APP")

app.include_router(TodoRouter)

templates = Jinja2Templates(directory="templates")


@app.get("/", tags=["Main"])
def indexView(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})