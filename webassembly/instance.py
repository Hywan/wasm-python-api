from abc import ABC, abstractmethod
from webassembly.exports import Exports
from webassembly.memory import Memory


class Instance(ABC):
    pass


class Instance(ABC):
    # IMO, an Instance should be created only from a module
    # @abstractmethod
    # def __init__(self, bytes: bytes):
    #     """Compiles and instantiates WebAssembly bytes."""
    #     pass

    @classmethod
    @abstractmethod
    def from_module(cls, module) -> Instance:
        """Instantiates from a WebAssembly module."""
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
