from pathlib import Path

from wasmer import Instance as raw_instance
from webassembly.instance import Instance
from examples.module import MyModule


class MyInstance(Instance):
    parent_module = None
    wasm_instance = None

    def __init__(self, module: MyModule = None):
        self.parent_module = module
        self.has_module = has_module = module is not None
        if has_module:
            self.wasm_instance = raw_instance(module._bytes)

    @property
    def exports(self):
        if self.has_module:
            return self.wasm_instance.exports
        return None

    @property
    def memory(self):
        if self.has_module:
            return self.wasm_instance.memory
        return None
