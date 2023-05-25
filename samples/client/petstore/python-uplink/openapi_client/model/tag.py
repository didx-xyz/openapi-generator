# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class Tag(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Tag - a model defined in OpenAPI
        id: The id of this Tag [Optional].
        name: The name of this Tag [Optional].
    """

    id: Optional[int] = None
    name: Optional[str] = None


    class Config:
        allow_population_by_field_name = True


Tag.update_forward_refs()
