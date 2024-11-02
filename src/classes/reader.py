import xml.etree.ElementTree as ET
from datetime import datetime
from .extractor import Extractor
from .product import Product

class Reader:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_xml(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()

        products = []
        for product in root.findall('Product'):
            item = Product(
                stock_code=product.attrib.get('ProductId'),
                color=[product.find('ProductDetails/ProductDetail[@Name="Color"]').attrib.get('Value')],
                discounted_price=float(product.find('ProductDetails/ProductDetail[@Name="DiscountedPrice"]').attrib.get('Value').replace(',', '.')),
                images=[img.attrib['Path'] for img in product.find('Images').findall('Image')],
                is_discounted=float(product.find('ProductDetails/ProductDetail[@Name="DiscountedPrice"]').attrib.get('Value').replace(',', '.')) < float(product.find('ProductDetails/ProductDetail[@Name="Price"]').attrib.get('Value').replace(',', '.')),
                name=product.attrib.get('Name'),
                price=float(product.find('ProductDetails/ProductDetail[@Name="Price"]').attrib.get('Value').replace(',', '.')),
                price_unit="USD",
                product_type=product.find('ProductDetails/ProductDetail[@Name="ProductType"]').attrib.get('Value'),
                quantity=int(product.find('ProductDetails/ProductDetail[@Name="Quantity"]').attrib.get('Value')),
                series=product.find('ProductDetails/ProductDetail[@Name="Series"]').attrib.get('Value'),
                status="Active",
                fabric=Extractor.extract_fabric_from_description(product.find('Description')),
                model_measurements=Extractor.extract_model_measurements(product.find('Description')),
                product_measurements=Extractor.extract_product_measurements(product.find('Description')),
                createdAt=datetime.now().isoformat(),  # Serialize datetime
                updatedAt=datetime.now().isoformat(),  # Serialize datetime
                product_information=Extractor.extract_product_information(product.find('Description'))
            )

            products.append(item)

        return products
