#!/usr/bin/python3
"""
test the edge cases from the filestorage class"""
from models.engine.file_storage import FileStorage
from json import load, dump
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime
from models import storage
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """this unit test test possible edge cases fro the FileStorage
    class"""

    def setUp(self):
        self.file_path = 'file.json'
        self.inst = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_inst_type(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_attr(self):
        self.assertTrue(hasattr(self.inst, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.inst, '_FileStorage__objects'))

    def test_attr_types(self):
        self.assertEqual(type(self.inst._FileStorage__file_path), str)
        self.assertEqual(type(self.inst._FileStorage__objects), dict)

    def test_no_attr(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all_method(self):
        objects = self.inst.all()
        self.assertEqual(type(objects), dict)
        self.assertEqual(type(storage.all()), dict)
        self.assertIs(objects, self.inst._FileStorage__objects)

    def test_all_with_no_attr(self):
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_none(self):
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_new_attr(self):
        with self.assertRaises(TypeError):
            inst = User()
            storage.new(inst, 'ok')

    def test_new_method_base(self):
        inst = BaseModel()
        storage.new(inst)
        self.assertIn("BaseModel." + inst.id, storage.all().keys())

    def test_new_method_User(self):
        inst = User()
        storage.new(inst)
        self.assertIn("User." + inst.id, storage.all().keys())

    def test_new_method_place(self):
        inst = Place()
        storage.new(inst)
        self.assertIn("Place." + inst.id, storage.all().keys())

    def test_new_method_city(self):
        inst = City()
        storage.new(inst)
        self.assertIn("City." + inst.id, storage.all().keys())

    def test_new_method_state(self):
        inst = State()
        storage.new(inst)
        self.assertIn("State." + inst.id, storage.all().keys())

    def test_new_method_Review(self):
        inst = Review()
        storage.new(inst)
        self.assertIn("Review." + inst.id, storage.all().keys())

    def test_new_method_amenity(self):
        inst = Amenity()
        storage.new(inst)
        self.assertIn("Amenity." + inst.id, storage.all().keys())

    def test_save_with_no_args(self):
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_save_a_new_user(self):
        new_inst = User()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_basemodel(self):
        new_inst = BaseModel()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_place(self):
        new_inst = Place()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_state(self):
        new_inst = State()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_amenity(self):
        new_inst = Amenity()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_review(self):
        new_inst = Review()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_city(self):
        new_inst = City()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_reload_with_none(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_reload_with_basemodel(self):
        inst = BaseModel()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_user(self):
        inst = User()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_Place(self):
        inst = Place()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_State(self):
        inst = State()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_city(self):
        inst = City()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_amenity(self):
        inst = Amenity()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_review(self):
        inst = Review()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)


if __name__ == '__main__':
    unittest.main()
