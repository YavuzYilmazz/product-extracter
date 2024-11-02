from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Product:
    stock_code: str
    color: List[str]
    discounted_price: float
    images: List[str]
    is_discounted: bool
    name: str
    price: float
    price_unit: str
    product_type: str
    quantity: int
    series: str
    status: str
    fabric: str
    model_measurements: str
    product_measurements: str
    createdAt: str
    updatedAt: str
    product_information: str

    def to_dict(self):
        return asdict(self)
