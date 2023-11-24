from aiogram import Router

def setup_routers() -> Router:
    from . import service_commands, random_pattern

    router = Router()
    router.include_router(service_commands.router)
    router.include_router(random_pattern.router)

    return router