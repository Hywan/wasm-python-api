import unittest
from pathlib import Path
from os.path import join, dirname, abspath

from examples.instance import MyInstance


class TestInstance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from examples.module import WebAssembly
        path_str = join(dirname(dirname(dirname(abspath(__file__)))),
                        'binaries', 'tests_binary.wasm')
        cls.path = path = Path(path_str)
        cls.module = WebAssembly(path)

    def test_instance(self):
        instance = MyInstance(self.module)
        assert instance.wasm_instance is not None


if __name__ == '__main__':
    unittest.main()