from abc import ABC, abstractmethod


class ExportedFunction(ABC):
    @abstractmethod
    def __call__(self, *arguments):
        """Invokes the exported function."""
        pass


class Exports(ABC):
    @abstractmethod
    def __getattr__(self, exported_function_name: str) -> ExportedFunction:
        """Gets an exported function."""
        pass
