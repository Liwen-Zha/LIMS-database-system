# API Documentation

- Author: Liwen Zha
- Date: Aug. 2021

## Overview

| **Action**                  | **HTTP Method** | **URL**        | **curl**                                                                                                                                                                                          |
| --------------------------- | --------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Log sample transaction      | POST            | /log           | curl -v --header "Content-Type: application/json" --request POST --data '{"sample_type":"","sample_ID":"","loc":"","status":"","Q":"","unit":"","custodian":""}' http://127.0.0.1:5000/log        |
| Search sample records       | POST            | /search        | curl -v --header "Content-Type: application/json" --request POST --data '{"sample_type":"","sample_ID":"","loc":"","status":"","Q":"","unit":"","custodian":""}' http://127.0.0.1:5000/search     |
| View all sample records     | GET             | /view-logs     | curl -v --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/view-logs                                                                                                   |
| View all samples            | GET             | /view-samples  | curl -v --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/view-samples                                                                                                |
| Check the current status    | POST            | /check         | curl -v --header "Content-Type: application/json" --request POST --data '{"sample_type":"","sample_ID":"","loc":"","status":"","Q":"","unit":"","custodian":""}' http://127.0.0.1:5000/check      |


___

## Log sample transaction

### Send

- URL: /log
- HTTP Method: POST
- Body: 

```json
{
  "sample_type": "blood",
  "sample_ID": "blo001",
  "loc": "freezer001",
  "status": "available",
  "Q": "10",
  "unit": "ml",
  "custodian": "peter"
}
```

### Response

**Succeed**

- HTTP Status Code: 200
- Body:

```json
{
  "Status": "200 OK",
  "Method": "POST",
  "Data":
  {
    "type": "blood",
    "id": "blo001",
    "loc": "freezer001",
    "status": "available",
    "Qvar": "10",
    "Qvar_unit": "ml",
    "custodian": "peter"
  }
}
```

**Fail**

- HTTP Status Code: 400
- Body:

```json
{
  "errorMsg": "Failed add sample"
}
```

#### Comments:
For /log, all the variables being sent to the web server are supposed not to be empty fields, as the sample registration 
should always include all aspects of the transaction details. However, they can be empty fields. That is because the 
backend function (insert()) called via the API (/log) has a built-in logic to alert users when they input empty fields.
In other words, instead of rejecting empty fields, insert() accepts empty fields and responds to them with a reminder.


___

## Search sample records

### Send

- URL: /search
- HTTP Method: POST
- Body:

```json
{
  "sample_type": "blood",
  "sample_ID": "blo001",
  "loc": "freezer001",
  "status": "",
  "Q": "",
  "unit": "",
  "custodian": "peter"
}
```

### Response

**Succeed**

- HTTP Status Code: 200
- Body:

```json
{
  "Status": "200 OK", 
  "Method": "POST",
  "Data":[
    {
      "custodian": "peter",
      "id": "blo001",
      "loc": "freezer001",
      "Qvar": "10",
      "Qvar_unit": "ml",
      "Qnow": "18",
      "Qnow_unit": "ml",
      "time": "27/07/2021 - 00:49:05"
    },
    {
      "custodian": "peter",
      "id": "blo001",
      "loc": "freezer001",
      "Qvar": "5",
      "Qvar_unit": "ml",
      "Qnow": "8",
      "Qnow_unit": "ml",
      "time": "27/07/2021 - 00:30:19"
    }
  ]
}
```

**Fail**

- HTTP Status Code: 400
- Body:

```json
{
  "errorMsg": "Fail to search the log(s)!"
}
```

#### Comments:
For /search, all the variables being sent to the web server can be empty fields or not. The reason why the empty fields 
are allowed here is to consider the situation that users sometimes may just want to search a group of data records with same
attributes. The above case is such an instance, where the user only wanted to find the data records related to blood blo001 in freezer001
that was specifically operated by peter. Therefore, when other people such as helen operated blo001, or when blo001 was
moved and stored in freezer002, the related data records would not be searched and considered. The API (/search) calls the function
(search()) in backend to operate the user inputs. If some of the variables are empty fields, the backend function (search()) will ignore 
them and only read values of the variables that are not empty fields, then according to the reading values it can do the corresponding data
matching in the backend database. If there are no matching records, it will show the error message "Fail to search the log(s)!".


___

## View all sample records

### Send

- URL: /view-logs
- HTTP Method: GET
- Body: NULL


### Response

**Succeed**

- HTTP Status Code: 200
- Body:

```json
{
  "Status": "200 OK", 
  "Method": "POST",
  "Data":[
    {
      "custodian": "peter",
      "id": "blo001",
      "loc": "freezer001",
      "Qvar": "10",
      "Qvar_unit": "ml",
      "Qnow": "18",
      "Qnow_unit": "ml",
      "time": "27/07/2021 - 00:49:05"
    },
    {
      "custodian": "peter",
      "id": "blo001",
      "loc": "freezer001",
      "Qvar": "5",
      "Qvar_unit": "ml",
      "Qnow": "8",
      "Qnow_unit": "ml",
      "time": "27/07/2021 - 00:30:19"
    },
    {
      "custodian": "helen",
      "id": "blo001",
      "loc": "freezer001",
      "Qvar": "3",
      "Qvar_unit": "ml",
      "Qnow": "3",
      "Qnow_unit": "ml",
      "time": "27/07/2021 - 00:10:19"
    }
  ]
}

```

**Fail**

- HTTP Status Code: 400
- Body:

```json
{
    "errorMsg": "Fail to view all logs!"
}
```


####Comments:
For /view-logs, all the sample records/transactions/history logged into the LIMS will be shown in a table format. It is
like a logbook, recording all the sample actions happened in the lab from the past to the future. As the database grows, 
the logbook should always be huge, this function may not be used as often as other functions. But it is useful to keep it 
in the API(/view-logs), acting as a fundamental way of viewing the entire logbook. The 400 code will happen when there is 
not a single record in the database. In other words, it is just right before the LIMS starts to be used in the lab. 

___

## View all samples

### Send

- URL: /view-samples
- HTTP Method: GET
- Body: Null

### Response

**Succeed**

- HTTP Status Code: 200
- Body:

```json
{
  "Status": "200 OK", 
  "Method": "GET",
  "Data":[
    {
      "type": "blood",
      "id": "blo001",
      "Qnow": "18",
      "Qnow_unit": "ml",
      "time": "27/07/2021 - 00:49:05",
      "loc": "freezer001",
      "status": "available",
      "latest_custodian": "peter"
    }
  ]
}

```

**Fail**

- HTTP Status Code: 400
- Body:

```json
{
    "errorMsg": "Failed view all samples"
}
```

####Comments:
For /view-samples, all the samples registered into the LIMS will be shown in a table format. It is like a 
automatically-updated sample catalogue, recording the latest information of all the samples in the lab. Like /view-logs, 
it may not be called very often, but it is useful to keep such a function to have an overview of the lab's sample inventory.
Database contains all the detailed information of the registered sample, including the quantity variation, initial quantity
and the current quantity. But this function aims to show the latest information (current sample status), it will only
provide the information of the current quantity to the users, regardless of the past transactions. 

___


## Check the current status

### Send

- URL: /check
- HTTP Method: POST
- Body: 

```json
{
  "sample_type": "blood",
  "sample_ID": "",
  "loc": "",
  "status": "",
  "custodian": ""
}
```

### Response

**Succeed**

- HTTP Status Code: 200
- Body:

```json
{
  "Status": "200 OK",
  "Method": "POST",
  "Data": [
    {
    "type": "blood",
    "id": "blo001",
    "Qnow": "18",
    "Qnow_unit": "ml",
    "loc": "freezer001",
    "status": "available",
    "latest_custodian": "peter"
  },
    {
    "type": "blood",
    "id": "blo002",
    "Qnow": "11",
    "Qnow_unit": "ml",
    "loc": "freezer002",
    "status": "available",
    "latest_custodian": "helen"
  }
  ]
}
```

**Fail**

- HTTP Status Code: 400
- Body:

```json
{
  "errorMsg": "Fail to check status!"
}
```
#### Comments:
For /check, all the variables being sent to the web server can be empty fields or not, just like /search. 
The reason why the empty fields are allowed here is to consider the situation that users sometimes may just want to check
the sample status in a specific circumstance. For example, check all the samples in a designated freezer, or check 
all the samples supervised by a designated custodian. The above case is such an instance, where the user only wanted to 
check all the blood samples in the lab. In this case, sample_type (blood) was a restricted condition. Only the records of 
blood samples could be matched and checked in the database. The difference of between the check function and the search function
is that the former one only shows the latest information/status of the samples we want to check, while the latter one shows
all the records/transactions/history of the samples we want to search. The API (/check) calls the function (check()) in 
backend to operate the user inputs. If some of the inputs are empty fields, the backend function (check()) will ignore 
them and only read values of the variables that are not empty fields, then according to the reading values it can do the 
corresponding data matching in the backend database. If there are no matching records, it will show the error message 
"Fail to check status!".


