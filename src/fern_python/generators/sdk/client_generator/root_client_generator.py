from ..context.sdk_generator_context import SdkGeneratorContext


class RootClientGenerator:
    _ROOT_CLIENT_CLASS_NAME = "Client"

    def __init__(self, context: SdkGeneratorContext):
        self._context = context
