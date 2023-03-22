import os
from typing import Optional, Set

from fern_python.codegen import AST, Filepath, Project
from fern_python.source_file_generator import SourceFileGenerator

from ..sdk_filepath_creator import SdkFilepathCreator


class CoreUtilities:
    def __init__(self, filepath_creator: SdkFilepathCreator):
        self.filepath = filepath_creator.generate_filepath_prefix() + (
            Filepath.DirectoryFilepathPart(module_name="core"),
        )
        self._module_path = tuple(part.module_name for part in self.filepath)

    def copy_to_project(self, *, project: Project) -> None:
        self._copy_file_to_project(
            project=project,
            relative_filepath_on_disk="datetime_utils.py",
            filepath_in_project=Filepath(
                directories=self.filepath,
                file=Filepath.FilepathPart(module_name="datetime_utils"),
            ),
            exports={"serialize_datetime"},
        )
        self._copy_file_to_project(
            project=project,
            relative_filepath_on_disk="api_error.py",
            filepath_in_project=Filepath(
                directories=self.filepath,
                file=Filepath.FilepathPart(module_name="api_error"),
            ),
            exports={"ApiError"},
        )

    def _copy_file_to_project(
        self, *, project: Project, relative_filepath_on_disk: str, filepath_in_project: Filepath, exports: Set[str]
    ) -> None:
        source = (
            os.path.join(os.path.dirname(__file__), "../../../../../core_utilities/sdk")
            if "PYTEST_CURRENT_TEST" in os.environ
            else "/assets/core_utilities"
        )
        SourceFileGenerator.add_source_file_from_disk(
            project=project,
            path_on_disk=os.path.join(source, relative_filepath_on_disk),
            filepath_in_project=filepath_in_project,
            exports=exports,
        )

    def get_serialize_datetime(self) -> AST.Reference:
        return AST.Reference(
            qualified_name_excluding_import=(),
            import_=AST.ReferenceImport(
                module=AST.Module.local(*self._module_path, "datetime_utils"), named_import="serialize_datetime"
            ),
        )

    def get_api_error(self) -> AST.ClassReference:
        return AST.ClassReference(
            qualified_name_excluding_import=(),
            import_=AST.ReferenceImport(
                module=AST.Module.local(*self._module_path, "api_error"), named_import="ApiError"
            ),
        )

    def instantiate_api_error_from_subclass(
        self, *, status_code: Optional[AST.Expression], body: Optional[AST.Expression]
    ) -> AST.AstNode:
        def _write(writer: AST.NodeWriter) -> None:
            writer.write("super().__init__(")
            if status_code is not None:
                writer.write("status_code=")
                writer.write_node(status_code)
            if body is not None:
                writer.write(", body=")
                writer.write_node(body)
            writer.write_line(")")

        return AST.CodeWriter(code_writer=_write)
