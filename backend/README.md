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
  "errorMsg": "Failed search sample"
}
```

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
    "errorMsg": "Failed view the logbook"
}
```

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

___


## Check the current status

### Send

- URL: /check
- HTTP Method: POST
- Body: 

```json
{
  "sample_type": "blood",
  "sample_ID": "blo001",
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
  "Data":
  {
    "type": "blood",
    "id": "blo001",
    "Qnow": "18",
    "Qnow_unit": "ml",
    "loc": "freezer001",
    "status": "available",
    "latest_custodian": "peter"
  }
}
```

**Fail**

- HTTP Status Code: 400
- Body:

```json
{
  "errorMsg": "Failed check status"
}
```

