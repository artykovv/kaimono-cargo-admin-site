from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/take")
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def take_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "take/take.html",
        {
            "request": request,
            "current_page": "take",
            "title": "Выдать",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/{code}", response_class=HTMLResponse)
async def take_page(
    request: Request,
    code: str
    ):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "take/take_user.html",
        {
            "request": request,
            "current_page": "take",
            "title": "Выдать",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
            "code": code
        }
    )