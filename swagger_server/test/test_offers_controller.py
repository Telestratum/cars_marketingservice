# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.model200_offer_deleted_response import Model200OfferDeletedResponse  # noqa: E501
from swagger_server.models.model200_update_offer_response import Model200UpdateOfferResponse  # noqa: E501
from swagger_server.models.model201_offer_created_response import Model201OfferCreatedResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model409_conflict_response import Model409ConflictResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server.models.offer_details import OfferDetails  # noqa: E501
from swagger_server.models.offer_info import OfferInfo  # noqa: E501
from swagger_server.models.update_offer_info import UpdateOfferInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOffersController(BaseTestCase):
    """OffersController integration test stubs"""

    def test_add_offer(self):
        """Test case for add_offer

        
        """
        body = {
            "discount_pct": 5,
            "start_date": "2/4/2023",
            "end_date": "2/5/2023",
            "applicable_models": [
                "SUVs","Sedan"
            ]
            }
        response = self.client.open(
            '/marketingservice/v1/offers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_offer(self):
        """Test case for delete_offer

        
        """
        response = self.client.open(
            '/marketingservice/v1/offers/{offer_id}'.format(offer_id="9c3a5f45c2f8498bb3f9d5603ef0f10b"),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_offer_details(self):
        """Test case for get_offer_details

        
        """
        response = self.client.open(
            '/marketingservice/v1/offers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_offers(self):
        """Test case for update_offers

        
        """
        body = {
                "start_date":"4/4/2023"
            }
        response = self.client.open(
            '/marketingservice/v1/offers/{offer_id}'.format(offer_id="a516894d97da4b8e8a013c5a72663e5a"),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
