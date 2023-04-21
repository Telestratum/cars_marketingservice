import connexion
import six
import uuid
from pymongo import MongoClient
from flask import jsonify , request
import ast
import json
import logging,logging.config

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
from swagger_server import util

cluster = MongoClient("localhost",27017)
carDatabase = cluster.carDatabase
car_offers = carDatabase.car_offers

logging.basicConfig(filename="newfile2.log",format="%(filename)s::%(levelname)s:%(message)s",level=logging.DEBUG)


def add_offer(body=None):  # noqa: E501
    """add_offer

    Add offers # noqa: E501

    :param body: Adding offers
    :type body: dict | bytes

    :rtype: Model201OfferCreatedResponse
    """
    if connexion.request.is_json:
        # body = OfferInfo.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if car_offers.find_one({"applicable_models":body['applicable_models']}):
                return "offer already exist"
            else:
                body.update({"offer_id" : (uuid.uuid4().hex)})
                data = car_offers.insert_one(body)
                return "Car_model offer created", 200
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



def delete_offer(offer_id):  # noqa: E501
    """delete_offer

    delete offers # noqa: E501

    :param offer_id: 
    :type offer_id: str

    :rtype: Model200OfferDeletedResponse
    """
    try:
        
        if car_offers.find_one({"offer_id":offer_id}):
            delete_user = car_offers.delete_one({"offer_id":offer_id})
            return "successfully deleted",200
        else:
            return "Offer_id is not found"
    except 401:
            return "unauthorized", 401
    except 403:
        return "Forbidden", 403
    except 404:
        return "Not found", 404
    except 503:
        return "server unavailable", 503
    except:
        return "Internal server error",500


def get_offer_details():  # noqa: E501
    """get_offer_details

    Get offers # noqa: E501


    :rtype: OfferDetails
    """
    try:
        data = car_offers.find()
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

def update_offers(offer_id, body=None):  # noqa: E501
    """update_offers

    update offers # noqa: E501

    :param offer_id: 
    :type offer_id: str
    :param body: Adds price and offers
    :type body: dict | bytes

    :rtype: Model200UpdateOfferResponse
    """
    if connexion.request.is_json:
        body = UpdateOfferInfo.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
            car_offers.update_many({"offer_id":offer_id},{"$set":body})
            return "successfully updated",200
        except 401:
            return "unauthorized", 401
        except 403:
            return "Forbidden", 403
        except 404:
            return "Not found", 404
        except 503:
            return "server unavailable", 503
        except:
            return "Internal server error",500
