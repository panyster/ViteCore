# test_vitecore.py
"""
Tests for ViteCore module.
"""

import unittest
from vitecore import ViteCore

class TestViteCore(unittest.TestCase):
    """Test cases for ViteCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ViteCore()
        self.assertIsInstance(instance, ViteCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ViteCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
