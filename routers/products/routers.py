from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from config.config import site_url_and_port
from config.token import validate_token

router = APIRouter(prefix="/products")
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
        "products/products.html",
        {
            "current_page": "products",
            "title": "Товары",
            "request": request,
            "token": session_key,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/create", response_class=HTMLResponse)
async def create_product_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "products/create_product.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Добавить новый товар",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/china", response_class=HTMLResponse)
async def create_product_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "products/china.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Добавить товары Китай",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/bishkek", response_class=HTMLResponse)
async def create_product_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "products/bishkek.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Добавить товары Бишкек",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/transit", response_class=HTMLResponse)
async def create_product_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "products/transit.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Добавить товары В пути",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/delete/{product_id}/", response_class=HTMLResponse)
async def delete_product_page(request: Request, product_id: int):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")

    return templates.TemplateResponse(
        "products/delete_product.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Удалить товар",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/edit/{product_id}/", response_class=HTMLResponse)
async def edit_product_page(request: Request, product_id: int):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "products/edit_product.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Редактировать товар",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/update", response_class=HTMLResponse)
async def update_products_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "products/update_products.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Изменить товары",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

@router.get("/confirm-delete", response_class=HTMLResponse)
async def confirm_delete_products_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "products/confirm_delete.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Удалить товары",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )

# Маршрут для страницы деталей товара
@router.get("/detail/{product_id}", response_class=HTMLResponse)
async def product_detail_page(request: Request, product_id: int):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")

    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "products/product_detail.html",
        {
            "request": request,
            "current_page": "products",
            "title": "Детали товара",
            "token": session_key,
            "site_url_and_port": site_url_and_port,
        }
    )