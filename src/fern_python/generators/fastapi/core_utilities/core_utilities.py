from typing import Tuple

from fern_python.codegen import AST, Filepath

from ..fastapi_filepath_creator import FastApiFilepathCreator


class CoreUtilities:
    def __init__(self, filepath_creator: FastApiFilepathCreator):
        self._filepath = filepath_creator.generate_filepath_prefix() + (
            Filepath.DirectoryFilepathPart(module_name="core"),
        )
        self._module_path = tuple(part.module_name for part in self._filepath)

    def BearerToken(self) -> AST.ClassReference:
        return AST.ClassReference(
            qualified_name_excluding_import=(),
            import_=AST.ReferenceImport(
                module=AST.Module.local(*self._get_bearer_module_path()), named_import="BearerToken"
            ),
        )

    def HTTPBearer(self) -> AST.ClassReference:
        return AST.ClassReference(
            qualified_name_excluding_import=(),
            import_=AST.ReferenceImport(
                module=AST.Module.local(*self._get_bearer_module_path()), named_import="HTTPBearer"
            ),
        )

    def _get_security_filepath(self) -> Tuple[Filepath.DirectoryFilepathPart, ...]:
        return self._filepath + (Filepath.DirectoryFilepathPart(module_name="security"),)

    def _get_security_module_path(self) -> AST.ModulePath:
        return tuple(part.module_name for part in self._get_security_filepath())

    def _get_bearer_module_path(self, *submodule: str) -> AST.ModulePath:
        return self._get_security_submodule_path("bearer")

    def _get_security_submodule_path(self, *submodule: str) -> AST.ModulePath:
        return self._get_security_module_path() + submodule
