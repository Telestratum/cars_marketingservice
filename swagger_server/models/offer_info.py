# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class OfferInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, discount_pct: float=None, start_date: date=None, end_date: date=None, applicable_models: List[str]=None):  # noqa: E501
        """OfferInfo - a model defined in Swagger

        :param discount_pct: The discount_pct of this OfferInfo.  # noqa: E501
        :type discount_pct: float
        :param start_date: The start_date of this OfferInfo.  # noqa: E501
        :type start_date: float
        :param end_date: The end_date of this OfferInfo.  # noqa: E501
        :type end_date: float
        :param applicable_models: The applicable_models of this OfferInfo.  # noqa: E501
        :type applicable_models: List[str]
        """
        self.swagger_types = {
            'discount_pct': float,
            'start_date': date,
            'end_date': date,
            'applicable_models': List[str]
        }

        self.attribute_map = {
            'discount_pct': 'discount_pct',
            'start_date': 'start_date',
            'end_date': 'end_date',
            'applicable_models': 'applicable_models'
        }
        self._discount_pct = discount_pct
        self._start_date = start_date
        self._end_date = end_date
        self._applicable_models = applicable_models

    @classmethod
    def from_dict(cls, dikt) -> 'OfferInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The offer_info of this OfferInfo.  # noqa: E501
        :rtype: OfferInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def discount_pct(self) -> float:
        """Gets the discount_pct of this OfferInfo.


        :return: The discount_pct of this OfferInfo.
        :rtype: float
        """
        return self._discount_pct

    @discount_pct.setter
    def discount_pct(self, discount_pct: float):
        """Sets the discount_pct of this OfferInfo.


        :param discount_pct: The discount_pct of this OfferInfo.
        :type discount_pct: float
        """
        if discount_pct is None:
            raise ValueError("Invalid value for `discount_pct`, must not be `None`")  # noqa: E501

        self._discount_pct = discount_pct

    @property
    def start_date(self) -> date:
        """Gets the start_date of this OfferInfo.


        :return: The start_date of this OfferInfo.
        :rtype: float
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this OfferInfo.


        :param start_date: The start_date of this OfferInfo.
        :type start_date: float
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this OfferInfo.


        :return: The end_date of this OfferInfo.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this OfferInfo.


        :param end_date: The end_date of this OfferInfo.
        :type end_date: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def applicable_models(self) -> List[str]:
        """Gets the applicable_models of this OfferInfo.


        :return: The applicable_models of this OfferInfo.
        :rtype: List[str]
        """
        return self._applicable_models

    @applicable_models.setter
    def applicable_models(self, applicable_models: List[str]):
        """Sets the applicable_models of this OfferInfo.


        :param applicable_models: The applicable_models of this OfferInfo.
        :type applicable_models: List[str]
        """
        if applicable_models is None:
            raise ValueError("Invalid value for `applicable_models`, must not be `None`")  # noqa: E501

        self._applicable_models = applicable_models
