# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.model200_price_deleted_response import Model200PriceDeletedResponse  # noqa: E501
from swagger_server.models.model201_price_created_response import Model201PriceCreatedResponse  # noqa: E501
from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model409_conflict_response import Model409ConflictResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server.models.price_details import PriceDetails  # noqa: E501
from swagger_server.models.price_info import PriceInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPricesController(BaseTestCase):
    """PricesController integration test stubs"""

    def test_add_price(self):
        """Test case for add_price

        
        """
        body = {
                "model_id": "d2c5bca8ee9f43468c9e0e963682120b",
                "price": 2000000,
                "start_date": "2/4/2023",
                "end_date": "2/7/2023"
                }
        response = self.client.open(
            '/marketingservice/v1/prices',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_price(self):
        """Test case for delete_price

        
        """
        response = self.client.open(
            '/marketingservice/v1/price/{price_id}'.format(price_id='403f06fe562c4024aaefc7b375ec6a6d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_price(self):
        """Test case for get_price

        
        """
        response = self.client.open(
            '/marketingservice/v1/price/{price_id}'.format(price_id='403f06fe562c4024aaefc7b375ec6a6d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_prices(self):
        """Test case for get_prices

        
        """
        response = self.client.open(
            '/marketingservice/v1/prices',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
