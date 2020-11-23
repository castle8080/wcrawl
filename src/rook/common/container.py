"""
A basic dependency injection container.

A dependency injection container is just an object with parameterless methods
which return dependencies.

The singleton annotation can be used on a method so that only 1 instance is returned.

The ContainerBuilder creates a class and instance from multiple dependency providers
and factories.

"""
from abc import ABC
import importlib
import json

def singleton(method):
    """Add this annotation to methods where the instance should be cached."""
    cache = []
    def execute(self):
        if len(cache) == 0:
            cache.append(method(self))
        return cache[0]
    return execute

class Provider(ABC):
    """A base class that provider classes should inherit from in order to be discovered by scanning modules."""
    pass

class ContainerBuilder:
    """A builder for creating a dependency injection container."""
    
    def __init__(self, name):
        self.provider_types = []
        self.name = name
        self._provider_type = None
        self._factories = {}

    def load_configuration(self, json_file):
        with open(json_file, 'r') as fh:
            config = json.load(fh)
        for k, v in config.items():
            self.add_object(k, v)

    def add_object(self, name, _obj):
        self.add_factory(name, lambda _: _obj)

    def add_factory(self, name, factory):
        self._factories[name] = factory
        self._provider_type = None

    def add_provider(self, provider_type):
        if provider_type in self.provider_types:
            self.provider_types.remove(provider_type)
        self.provider_types.append(provider_type)
        self._provider_type = None

    def load_providers(self, m):
        if isinstance(m, str):
            m = importlib.import_module(m)

        def is_loadable_provider(provider_type):
            return (
                isinstance(provider_type, type) and
                issubclass(provider_type, Provider) and
                provider_type.__module__ == m.__name__
            )

        for attr_name in dir(m):
            provider_type = getattr(m, attr_name)
            if is_loadable_provider(provider_type):
                self.add_provider(provider_type)

    def provider_type(self):
        if self._provider_type is None:
            self._provider_type = type(
                f"Provider${self.name}",
                tuple(self.provider_types),
                self._factories
            )
        return self._provider_type

    def __call__(self):
        provider_type = self.provider_type()
        return provider_type()