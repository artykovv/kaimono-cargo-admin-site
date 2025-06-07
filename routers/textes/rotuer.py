from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/textes")
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
        "textes/textes.html",
        {
            "current_page": "config",
            'current_mini_page': 'textes',
            "title": "Текста",
            "request": request,
            "token": session_key,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/edit/{id}", response_class=HTMLResponse)
async def page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
        
    return templates.TemplateResponse(
        "textes/text.html",
        {
            "current_page": "config",
            'current_mini_page': 'textes',
            "title": "Изменить",
            "request": request,
            "id": id,
            "token": session_key,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/create/", response_class=HTMLResponse)
async def page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
        
    return templates.TemplateResponse(
        "textes/create.html",
        {
            "current_page": "config",
            'current_mini_page': 'textes',
            "title": "Изменить",
            "request": request,
            "token": session_key,
            "site_url_and_port": site_url_and_port
        }
    )