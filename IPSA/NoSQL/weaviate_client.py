import os
import weaviate
from weaviate.classes.init import Auth

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Best practice: store your credentials in environment variables
weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")

# Connect to Weaviate Cloud (test)
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_api_key),
    )

    print(client.is_ready())
    client.close()
except Exception as e:
    print("Error connecting to Weaviate Cloud:", e)
