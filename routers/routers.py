from fastapi import APIRouter

from .index.router import router as index
from .client.router import router as clients
from .products.routers import router as products
from .take.router import router as take
from .setting.router import router as setting
from .report.router import router as report
from .user.router import router as users
from .branch.router import router as branch
from .china.router import router as china
from .payment.router import router as payment
from .telegram.router import router as telegram

routers  = APIRouter()

routers.include_router(index)
routers.include_router(clients)
routers.include_router(products)
routers.include_router(take)
routers.include_router(setting)
routers.include_router(report)
routers.include_router(users)
routers.include_router(branch)
routers.include_router(china)
routers.include_router(payment)
routers.include_router(telegram)