# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class Order(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Order - a model defined in OpenAPI
        id: The id of this Order [Optional].
        pet_id: The pet_id of this Order [Optional].
        quantity: The quantity of this Order [Optional].
        ship_date: The ship_date of this Order [Optional].
        status: Order Status [Optional].
        complete: The complete of this Order [Optional].
    """

    id: Optional[int] = None
    pet_id: Optional[int] = Field(None, alias="petId")
    quantity: Optional[int] = None
    ship_date: Optional[datetime] = Field(None, alias="shipDate")
    status: Optional[Literal["placed", "approved", "delivered"]] = None
    complete: Optional[bool] = None

    def __init__(
        self,
        *,
        id: Optional[int] = None,
        pet_id: Optional[int] = None,
        quantity: Optional[int] = None,
        ship_date: Optional[datetime] = None,
        status: Optional[Literal["placed", "approved", "delivered"]] = None,
        complete: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


Order.update_forward_refs()
