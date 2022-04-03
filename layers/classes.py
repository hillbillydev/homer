from dataclasses import dataclass
from typing import Any, List
from uuid import UUID

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class SaleType:
    minUnit: int
    type: str  # noqa: A003, VNE003
    stepSize: int
    unit: str


@dataclass_json
@dataclass
class Product:
    productId: str
    quantity: float
    sale_type: str
    name: str
    price: int
    catalogPrice: int
    hasBadge: bool
    badgeImageUrl: str
    imageUrl: str
    restricted: bool
    tobacco: bool
    liquor: bool
    saleTypes: List[SaleType]
    weightDisplayName: str
    brand: str
    categoryName: str
    promoBadgeImageTitle: str
    promotionCode: str


@dataclass_json
@dataclass
class Store:
    storeId: UUID
    storeName: str
    storeAddress: str
    storeRegion: str


@dataclass_json
@dataclass
class AddProductsResponse:
    products: List[Product]
    unavailableProducts: List[Any]  # TODO figure this one out.
    subtotal: float
    promoCodeDiscount: float
    saving: float
    serviceFee: float
    bagFee: float
    store: Store
    orderNumber: int
    allowSubstitutions: bool
    wasRepriced: bool
