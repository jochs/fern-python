# This file was auto-generated by Fern from our API Definition.

import glob
import importlib
import os
import types

import fastapi
import starlette

from .core.abstract_fern_service import AbstractFernService
from .core.exceptions import default_exception_handler, fern_http_exception_handler, http_exception_handler
from .core.exceptions.fern_http_exception import FernHTTPException
from .resources.admin.service.service import AbstractAdminService
from .resources.homepage.service.service import AbstractHomepageProblemService
from .resources.migration.service.service import AbstractMigrationInfoService
from .resources.playlist.service.service import AbstractPlaylistCrudService
from .resources.problem.service.service import AbstractProblemCrudService
from .resources.submission.service.service import AbstractExecutionSesssionManagementService
from .resources.sysprop.service.service import AbstractSysPropCrudService
from .resources.v_2.problem.service.service import (
    AbstractProblemInfoServicV2 as resources_v_2_problem_service_service_AbstractProblemInfoServicV2,
)
from .resources.v_2.v_3.problem.service.service import (
    AbstractProblemInfoServicV2 as resources_v_2_v_3_problem_service_service_AbstractProblemInfoServicV2,
)


def register(
    app: fastapi.FastAPI,
    *,
    admin: AbstractAdminService,
    homepage: AbstractHomepageProblemService,
    migration: AbstractMigrationInfoService,
    playlist: AbstractPlaylistCrudService,
    problem: AbstractProblemCrudService,
    submission: AbstractExecutionSesssionManagementService,
    sysprop: AbstractSysPropCrudService,
    v_2_problem: resources_v_2_problem_service_service_AbstractProblemInfoServicV2,
    v_2_v_3_problem: resources_v_2_v_3_problem_service_service_AbstractProblemInfoServicV2
) -> None:
    app.include_router(__register_service(admin))
    app.include_router(__register_service(homepage))
    app.include_router(__register_service(migration))
    app.include_router(__register_service(playlist))
    app.include_router(__register_service(problem))
    app.include_router(__register_service(submission))
    app.include_router(__register_service(sysprop))
    app.include_router(__register_service(v_2_problem))
    app.include_router(__register_service(v_2_v_3_problem))

    app.add_exception_handler(FernHTTPException, fern_http_exception_handler)
    app.add_exception_handler(starlette.exceptions.HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, default_exception_handler)


def __register_service(service: AbstractFernService) -> fastapi.APIRouter:
    router = fastapi.APIRouter()
    type(service)._init_fern(router)
    return router


def register_validators(module: types.ModuleType) -> None:
    validators_directory: str = os.path.dirname(module.__file__)  # type: ignore
    for path in glob.glob(os.path.join(validators_directory, "**/*.py"), recursive=True):
        if os.path.isfile(path):
            relative_path = os.path.relpath(path, start=validators_directory)
            module_path = ".".join([module.__name__] + relative_path[:-3].split("/"))
            importlib.import_module(module_path)
