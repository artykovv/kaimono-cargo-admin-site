from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/branch")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def branch_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")

    return templates.TemplateResponse(
        "branch/branch.html",
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": "branch", 
            "title": "Филиалы",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/create", response_class=HTMLResponse)
async def branch_create_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")

    return templates.TemplateResponse(
        "branch/branch_create.html",
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": "branch", 
            "title": "Добавить филиал",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/update/{id}", response_class=HTMLResponse)
async def branch_update(id: int, request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")

    return templates.TemplateResponse(
        "branch/branch_edit.html",
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": "branch", 
            "title": "Добавить филиал",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
            "branch_id": id
        }
    )