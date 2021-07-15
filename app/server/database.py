import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config


MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.peoplelist

customers_collection = database.get_collection("customers_collection")
employees_collection = database.get_collection("employees_collection")
stores_collection = database.get_collection("stores_collection")


# helpers


def customer_helper(customer) -> dict:
    return {
        "id": str(customer["_id"]),
        "name": customer["name"],
        "surname": customer["surname"],
        "loyalty_id": customer["loyalty_id"],
        "address": customer["address"],
        "phone": customer["phone"],
        "email": customer["email"]
    }


def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "surname": employee["surname"],
        "address": employee["address"],
        "phone": employee["phone"],
        "email": employee["email"],
        "dateHired": employee["dateHired"],
        "role": employee["role"]
    }


def store_helper(store) -> dict:
    return {
        "id": str(store["_id"]),
        "storeName": store["storeName"],
        "address": store["address"]
    }


# Retrieve all registries present in the database
async def retrieve_customers():
    customers = []
    async for customer in customers_collection.find():
        customers.append(customer_helper(customer))
    return customers


async def retrieve_employees():
    employees = []
    async for employee in employees_collection.find():
        employees.append(employee_helper(employee))
    return employees


async def retrieve_stores():
    stores = []
    async for store in stores_collection.find():
        stores.append(store_helper(store))
    return stores


# Add a new registry into to the database
async def add_customer(customer_data: dict) -> dict:
    customer = await customers_collection.insert_one(customer_data)
    new_customer = await customers_collection.find_one({"_id": customer.inserted_id})
    return customer_helper(new_customer)


async def add_employee(employee_data: dict) -> dict:
    employee = await employees_collection.insert_one(employee_data)
    new_employee = await employees_collection.find_one({"_id": employee.inserted_id})
    return employee_helper(new_employee)


async def add_store(store_data: dict) -> dict:
    store = await stores_collection.insert_one(store_data)
    new_store = await stores_collection.find_one({"_id": store.inserted_id})
    return store_helper(new_store)


# Retrieve a registry with a matching ID
async def retrieve_customer(id: str) -> dict:
    customer = await customers_collection.find_one({"_id": ObjectId(id)})
    if customer:
        return customer_helper(customer)


async def retrieve_employee(id: str) -> dict:
    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    if employee:
        return employee_helper(employee)


async def retrieve_store(id: str) -> dict:
    store = await stores_collection.find_one({"_id": ObjectId(id)})
    if store:
        return store_helper(store)


# Update a registry with a matching ID
async def update_customer(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    customer = await customers_collection.find_one({"_id": ObjectId(id)})
    if customer:
        updated_customer = await customers_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_customer:
            return True
        return False


async def update_employee(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    if employee:
        updated_employee = await employee.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_employee:
            return True
        return False


async def update_store(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    store = await stores_collection.find_one({"_id": ObjectId(id)})
    if store:
        updated_store = await stores_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_store:
            return True
        return False


# Delete a registry from the database
async def delete_customer(id: str):
    customer = await customers_collection.find_one({"_id": ObjectId(id)})
    if customer:
        await customers_collection.delete_one({"_id": ObjectId(id)})
        return True


async def delete_employee(id: str):
    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    if employee:
        await employees_collection.delete_one({"_id": ObjectId(id)})
        return True


async def delete_store(id: str):
    store = await stores_collection.find_one({"_id": ObjectId(id)})
    if store:
        await stores_collection.delete_one({"_id": ObjectId(id)})
        return True
