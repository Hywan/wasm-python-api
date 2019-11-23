from pathlib import Path

from webassembly.module import Module
from webassembly.instance import Instance


def WebAssembly(path: Path, instance_cls: Instance):
    """ Bootstrap the Python-Wasm "framework".

    This entrypoint function is named CamelCase to underline its
     bootstrapping capability. Expected usage:
     >>> path = Path('path_to_wasm_binary')
     >>> from examples.instance from MyInstance
     >>> wasm_with_python = WebAssembly(path, MyInstance)

    Args:
      path: a `Path` object to a Wasm binary
      instance_cls: the instance class that the module will be able to instantiate
    """
    loaded = None
    with open(str(path), 'rb') as bytecode:
        loaded = bytecode.read()

    return MyModule(loaded, instance_cls)


class MyModule(Module):
    _bytes = None
    _instance_cls = None

    def __init__(self, bytes_: bytes, instance_cls: Instance):
        self._bytes = bytes_
        self._instance_cls = instance_cls

    def instantiate(self):
        instance = self._instance_cls(self)
        return instance

    def serialize(self) -> bytes:
        return self._bytes

    @classmethod
    def deserialize(cls, serialized_module) -> Module:
        if not isinstance(serialized_module, bytes):
            raise ValueError('value is not bytes')
        return MyModule(serialized_module, cls._instance_cls)
