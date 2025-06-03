from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/users")
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def users_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "user/users.html",
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": "users", 
            "title": "Пользователи",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/create", response_class=HTMLResponse)
async def create_user_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "user/create_user.html", 
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": "users",
            "title": "Создание пользователя",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )