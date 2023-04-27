import connexion
import six
import uuid
from pymongo import MongoClient
from flask import jsonify , request
import ast
import json
import logging,logging.config

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
from swagger_server import util

cluster = MongoClient("localhost",27017)
carDatabase = cluster.carDatabase
car_price = carDatabase.car_price
car_models = carDatabase.car_models

logging.basicConfig(filename="newfile3.log",format="%(filename)s::%(levelname)s:%(message)s",level=logging.DEBUG)


def add_price(body=None):  # noqa: E501
    """add_price

    Add price to cars # noqa: E501

    :param body: Adding price
    :type body: dict | bytes

    :rtype: Model201PriceCreatedResponse
    """
    if connexion.request.is_json:
        # body = PriceInfo.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if car_models.find_one({"model_id":body['model_id']}):
                if car_price.find_one({"model_id":body['model_id']}):
                    return "price already exist",
                else:
                    body.update({"price_id" : (uuid.uuid4().hex)})
                    data = car_price.insert_one(body)
                    return "Car_model price created", 201
            else:
                return "model_id Not found",404

        except 500:
            return "Internal_server_error",500


def delete_price(price_id):  # noqa: E501
    """delete_price

    Delete price # noqa: E501

    :param price_id: 
    :type price_id: str

    :rtype: Model200PriceDeletedResponse
    """
    try:
        
        if car_price.find_one({"price_id":price_id}):
            delete_user = car_price.delete_one({"price_id":price_id})
            return "successfully deleted",200
        else:
            return "Price_id is Not Found", 404
    
    except:
        return "Internal_server_error",500

def get_price(price_id):  # noqa: E501
    """get_price

    get unique id # noqa: E501

    :param price_id: 
    :type price_id: str

    :rtype: PriceDetails
    """
    try:
        data=car_price.find({"price_id":price_id})
        data_list=[]
        for i in data:
                i["_id"]=str(i["_id"])
                data_list.append(i)
                return data_list,200
        else:
            return "Price_id Not exist",404
    
    except:
        return "Internal_server_error",500


def get_prices():  # noqa: E501
    """get_prices

    Get prices # noqa: E501


    :rtype: PriceDetails
    """
    try:
        data = car_price.find()
        data_list = []
        for i in list(data):
            i["_id"]=str (i["_id"])

            data_list.append(i)
            return data_list,200
    except:
        return "Inetrnal_server_error",500