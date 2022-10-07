import os
from abc import ABC, abstractmethod

from generator_exec.resources import logging
from generator_exec.resources.config import GeneratorConfig, GeneratorPublishConfig

from fern_python.codegen.project import Project, PyProjectTomlConfig
from fern_python.generated.ir_types import IntermediateRepresentation
from fern_python.generator_exec_wrapper import GeneratorExecWrapper


class AbstractGenerator(ABC):
    def generate_project(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: IntermediateRepresentation,
        generator_config: GeneratorConfig,
    ) -> None:
        pyproject_toml_config = generator_config.output.mode.visit(
            download_files=lambda: None,
            publish=lambda publish: PyProjectTomlConfig(
                package_name=publish.registries_v_2.pypi.package_name, package_version=publish.version
            ),
        )
        with Project(
            filepath=generator_config.output.path,
            project_name=ir.api_name,
            pyproject_toml_config=pyproject_toml_config,
        ) as project:
            self.run(
                generator_exec_wrapper=generator_exec_wrapper,
                ir=ir,
                generator_config=generator_config,
                project=project,
            )
        generator_config.output.mode.visit(
            download_files=lambda: None,
            publish=lambda publish: self._publish_project(
                generator_exec_wrapper=generator_exec_wrapper, publish_config=publish
            ),
        )

    def _publish_project(self, generator_exec_wrapper: GeneratorExecWrapper, publish_config: GeneratorPublishConfig) -> None:
        pypi_registry_config = publish_config.registries_v_2.pypi
        poetry_repo_name = "fern"
        self._run_command(generator_exec_wrapper=generator_exec_wrapper, command=f"poetry install")
        self._run_command(
            generator_exec_wrapper=generator_exec_wrapper,
            command=f"poetry config repositories.{poetry_repo_name} {pypi_registry_config.registry_url}/simple",
        )
        self._run_command(
            generator_exec_wrapper=generator_exec_wrapper,
            command=f"poetry config http-basic.{poetry_repo_name} {pypi_registry_config.username} {pypi_registry_config.password}",
        )
        self._run_command(
            generator_exec_wrapper=generator_exec_wrapper,
            command=f"poetry publish --build --repository {poetry_repo_name}",
        )

    def _run_command(
        self,
        *,
        command: str,
        generator_exec_wrapper: GeneratorExecWrapper,
    ) -> None:
        generator_exec_wrapper.send_update(
            logging.GeneratorUpdate.factory.log(logging.LogUpdate(level=logging.LogLevel.DEBUG, message=command))
        )
        exit_code = os.system(command)
        if exit_code < 0:
            raise Exception(f"{command} failed with exit code {exit_code}")

    @abstractmethod
    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:
        pass
