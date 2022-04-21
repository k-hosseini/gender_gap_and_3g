from unittest import TestCase
from gender_gaps import maps

class TestMaps(TestCase):

    # a funny test
    def test_temp(self):
        result = maps.temp(19)
        self.assertEqual(result,19)
    
    # the number shapefiles road = 4. i.e Country, Provinces, Counties, Cities
    def test_import_shapefiles(self):
        result= maps.load_Iran_shape_files()
        self.assertEqual(len(result),4)
    
    # Coverage rate must be a positive number less than zero
    def test_coverage_rate(self):
        result= maps.coverage_rate()[1]["coverage_rate"]
        
        self.assertFalse(((result>1).any()) or ((result<0).any()))
    
    # number of cities received 3g coverage must be less than the number of cities.
    def test_cov_map(self):
        self.assertLessEqual(len(maps.coverage_map()) ,len(maps.load_Iran_shape_files()["Cities"]) )
