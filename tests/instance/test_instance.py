import unittest
from pathlib import Path
from os.path import join, dirname, abspath

from examples.instance import MyInstance
from tests import TestParentClass


class TestInstance(TestParentClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_instance_from_module(self):
        instance = MyInstance(self.module)
        assert instance.wasm_instance is not None


if __name__ == '__main__':
    unittest.main()