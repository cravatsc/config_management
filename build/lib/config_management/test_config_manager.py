import unittest
import config_manager


class TestConfigManagement(unittest.TestCase):

    def setUp(self):
        self.conf = config_manager.ConfigManager('sample.config')

    def test_conf_management(self):
        self.assertEqual(self.conf.get('sample'), 'file')
        self.assertEqual(self.conf.get('key'), 'value')
        self.assertTrue(isinstance(self.conf.config, dict))
        self.assertTrue(len(self.conf.config) == 3)
        self.assertNotIn('#test',self.conf.config.keys())
        self.assertEqual(self.conf.get('twoequals'), 'test=two')


if __name__ == '__main__':
    unittest.main()
