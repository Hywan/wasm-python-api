import unittest
from pathlib import Path
from os.path import join, dirname, abspath

from examples.instance import MyInstance
from tests import TestParentClass


class TestModule(TestParentClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_module(self):
        assert isinstance(self.module._bytes, bytes)

    def test_instantiate(self):
        instance = self.module.instantiate()
        assert isinstance(instance, MyInstance)


if __name__ == '__main__':
    unittest.main()
