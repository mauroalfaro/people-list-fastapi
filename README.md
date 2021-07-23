# people-list-fastapi
Basic REST Api with CRUD operations made with FastAPI

## Description
people-list project developed with Python and FastAPI. Contains CRUD operations impacting a MongoDB database running on the cloud on a Mongo Atlas cluster.

## Design
Basic Python/FatsAPI application with CRUD endpoints for three models: Customers, Employees and Stores.
Includes:
- Python/FastAPI
- Uvicorn Server
- Pydantic Schemas
- Pydantic validators (Email)
- MongoDB asynchronous interaction
- Deployed on the cloud with MongoDB Atlas / Heroku
- FastAPI UI to test the app

## Using the app
The application is deployed on Heroku and is available to test via this link: https://cryptic-shelf-56391.herokuapp.com/docs#

If you want to test and deploy the app locally, you should clone this repository, create a virtual environment with venv and install the requirements:
```bash
pip install -r requirements.txt
```

Then, after sourcing your venv environment, you can run the app by executing:
```bash
python app/main.py
```

You should start your local MongoDB and set the db name to peoplelist. Then creating a .env file with a mongo_details variable and the url to be resolved by Motor:

MONGO_DETAILS=your_mongodb_url

You can access to the FastAPI UI on the URL http://localhost:8000/docs#/

## Notes
- Refer to [this](https://docs.mongodb.com/manual/installation/) link if you don't know how to install/run MongoDB locally
- You can swap out virtualenv and Pip for Poetry or Pipenv.
- If you dont know how to create and source your virtual environment, the commands are the following:
```bash
python3.8 -m venv venv
source venv/bin/activate
```

