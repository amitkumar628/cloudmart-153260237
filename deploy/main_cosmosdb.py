from azure.cosmos import CosmosClient
endpoint = "https://cloudmartdb153260237.documents.azure.com:443/"
key = "m1yCS6p4AINxAQm25e6bRAy1ssrJ1ZrkxEJ4q6OFMfSZ1JLXRk0SltK62iA54Mxqo0YcuBMH7hDEACDbOQGSyA=="

client = CosmosClient(endpoint, key)

print("Connected to Cosmos DB")
