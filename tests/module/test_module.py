import unittest
from pathlib import Path
from os.path import join, dirname, abspath

from examples.module import MyModule


class TestValue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from examples.module import WebAssembly
        path_str = join(dirname(dirname(dirname(abspath(__file__)))),
                        'binaries', 'tests_binary.wasm')
        cls.path = path = Path(path_str)
        cls.module = WebAssembly(path)

    def test_module(self):
        assert isinstance(self.module._bytes, bytes)


if __name__ == '__main__':
    unittest.main()
