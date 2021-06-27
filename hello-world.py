import os
import pandas as pd
import pinecone

os.environ["PINECONE_API_KEY"] = "YOUR_API_KEY"

# load Pinecone API key
api_key = os.getenv("PINECONE_API_KEY")
pinecone.init(api_key=api_key)

# List indexes
ind_list = pinecone.list_indexes()

# Create an index
if "hello-pinecone-index" not in ind_list:
    pinecone.create_index("hello-pinecone-index", metric="euclidean")

# Connect to the index
index = pinecone.Index("hello-pinecone-index")

# Generate some data
df = pd.DataFrame(data={
    "id": ["A", "B", "C", "D", "E"],
    "vector": [[1]*2, [2]*2, [3]*2, [4]*2, [5]*2]
})

# Insert the data
index.upsert(items=zip(df.id, df.vector))

# Get index info
information = index.info()
print(f"Elements found on index: {information.index_size}")

# Query the index and get similar vectors
result = index.query(queries=[[0, 1]], top_k=3)
print(result)

# Delete the index
pinecone.delete_index("hello-pinecone-index")