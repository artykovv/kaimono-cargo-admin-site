from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "index.html",
        {
            "current_page": "home",
            "title": "Главная",
            "site_url_and_port": site_url_and_port,
            "token": session_key,
            "request": request
        }
    )

@router.get("/login", response_class=HTMLResponse, include_in_schema=False)
async def get_index_html(
    request: Request
):
    
    return templates.TemplateResponse(
        "auth/login.html", 
        {
            "request": request,
            "title": "Войти",
            "site_url_and_port": site_url_and_port 
        }
    )
