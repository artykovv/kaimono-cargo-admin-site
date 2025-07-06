from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/files")
templates = Jinja2Templates(directory="templates")

@router.get("/create/{type}", response_class=HTMLResponse)
async def take_page(request: Request, type: str):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "file/create.html",
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": type,
            "title": "Добавить",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/photo", response_class=HTMLResponse)
async def take_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "file/photo.html",
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": "photo",
            "title": "Фото",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/video", response_class=HTMLResponse)
async def take_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "file/video.html",
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": "video",
            "title": "Видeо",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )