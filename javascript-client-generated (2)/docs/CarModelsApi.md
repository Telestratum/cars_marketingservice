# MarketingManagementService.CarModelsApi

All URIs are relative to *http://127.0.0.1:7000/userservice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCarModel**](CarModelsApi.md#addCarModel) | **POST** /cars/models | 
[**getCarModels**](CarModelsApi.md#getCarModels) | **GET** /cars/models | 
[**getCarModeltype**](CarModelsApi.md#getCarModeltype) | **GET** /cars/models/{model_type} | 

<a name="addCarModel"></a>
# **addCarModel**
> Model201CarModelCreatedResponse addCarModel(opts)



Add one car model

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.CarModelsApi();
let opts = { 
  'body': new MarketingManagementService.Carmodelinfo() // Carmodelinfo | Adds a car model
};
apiInstance.addCarModel(opts, (error, data, response) => {
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
 **body** | [**Carmodelinfo**](Carmodelinfo.md)| Adds a car model | [optional] 

### Return type

[**Model201CarModelCreatedResponse**](Model201CarModelCreatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="getCarModels"></a>
# **getCarModels**
> Carmodeldetails getCarModels()



Get details of all car models

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.CarModelsApi();
apiInstance.getCarModels((error, data, response) => {
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

[**Carmodeldetails**](Carmodeldetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getCarModeltype"></a>
# **getCarModeltype**
> Carmodeldetails getCarModeltype(modelType)



Get details of all car models

### Example
```javascript
import {MarketingManagementService} from 'marketing_management_service';

let apiInstance = new MarketingManagementService.CarModelsApi();
let modelType = "modelType_example"; // String | 

apiInstance.getCarModeltype(modelType, (error, data, response) => {
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
 **modelType** | **String**|  | 

### Return type

[**Carmodeldetails**](Carmodeldetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

