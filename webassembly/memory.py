from abc import ABC, abstractmethod


class MemoryView(ABC):
    @staticmethod
    @abstractmethod
    def bytes_per_element() -> int:
        """Number of bytes per element in the memory view."""
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Returns the number of elements in the memory view."""
        pass

    @abstractmethod
    def __getitem__(self, index_or_slice):
        """Reads a portion of the memory view, either by using an index or a slice."""
        pass

    @abstractmethod
    def __setitem__(self, index_or_slice, data):
        """Writes a portion of the memory view, either by using an index or a slice."""
        pass


class Int8_View(MemoryView, ABC):
    @staticmethod
    def bytes_per_element() -> int:
        return 1


class Int16_View(MemoryView, ABC):
    @staticmethod
    def bytes_per_element() -> int:
        return 2


class Int32_View(MemoryView, ABC):
    @staticmethod
    def bytes_per_element() -> int:
        return 4


class Uint8_View(MemoryView, ABC):
    @staticmethod
    def bytes_per_element() -> int:
        return 1


class Uint16_View(MemoryView, ABC):
    @staticmethod
    def bytes_per_element() -> int:
        return 2


class Uint32_View(MemoryView, ABC):
    @staticmethod
    def bytes_per_element() -> int:
        return 4


class Memory(ABC):
    @abstractmethod
    def grow(self, number_of_pages) -> int:
        """Extends the size of the array buffer by a number of pages."""
        pass

    @abstractmethod
    def int8_view(self, offset: int = 0, length: int = None) -> Int8_View:
        """Returns a view where each element is of kind `int8`."""
        pass

    @abstractmethod
    def int16_view(self, offset: int = 0, length: int = None) -> Int16_View:
        """Returns a view where each element is of kind `int16`."""
        pass

    @abstractmethod
    def int32_view(self, offset: int = 0, length: int = None) -> Int32_View:
        """Returns a view where each element is of kind `int32`."""
        pass

    @abstractmethod
    def uint8_view(self, offset: int = 0, length: int = None) -> Uint8_View:
        """Returns a view where each element is of kind `uint8`."""
        pass

    @abstractmethod
    def uint16_view(self, offset: int = 0, length: int = None) -> Uint16_View:
        """Returns a view where each element is of kind `uint16`."""
        pass

    @abstractmethod
    def uint32_view(self, offset: int = 0, length: int = None) -> Uint32_View:
        """Returns a view where each element is of kind `uint32`."""
        pass
