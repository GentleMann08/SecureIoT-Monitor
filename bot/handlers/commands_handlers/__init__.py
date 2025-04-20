from .start_handler import start_router
from .example import example_router
from .admin import admin_router

command_routers = [
    start_router,
    example_router,
    admin_router
]