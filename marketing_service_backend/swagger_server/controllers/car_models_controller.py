import connexion
import six
import uuid
from pymongo import MongoClient
from flask import jsonify , request
import ast
import json
import logging,logging.config

from swagger_server.models.carmodeldetails import Carmodeldetails  # noqa: E501
from swagger_server.models.carmodelinfo import Carmodelinfo  # noqa: E501
from swagger_server.models.model201_car_model_created_response import Model201CarModelCreatedResponse  # noqa: E501
from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model409_conflict_response import Model409ConflictResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server import util

cluster = MongoClient("localhost",27017)
carDatabase = cluster.carDatabase
car_models = carDatabase.car_models

logging.basicConfig(filename="newfile1.log",format="%(filename)s::%(levelname)s:%(message)s",level=logging.DEBUG)


def add_car_model(body=None):  # noqa: E501
    """add_car_model

    Add one car model # noqa: E501

    :param body: Adds a car model
    :type body: dict | bytes

    :rtype: Model201CarModelCreatedResponse
    """
    if connexion.request.is_json:
        # body = Carmodelinfo.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            # if car_models.find_one({"model_type":body['model_type']}):
            #     return "model already exist"

            # else:
                body.update({"model_id" : (uuid.uuid4().hex)})
                data = car_models.insert_one(body)
                return "Car model created", 200
        except 401:
            return "unauthorized", 401
        except 403:
            return "Forbidden", 403
        except 404:
            return "Not found", 404
        except 503:
            return "server unavailable", 503
        except 500:
            return "Internal server error",500


def get_car_models():  # noqa: E501
    """get_car_models

    Get details of all car models # noqa: E501


    :rtype: Carmodeldetails
    """
    try:
        data = car_models.find()
        data_list = []
        for i in list(data):
            i["_id"]=str (i["_id"])

            data_list.append(i)
        return data_list,200
    except 401:
        return "unauthorized", 401
    except 403:
        return "Forbidden", 403
    except 404:
        return "Not found", 404
    except 503:
        return "server unavailable", 503
    except:
        return "Inetrnal server error"



def get_car_modeltype(model_type):  # noqa: E501
    """get_car_modeltype

    Get details of all car models # noqa: E501

    :param model_type: 
    :type model_type: str

    :rtype: Carmodeldetails
    """
    try:

        data=car_models.find({"model_type":model_type})
        data_list=[]
        for i in data:
                i["_id"]=str(i["_id"])
                data_list.append(i)
                return data_list,200
        else:
            return "modeltype not exist"
    except 401:
        return "unauthorized", 401
    except 403:
        return "Forbidden", 403
    except 404:
        return "Not found", 404
    except 503:
        return "server unavailable", 503
    except:
        return "Internal error",500
