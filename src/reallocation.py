# Brokerage
# Account
# SYmbol
# Type
# Current Value
# Target

from enum import Enum


class Brokerage(Enum):
    FIDELITY = "Fidelity"
    VANGUARD = "Vanguard"


class Account(Enum):
    INDIVIDUAL = "Individual"
    SIMPLE_IRA = "Simple IRA"
    HSA = "HSA"


class AssetType(Enum):
    US_STOCK = "US Stock"
    INT_STOCK = "Int Stock"
    US_BOND = "US Bond"
    CASH = "Cash"


allocation_targets = {
    AssetType.US_STOCK.value: 0.6,
    AssetType.INT_STOCK.value: 0.3,
    AssetType.US_BOND.value: 0.1,
    AssetType.CASH.value: 0,
}

current_allocations = {
    "Brokerage": ["Fidelity"] * 7,
    "Account": [
        "Individual",
        "Simple IRA",
        "Simple IRA",
        "Simple IRA",
        "Simple IRA",
        "HSA",
        "HSA",
    ],
    "Symbol": ["FXAIX", "FSKAX", "FSPSX", "FXNAX", "Cash", "FXAIX", "Cash"],
    "Type": [
        "US Stock",
        "US Stock",
    ],
}
print(allocation_targets)
