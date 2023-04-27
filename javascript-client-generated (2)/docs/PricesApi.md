# MarketingManagementService.PricesApi

All URIs are relative to *http://127.0.0.1:7000/userservice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPrice**](PricesApi.md#addPrice) | **POST** /prices | 
[**deletePrice**](PricesApi.md#deletePrice) | **DELETE** /price/{price_id} | 
[**getPrice**](PricesApi.md#getPrice) | **GET** /price/{price_id} | 
[**getPrices**](PricesApi.md#getPrices) | **GET** /prices | 

<a name="addPrice"></a>
# **addPrice**
> Model201PriceCreatedResponse addPrice(opts)



Add price to cars

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.PricesApi();
let opts = { 
  'body': new MarketingManagementService.PriceInfo() // PriceInfo | Adding price
};
apiInstance.addPrice(opts, (error, data, response) => {
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
 **body** | [**PriceInfo**](PriceInfo.md)| Adding price | [optional] 

### Return type

[**Model201PriceCreatedResponse**](Model201PriceCreatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deletePrice"></a>
# **deletePrice**
> Model200PriceDeletedResponse deletePrice(priceId)



Delete price

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.PricesApi();
let priceId = "priceId_example"; // String | 

apiInstance.deletePrice(priceId, (error, data, response) => {
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
 **priceId** | **String**|  | 

### Return type

[**Model200PriceDeletedResponse**](Model200PriceDeletedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getPrice"></a>
# **getPrice**
> PriceDetails getPrice(priceId)



get unique id

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.PricesApi();
let priceId = "priceId_example"; // String | 

apiInstance.getPrice(priceId, (error, data, response) => {
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
 **priceId** | **String**|  | 

### Return type

[**PriceDetails**](PriceDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getPrices"></a>
# **getPrices**
> PriceDetails getPrices()



Get prices

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.PricesApi();
apiInstance.getPrices((error, data, response) => {
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

[**PriceDetails**](PriceDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applications/json, application/json

