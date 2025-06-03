import asyncio
import aiohttp
from config.config import site_url_and_port


async def validate_token(token: str):
    url = f"{site_url_and_port}/auth/validate-token"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return response.status  # Возвращает статус-код
