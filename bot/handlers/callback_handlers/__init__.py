from .system_callbacks import system_router
from .menu import menu_router
from .info_callback import info_router

callbacks_routers = [
    system_router,
    info_router,
    menu_router,
]