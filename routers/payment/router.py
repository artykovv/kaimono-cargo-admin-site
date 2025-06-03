from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/payment")
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
        "payment/payment.html",
        {
            "request": request,
            "current_page": "config",
            "current_mini_page": "payment_methods",
            "title": "Способы оплаты",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

# Маршрут для страницы создания
@router.get("/create", response_class=HTMLResponse)
async def create_payment_method_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "payment/create_payment_method.html",
        {
            "request": request,
            "current_page": "payment_methods",
            "current_mini_page": "payment_methods",
            "title": "Добавить способ оплаты",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

# Маршрут для страницы редактирования
@router.get("/edit/{method_id}", response_class=HTMLResponse)
async def edit_payment_method_page(request: Request, method_id: int):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "payment/edit_payment_method.html",
        {
            "request": request,
            "current_page": "payment_methods",
            "current_mini_page": "payment_methods",
            "title": "Редактировать способ оплаты",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )