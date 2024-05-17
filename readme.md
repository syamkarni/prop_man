
# Property Management API

This is a Property Management API built with FastAPI and MongoDB. It allows you to create, retrieve, update, and delete property records.

## API Endpoints

### 1. Create New Property

- **Endpoint:** `/props`
- **Method:** `POST`
- **Input:**
  ```json
  {
      "name": "Property Name",
      "addr": "Property Address",
      "city": "Property City",
      "state": "Property State"
  }
  ```
- **Output:**
  - Returns a list of properties with all details.

### 2. Fetch Property Details

- **Endpoint:** `/props/{city}`
- **Method:** `GET`
- **Input:**
  - `city` (string): Name of the city.
- **Output:**
  - Returns a list of all properties that belong to the specified city.
  
### 3. Update Property Details

- **Endpoint:** `/props/{property_id}`
- **Method:** `PUT`
- **Input:**
  ```json
  {
      "name": "Updated Property Name",
      "addr": "Updated Property Address",
      "city": "Updated Property City",
      "state": "Updated Property State"
  }
  ```
  - `property_id` (string): ID of the property to update.
- **Output:**
  - Returns a list of properties with updated information.
  
### 4. Find Cities by State

- **Endpoint:** `/cities/{state}`
- **Method:** `GET`
- **Input:**
  - `state` (string): Name of the state.
- **Output:**
  - Returns a list of all city names that belong to the specified state.

### 5. Find Similar Properties

- **Endpoint:** `/props/sim/{property_id}`
- **Method:** `GET`
- **Input:**
  - `property_id` (string): ID of the property.
- **Output:**
  - Returns a list of all properties that belong to the same city as the specified property.

## Running the Application

To run the application, ensure you have all dependencies installed and then start the FastAPI server.

```sh
python3 app/main.py
```

## Testing the Application

You can use tools like `httpx`, `curl`, or Postman to test the API endpoints.

### Example using `curl`

**Create New Property:**

```sh
curl -X POST "http://127.0.0.1:8000/props" -H "Content-Type: application/json" -d '{"name": "Property 1", "addr": "123 Main St", "city": "City A", "state": "State A"}'
```

**Fetch Property Details:**

```sh
curl "http://127.0.0.1:8000/props/City A"
```

**Update Property Details:**

```sh
curl -X PUT "http://127.0.0.1:8000/props/{property_id}" -H "Content-Type: application/json" -d '{"name": "Updated Property", "addr": "123 Updated St", "city": "Updated City", "state": "Updated State"}'
```

**Find Cities by State:**

```sh
curl "http://127.0.0.1:8000/cities/State A"
```

**Find Similar Properties:**

```sh
curl "http://127.0.0.1:8000/props/sim/{property_id}"
```

Replace `{property_id}` with the actual ID of the property.

## Dependencies

- FastAPI
- uvicorn
- httpx
- pymongo

Ensure you have all the required dependencies installed. You can install them using:

```sh
pip install -r requirements.txt