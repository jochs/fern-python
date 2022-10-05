from generator_exec.client import GeneratorExecClient
from generator_exec.resources.config import GeneratorConfig
from generator_exec.resources.logging import TaskId
from generator_exec.resources.logging import GeneratorUpdate
import typing


class GeneratorExecWrapper:
    def __init__(self, generator_config: GeneratorConfig):
        env = generator_config.environment.get()
        if env.type == "local":
            self.generator_exec_client = None
            self.task_id = None
        elif env.type == "remote":
            self.generator_exec_client = GeneratorExecClient(env.coordinator_url_v_2)
            self.task_id = env.id

    def send_update(self, generator_update: GeneratorUpdate) -> None:
        self.send_updates(generator_updates=[generator_update])

    def send_updates(self, generator_updates: typing.List[GeneratorUpdate]) -> None:
        if self.generator_exec_client is not None and self.task_id is not None:
            self.generator_exec_client.logging.send_update(self.task_id, generator_updates)
