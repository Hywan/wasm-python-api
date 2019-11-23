from pathlib import Path

from wasmer import Instance
from webassembly.module import Module


def WebAssembly(path: Path):
    """ Bootstrap the Python-Wasm "framework".

    This entrypoint function is named CamelCase to underline its
     bootstrapping capability. Expected usage:
     >>> path = Path('path_to_wasm_binary')
     >>> wasm_with_python = WebAssembly(path)
    """
    loaded = None
    with open(str(path), 'rb') as bytecode:
        loaded = bytecode.read()

    return MyModule(loaded)


class MyModule(Module):
    def __init__(self, bytes_: bytes):
        """Compiles WebAssembly bytes into a module."""
        self._bytes = bytes_

    def instantiate(self):
        instance = Instance(self._bytes)
        return instance

    def serialize(self) -> bytes:
        return self._bytes

    @staticmethod
    def deserialize(serialized_module) -> Module:
        if not isinstance(serialized_module, bytes):
            raise ValueError('value is not bytes')
        return MyModule(serialized_module)
