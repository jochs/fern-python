from generator_exec.client import GeneratorExecClient
from generator_exec.resources.config import GeneratorConfig
from generator_exec.resources.logging import TaskId
from generator_exec.resources.logging import GeneratorUpdate
import typing


class GeneratorExecWrapper:
    def __init__(self, generator_config: GeneratorConfig):
        if generator_config.environment.get().type == "local":
            self.generator_exec_client = None
            self.task_id = None
        else:
            self.generator_exec_client = GeneratorExecClient(generator_config.environment.get().coordinator_url_v_2)
            self.task_id = TaskId(__root__=generator_config.environment.get().id)

    def send_update(self, generator_update: GeneratorUpdate) -> None:
        self.send_updates(generator_updates=[generator_update])

    def send_updates(self, generator_updates: typing.List[GeneratorUpdate]) -> None:
        if self.generator_exec_client is not None and self.task_id is not None:
            self.generator_exec_client.logging.send_update(self.task_id, generator_updates)
