from abc import ABC, abstractmethod
from webassembly.instance import Instance


class Module(ABC):
    pass


class Module(ABC):
    def __init__(self, bytes_: bytes):
        """Compiles WebAssembly bytes into a module."""
        pass

    @abstractmethod
    def instantiate(self) -> Instance:
        """Instantiates the module."""
        pass

    @abstractmethod
    def serialize(self) -> bytes:
        """Serializes this module to bytes."""
        pass

    @staticmethod
    @abstractmethod
    def deserialize(serialized_module) -> Module:
        """Deserializes a (supposedly) serialized module."""
        pass
