from genericpath import exists

from conf import configRW

import os
import unittest

configRW.hello()

class TestConfigRW(unittest.TestCase):
    def setUp(self):
        # Create paths
        global root, rootConfig
        root = None
        rootConfig = None
        root = os.path.dirname(os.path.abspath(__file__))
        rootConfig = os.path.join(root, "../../configure")
        rootPlists = os.path.join(rootConfig, "plists")
        os.chdir(root)
        
    def test_gen(self):
        # configRW.genConfig(root, rootConfig)
        configRW.configRunner(root, rootConfig)
        self.assertTrue(os.path.isdir(rootConfig), "Folder exists")
        self.assertTrue(exists(os.path.join(rootConfig, "config.yml")), "Config exists")



if __name__ == '__main__':
    unittest.main()

# export PYTHONPATH=/home/user/git/sp-base