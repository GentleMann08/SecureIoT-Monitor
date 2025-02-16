from .testing import testing_router
from .system_callbacks import system_router
from .project_info import project_info_router
from .menu import menu_router
from .join import join_router

callbacks_routers = [
    testing_router,
    system_router,
    project_info_router,
    join_router
]