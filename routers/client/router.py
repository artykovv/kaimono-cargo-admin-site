from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/clients")
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
        "clients/clients.html",
        {
            "current_page": "clients",
            "title": "Клиенты",
            "request": request,
            "token": session_key,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/create", response_class=HTMLResponse)
async def create_client_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "clients/create_client.html",
        {
            "request": request,
            "current_page": "create_client",
            "title": "Добавить клиента",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/{client_id}", response_class=HTMLResponse)
async def delete_client_page(request: Request, client_id: int):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "clients/delete_client.html",
        {
            "request": request,
            "current_page": "delete_client",
            "title": "Удалить клиента",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/{client_id}/edit", response_class=HTMLResponse)
async def edit_client_page(request: Request, client_id: int):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "clients/edit_client.html",
        {
            "request": request,
            "current_page": "edit_client",
            "title": "Редактирование клиента",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/{client_id}/detail", response_class=HTMLResponse)
async def client_detail_page(request: Request, client_id: int):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "clients/client_detail.html",
        {
            "request": request,
            "current_page": "client_detail",
            "title": "Данные о клиенте",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )