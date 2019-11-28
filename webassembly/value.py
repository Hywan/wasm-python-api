from abc import ABC, abstractmethod


class Value(ABC):
    pass


class Value(ABC):
    @staticmethod
    @abstractmethod
    def i32(value: int) -> Value:
        """Build a WebAssembly i32 value."""
        pass

    @staticmethod
    @abstractmethod
    def i64(value: int) -> Value:
        """Build a WebAssembly i64 value."""
        pass

    @staticmethod
    @abstractmethod
    def f32(value: float) -> Value:
        """Build a WebAssembly f32 value."""
        pass

    @staticmethod
    @abstractmethod
    def f64(value: float) -> Value:
        """Build a WebAssembly f64 value."""
        pass
