#!/usr/bin/python3
"""
    this file will hold the unitest for the City
    class
"""
import unittest
import models
from models.city import City
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """this will run a verity of tests on the City class"""
    def setUp(self):
        self.inst = City()
        self.inst_string = str(self.inst)

    def test_id_type(self):
        """test the type of the attr"""
        self.assertEqual(str, type(self.inst.id))

    def test_created_at(self):
        """test the type of the attr"""
        self.assertEqual(datetime, type(self.inst.created_at))

    def test_updated_at(self):
        """test the type of the attr"""
        self.assertEqual(datetime, type(self.inst.updated_at))

    def test_init(self):
        """test the class name and id and dict exictance"""
        self.assertTrue(self.inst.__class__.__name__ in self.inst_string)
        self.assertTrue(self.inst.id in self.inst_string)
        self.assertTrue(str(self.inst.__dict__) in self.inst_string)

    def test_init_with_attr(self):
        """checks the format of the object and attr"""
        custom_dict = {
            "id": "1",
            "created_at": "2023-06-08T00:00:00",
            "updated_at": "2024-08-07T12:34:23",
            "name": "hamza"
        }
        inst = City(**custom_dict)
        self.assertEqual(inst.id, custom_dict["id"])
        self.assertEqual(inst.created_at,
                         datetime.fromisoformat(custom_dict["created_at"]))
        self.assertEqual(inst.updated_at,
                         datetime.fromisoformat(custom_dict["updated_at"]))
        self.assertTrue(hasattr(inst, "name"))
        self.assertEqual(inst.name, "hamza")

    def test_no_args(self):
        """test instantiation with no attr"""
        inst = City(None)
        self.assertNotIn(None, inst.__dict__.values())
        self.assertEqual(City, type(City()))

    def test_check_id(self):
        """check if the id is deff from each isnt"""
        insttest = City()
        self.assertNotEqual(insttest.id, self.inst.id)

    def test_check_creation_time(self):
        """check the time deff of every object created"""
        insttest = City()
        self.assertNotEqual(insttest.created_at, self.inst.created_at)
        self.assertGreater(insttest.created_at, self.inst.created_at)

    def test_init_with_on_kwagr(self):
        """check if we can create the object using kwargs"""
        testinst = City(34, 32, 45, id="86754432")
        self.assertEqual(testinst.id, "86754432")
        self.assertEqual(testinst.created_at, testinst.updated_at)

    def test_all(self):
        """test the function all if its working properly"""
        self.assertIn(City(), models.storage.all().values())

    def test_str(self):
        """test the str function is it returning the result we want"""
        self.assertTrue(self.inst.__class__.__name__ in self.inst_string)
        self.assertTrue(self.inst.id in self.inst_string)
        self.assertTrue(str(self.inst.__dict__) in self.inst_string)

    def test_dict_func_dict__(self):
        """test the dict function is it returning the proper dict"""
        self.assertNotEqual(self.inst.to_dict(), self.inst.__dict__)

    def test_to_dict(self):
        """checking if dict has the arguments"""
        inst_dict = self.inst.to_dict()
        self.assertIsInstance(inst_dict, dict)
        self.assertEqual(inst_dict['__class__'], 'City')
        self.assertEqual(inst_dict['id'], self.inst.id)
        self.assertEqual(inst_dict['created_at'],
                         self.inst.created_at.isoformat())
        self.assertEqual(inst_dict['updated_at'],
                         self.inst.updated_at.isoformat())

    def test_dict_fomat(self):
        """this well check the dict format if we use dict"""
        self.inst.id = "h1h2h3h4h5h6"
        todaysDate = datetime.today()
        self.inst.created_at = todaysDate
        self.inst.updated_at = todaysDate
        testDict = {
            "id": "h1h2h3h4h5h6",
            "__class__": "City",
            "created_at": todaysDate.isoformat(),
            "updated_at": todaysDate.isoformat()
        }
        self.assertDictEqual(testDict, self.inst.to_dict())

    def test_to_dict_with_custom_attr(self):
        """test to dict with costum attribute"""
        self.inst.name = "hamza"
        self.inst.age = 23
        self.assertIn("name", self.inst.to_dict())
        self.assertIn("age", self.inst.to_dict())
        self.assertEqual(self.inst.__dict__["name"], "hamza")
        self.assertEqual(self.inst.__dict__["age"], 23)

    def test_to_dict_custom_attr(self):
        """test to dict with costum attribute"""
        self.inst.name = "name_str"
        inst_dict = self.inst.to_dict()
        self.assertEqual(inst_dict['name'], "name_str")

    def test_created_at(self):
        """check the creation time"""
        self.assertEqual(self.inst.created_at, self.inst.updated_at)

    def test_check_saving_format(self):
        """check the saving format"""
        try:
            self.inst.save()
            with open("file.json", "r") as file:
                format_inst = "City." + self.inst.id
                self.assertIn(format_inst, file.read())
        except (FileNotFoundError):
            pass

    def test_save(self):
        """test the save method"""
        inst_update = self.inst.updated_at
        self.inst.save()
        self.assertNotEqual(inst_update, self.inst.updated_at)

    def test_save_n(self):
        """test the save method multiple times"""
        inst_updated_at = self.inst.updated_at
        self.inst.save()
        self.assertNotEqual(inst_updated_at, self.inst.updated_at)
        after_save_n_one = self.inst.updated_at
        self.inst.save()
        self.assertNotEqual(after_save_n_one, self.inst.updated_at)

    def test_save_with_no_args(self):
        """test save with no arrgs and passing None"""
        with self.assertRaises(TypeError):
            self.inst.save(None)

    def test_datetime(self):
        """test date time deff from instances"""
        date = datetime.now()
        self.inst.save()
        date_after = datetime.now()
        self.assertLessEqual(date, self.inst.updated_at)
        self.assertLessEqual(self.inst.updated_at, date_after)


if __name__ == '__main__':
    unittest.main()
