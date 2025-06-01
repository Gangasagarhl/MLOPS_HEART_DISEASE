from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus


# Escape username and password
username = quote_plus("sagar")
password = quote_plus("gatE2024@1")

# Properly formatted MongoDB URI
uri = f"mongodb+srv://{username}:{password}@heartdisaese.cmsksm5.mongodb.net/?retryWrites=true&w=majority&appName=heartdisaese"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Failed to connect:", e)
