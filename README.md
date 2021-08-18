# LIMS

- A [Frontend](https://github.com/Liwen-Zha/LIMS-database-system/tree/master/frontend/) using [React](https://reactjs.org/) and [Bootstrap](https://getbootstrap.com/)
- A [Backend](https://github.com/Liwen-Zha/LIMS-database-system/tree/master/backend/) using [Flask](https://flask.palletsprojects.com/en/2.0.x//)

___

## Implementation

- The top layer is [frontend](./frontend), which utilises the [APIs](./backend/main/__init__.py) provided by [Flask RESTful APIs](https://pypi.org/project/flask-rest-api/). When implementing [frontend](./frontend), we can assume that all the [APIs](./docs) have already been implemented.
- The middle layer is [backend](./backend), which utilises the differnt functions to manipulate data stored in the graph database [NEO4j](https://neo4j.com).
- The bottom layer is [database](./backend/graph_database), which utilises graph database [NEO4j](https://neo4j.com/) to record all the sample transactions and information. 
- A single version of the fronend is [tkinter app](./tk_frontend.py), which utilises the tkinter module in Python to build a simple program of the LIMS. 

## Run exsiting Frontend

### Setup Server
```shell
npm install
```
### Run Server

```shell 
npm start
```
### Install new-package

```shell
npm install --save new-package
```
___

## Start LIMS (fullstack)

### Run frontend

```shell 
npm run build
```

### Connect to backend

```shell 
hello.py
```

