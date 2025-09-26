# Tarea3_PCD
Repository for homework #3 of Data Science Project Course at ITESO. It covers the creation and development of an API using FastAPI.

# Users API 

The API is built for storing user data, such as name, email, age, recommendations and ZIP code. It has a built-in integration with SQLite to store user information.

## 1. Environment and Dependencies

### &ensp; 1.1. Library Installation 

Dependency management is done via uv, which needs to be installed in order to facilitate code execution and library downloads. The file uv.lock contains the specific libraries required to run the project. 

### &ensp; 1.2. Create .env file for Authentication

The API is protected with headers and API Keys. The .env file stores API Keys in order for the API to grant permission for edition. Create a .env file following the structure of .env.example with your desired key.

## 2. API Endpoints

### &ensp; 2.1. Create a user entry

POST `/api/v1/users/`

&ensp; Creates a new user in the database, using the following JSON structure:

```
{
  "user_name": "string",
  "user_email": "string",
  "age": 100,
  "recommendations": [
    "string"
  ],
  "zip": "string"
}
```

&ensp; For example:

```
{
  "user_name": "Kim Dokja",
  "user_email": "kim_dokja@kimcom.com",
  "age": 30,
  "recommendations": [
    "Persephone", "Prisoner of the Golden Headband", "Secretive Plotter", "Demon-like Judge of Fire"
  ],
  "zip": null
}
```

### &ensp; 2.2. Consult a specific user entry

GET `/api/v1/users/{user_id}`

&ensp; Searchs for an user based on an existing user_id and retrieves its corresponding data. 

### &ensp; 2.3. Update a user entry

PUT `/api/v1/users/{user_id}`

&ensp; Updates an user's information based on an existing user_id.

### &ensp; 2.4. Delete a user entry

DELETE `/api/v1/users/{user_id}`

&ensp; Deletes an user entry in the database based on an existing user_id.

## 3. Run the API

Execute in terminal:

`uv init fastapi dev main.py`