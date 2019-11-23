import unittest
from pathlib import Path
from os.path import join, dirname, abspath

from examples.instance import MyInstance


class TestParentClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from examples.module import WebAssembly
        path_str = join(dirname(dirname(abspath(__file__))),
                        'binaries', 'tests_binary.wasm')
        cls.path = path = Path(path_str)
        cls.module = WebAssembly(path, MyInstance)