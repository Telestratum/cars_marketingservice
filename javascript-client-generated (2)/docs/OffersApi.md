# MarketingManagementService.OffersApi

All URIs are relative to *http://127.0.0.1:7000/userservice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOffer**](OffersApi.md#addOffer) | **POST** /offers | 
[**deleteOffer**](OffersApi.md#deleteOffer) | **DELETE** /offers/{offer_id} | 
[**getOfferDetails**](OffersApi.md#getOfferDetails) | **GET** /offers | 
[**updateOffers**](OffersApi.md#updateOffers) | **PATCH** /offers/{offer_id} | 

<a name="addOffer"></a>
# **addOffer**
> Model201OfferCreatedResponse addOffer(opts)



Add offers

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.OffersApi();
let opts = { 
  'body': new MarketingManagementService.OfferInfo() // OfferInfo | Adding offers
};
apiInstance.addOffer(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OfferInfo**](OfferInfo.md)| Adding offers | [optional] 

### Return type

[**Model201OfferCreatedResponse**](Model201OfferCreatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteOffer"></a>
# **deleteOffer**
> Model200OfferDeletedResponse deleteOffer(offerId)



delete offers

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.OffersApi();
let offerId = "offerId_example"; // String | 

apiInstance.deleteOffer(offerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offerId** | **String**|  | 

### Return type

[**Model200OfferDeletedResponse**](Model200OfferDeletedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getOfferDetails"></a>
# **getOfferDetails**
> OfferDetails getOfferDetails()



Get offers

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.OffersApi();
apiInstance.getOfferDetails((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OfferDetails**](OfferDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="updateOffers"></a>
# **updateOffers**
> Model200UpdateOfferResponse updateOffers(offerId, opts)



update offers

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.OffersApi();
let offerId = "offerId_example"; // String | 
let opts = { 
  'body': new MarketingManagementService.UpdateOfferInfo() // UpdateOfferInfo | Adds price and offers
};
apiInstance.updateOffers(offerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offerId** | **String**|  | 
 **body** | [**UpdateOfferInfo**](UpdateOfferInfo.md)| Adds price and offers | [optional] 

### Return type

[**Model200UpdateOfferResponse**](Model200UpdateOfferResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

