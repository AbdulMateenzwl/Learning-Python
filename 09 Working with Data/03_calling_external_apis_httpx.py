import httpx 

response = httpx.get("https://jsonplaceholder.typicode.com/users/1") 
print(response.status_code) 
print(response.json()["name"])   # Output: Leanne Graham


import asyncio

async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts/1")
        print(response.json()["title"])

asyncio.run(get_data())
print("Data fetched successfully.")
