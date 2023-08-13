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
        """test the type if it is FileStorgae"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_attr(self):
        """test if the instance has the defined attrebutes"""
        self.assertTrue(hasattr(self.inst, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.inst, '_FileStorage__objects'))

    def test_attr_types(self):
        """test the type of the attrebutes"""
        self.assertEqual(type(self.inst._FileStorage__file_path), str)
        self.assertEqual(type(self.inst._FileStorage__objects), dict)

    def test_no_attr(self):
        """Test if constructor with None"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all_method(self):
        """test the all method"""
        objects = self.inst.all()
        self.assertEqual(type(objects), dict)
        self.assertEqual(type(storage.all()), dict)
        self.assertIs(objects, self.inst._FileStorage__objects)

    def test_all_with_no_attr(self):
        """test all with no attributes"""
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_none(self):
        """test the new method  with none"""
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_new_attr(self):
        """test the new method with attributes"""
        with self.assertRaises(TypeError):
            inst = User()
            storage.new(inst, 'ok')

    def test_new_method_base(self):
        """test the new method functionality"""
        inst = BaseModel()
        storage.new(inst)
        self.assertIn("BaseModel." + inst.id, storage.all().keys())

    def test_new_method_User(self):
        """test the new method on the user class"""
        inst = User()
        storage.new(inst)
        self.assertIn("User." + inst.id, storage.all().keys())

    def test_new_method_place(self):
        """test the new method on the places class"""
        inst = Place()
        storage.new(inst)
        self.assertIn("Place." + inst.id, storage.all().keys())

    def test_new_method_city(self):
        """test the new method on the city class"""
        inst = City()
        storage.new(inst)
        self.assertIn("City." + inst.id, storage.all().keys())

    def test_new_method_state(self):
        """test the new method on the state class"""
        inst = State()
        storage.new(inst)
        self.assertIn("State." + inst.id, storage.all().keys())

    def test_new_method_Review(self):
        """test the new method on the review class"""
        inst = Review()
        storage.new(inst)
        self.assertIn("Review." + inst.id, storage.all().keys())

    def test_new_method_amenity(self):
        """test the new method on the amenity class"""
        inst = Amenity()
        storage.new(inst)
        self.assertIn("Amenity." + inst.id, storage.all().keys())

    def test_save_with_no_args(self):
        """test the save method with no args"""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_save_a_new_user(self):
        """test the save method with the user class"""
        new_inst = User()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_basemodel(self):
        """test the save method with the baseModel class"""
        new_inst = BaseModel()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_place(self):
        """test the save method with the place class"""
        new_inst = Place()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_state(self):
        """test the save method with the state class"""
        new_inst = State()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_amenity(self):
        """test the save method with the amenity class"""
        new_inst = Amenity()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_review(self):
        """test the save method with the review class"""
        new_inst = Review()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_save_a_new_city(self):
        """test the save method with the city class"""
        new_inst = City()
        self.inst.new(new_inst)
        self.inst.save()
        with open(self.file_path, 'r') as file:
            info = load(file)
            key = '{}.{}'.format(new_inst.__class__.__name__, new_inst.id)
            self.assertTrue(key in info)

    def test_reload_with_none(self):
        """test reload method with no args """
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_reload_with_basemodel(self):
        """test the reload method on the basemodel"""
        inst = BaseModel()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_user(self):
        """test the reload method on the user"""
        inst = User()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_Place(self):
        """test the reload method on the place"""
        inst = Place()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_State(self):
        """test the reload method on the state"""
        inst = State()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_city(self):
        """test the reload method on the city"""
        inst = City()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_amenity(self):
        """test the reload method on the amenity"""
        inst = Amenity()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)

    def test_reload_with_review(self):
        """test the reload method on the review"""
        inst = Review()
        storage.new(inst)
        storage.save()
        storage.reload()
        objects_list = FileStorage._FileStorage__objects
        key = '{}.{}'.format(inst.__class__.__name__, inst.id)
        self.assertIn(key, objects_list)


if __name__ == '__main__':
    unittest.main()
