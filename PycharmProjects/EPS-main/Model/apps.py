from django.apps import AppConfig


class ModelConfig(AppConfig):
    name = 'Model'

    def ready(self):
        import Model.signals
