# purplship.Tracking

All URIs are relative to *https://instance.purplship.api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve**](Tracking.md#retrieve) | **GET** /proxy/tracking/{carrier_name}/{tracking_number} | 


# **retrieve**
> TrackingResponse retrieve(carrier_name, tracking_number, test=test)



 You can track a shipment by specifying the carrier and the shipment tracking number. 

### Example
```python
from __future__ import print_function
import time
import purplship
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
purplship.api_key = 'YOUR_API_KEY'
purplship.host = 'https://instance.purplship.api/v1'

try:
    api_response = purplship.Tracking.retrieve(
        carrier_name='carrier_name_example',
        tracking_number='tracking_number_example',
        test=false
    )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Tracking->retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_name** | **str**|  | 
 **tracking_number** | **str**|  | 
 **test** | **bool**|  The test flag indicates whether to use a carrier configured for test.   | [optional] [default to false]

### Return type

[**TrackingResponse**](TrackingResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
