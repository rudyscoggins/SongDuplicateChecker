from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from . import utils

app = FastAPI(title="Song Duplicate Checker")

templates = Jinja2Templates(directory=str(utils.TEMPLATES_DIR))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    random_file = utils.get_random_music_file()
    diagnostics = utils.get_nas_diagnostics()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "random_file": random_file,
            "diagnostics": diagnostics,
        },
    )

@app.get("/health")
async def health():
    return {"status": "ok"}
