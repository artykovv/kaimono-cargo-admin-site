from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/setting")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "config/config.html",
        {
            "current_page": "config",
            'current_mini_page': 'config',
            "title": "Настройки",
            "request": request,
            "token": session_key,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/edit/{id}", response_class=HTMLResponse)
async def page(id: int, request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
        
    return templates.TemplateResponse(
        "config/edit_config.html",
        {
            "current_page": "config",
            'current_mini_page': 'config',
            "title": "Изменить",
            "request": request,
            "token": session_key,
            "site_url_and_port": site_url_and_port,
            "setting_id": id
        }
    )