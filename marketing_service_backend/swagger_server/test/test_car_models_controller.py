# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.carmodeldetails import Carmodeldetails  # noqa: E501
from swagger_server.models.carmodelinfo import Carmodelinfo  # noqa: E501
from swagger_server.models.model201_car_model_created_response import Model201CarModelCreatedResponse  # noqa: E501
from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model409_conflict_response import Model409ConflictResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCarModelsController(BaseTestCase):
    """CarModelsController integration test stubs"""

    def test_add_car_model(self):
        """Test case for add_car_model

        
        """
        body = {
            "model_type": "SUVs",
            "model_name": "Bolero",
            "transmission": "automatic",
            "fuel_type": "diesel",
            "trim": "SE"
            }
        response = self.client.open(
            '/marketingservice/v1/cars/models',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_car_models(self):
        """Test case for get_car_models

        
        """
        response = self.client.open(
            '/marketingservice/v1/cars/models',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_car_modeltype(self):
        """Test case for get_car_modeltype

        
        """
        response = self.client.open(
            '/marketingservice/v1/cars/models/{model_type}'.format(model_type='model_type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        


if __name__ == '__main__':
    import unittest
    unittest.main()
