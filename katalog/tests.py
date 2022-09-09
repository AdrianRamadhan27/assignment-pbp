from django.test import TestCase
from katalog.models import CatalogItem
# Create your tests here.

class TestModels(TestCase):
    def setUp(self):
        self.catalog_item1 = CatalogItem.objects.create(
            item_name= "Nike Air Jordan FISIP",
            item_price = 3789000,
            description = "Nike Original Made In Taiwan",
            item_stock = 30,
            rating = 4,
            item_url = "https://www.tokopedia.com/807garage/air-jordan-1-mid-multicolour"
        )

    def test_catalog_item(self):
        self.assertTrue(isinstance(self.catalog_item1, CatalogItem))
   
