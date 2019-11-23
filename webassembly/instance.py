from abc import ABC, abstractmethod
from webassembly.exports import Exports
from webassembly.memory import Memory


class Instance(ABC):
    pass


class Instance(ABC):
    @abstractmethod
    def __init__(self, bytes: bytes):
        """Compiles and instantiates WebAssembly bytes."""
        pass

    @staticmethod
    @abstractmethod
    def from_module(module) -> Instance:
        """Instantiates a WebAssembly module."""
        pass

    @property
    @abstractmethod
    def exports(self) -> Exports:
        """Returns the exported functions"""
        pass

    @property
    @abstractmethod
    def memory(self) -> Memory:
        """Returns the instance memory if any."""
        pass
