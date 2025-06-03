from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

# Raw credentials
username = "sagar"
password = "gatE2024@1"

# Properly encode the credentials
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

print(encoded_password, encoded_username)
# Now construct the URI using the encoded credentials
uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.ikkbwln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a MongoClient instance
client = MongoClient(uri)

# Try pinging the database
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
