import unittest
import config_manager


class TestConfigManagement(unittest.TestCase):

    def setUp(self):
        self.conf = config_manager.ConfigManager('sample.config')

    def test_conf_management(self):
        self.assertEqual(self.conf.config.get('sample'), 'file')
        self.assertEqual(self.conf.config.get('key'), 'value')
        self.assertTrue(isinstance(self.conf.config, dict))
        self.assertTrue(len(self.conf.config) == 2)


if __name__ == '__main__':
    unittest.main()
