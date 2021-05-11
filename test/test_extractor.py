import unittest
from app.extractor import extract

class ExtractorTest(unittest.TestCase):

    def test_extract_only_png_images(self):
        page_string = "<html><body><img src='a.png' /><img src='b.png' /><img src='c.jpeg' /><img src='d.pNg?a=2'></body></html>"
        images = extract(page_string)
        self.assertEqual(len(images), 3)
