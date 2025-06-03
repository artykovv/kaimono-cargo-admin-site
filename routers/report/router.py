from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/report")
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def report_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    
    return templates.TemplateResponse(
        "report/report.html",
        {
            "request": request,
            "current_page": "report",
            "title": "Отчет",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )