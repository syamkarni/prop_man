import httpx
import asyncio

BASE_URL = "http://127.0.0.1:8000"

async def insert_sample_data():
    async with httpx.AsyncClient() as client:
        sample_data = [
            { "name": "Property 1", "addr": "123 Main St", "city": "City A", "state": "State A" },
            { "name": "Property 2", "addr": "456 Main St", "city": "City A", "state": "State A" },
            { "name": "Property 3", "addr": "789 Main St", "city": "City B", "state": "State B" },
            { "name": "Property 4", "addr": "101 Main St", "city": "City C", "state": "State C" },
            { "name": "Property 5", "addr": "102 Main St", "city": "City C", "state": "State C" },
            { "name": "Property 6", "addr": "103 Main St", "city": "City D", "state": "State D" },
            { "name": "Property 7", "addr": "104 Main St", "city": "City D", "state": "State D" },
            { "name": "Property 8", "addr": "105 Main St", "city": "City E", "state": "State E" },
            { "name": "Property 9", "addr": "106 Main St", "city": "City F", "state": "State F" },
            { "name": "Property 10", "addr": "107 Main St", "city": "City G", "state": "State G" }
        ]

        for property in sample_data:
            response = await client.post(f"{BASE_URL}/props", json=property)
            print(f"Inserted {property['name']}: {response.status_code}")

        # Verify the data
        response = await client.get(f"{BASE_URL}/props/City A")
        print(f"Properties in City A: {response.json()}")

        response = await client.get(f"{BASE_URL}/props/City C")
        print(f"Properties in City C: {response.json()}")

        response = await client.get(f"{BASE_URL}/props/City G")
        print(f"Properties in City G: {response.json()}")

asyncio.run(insert_sample_data())
