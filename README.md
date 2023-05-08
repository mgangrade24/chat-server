
# Chat Server in Python

A simple Flask-based chat server that supports sending messages from one user to another and getting all unread messages for a specific user.


## Installation

1. Install Python 3.6 or higher.

2. Install the required packages using pip:

```bash
pip install Flask
```
## Running The Application

Run the chat server using the following command:

```bash
  python3 chat_server.py
```
The server will start on http://127.0.0.1:5000/.

## API Explanation

The Flask chat server provides two API endpoints to facilitate communication between users.

### 1. Send Message API

The Send Message API enables one user to send a message to another user. This API accepts a JSON payload with the following properties:

- `from_user`: The username of the sender.
- `to_user`: The username of the recipient.
- `message`: The content of the message.

When the chat server receives a request, it checks the payload's validity and saves the message internally, marking it as unread. If the request is successful, the server responds with a 200 status code and a JSON object containing the message status.

### 2. Get Unread Messages API

The Get Unread Messages API allows a user to retrieve all their unread messages. This API accepts a URL parameter `user`, which is the username of the user requesting their unread messages.

When the chat server receives a request, it retrieves all the unread messages for the specified user and marks them as read. The server then responds with a 200 status code and a JSON array containing the unread messages, each with the following properties:

- `from_user`: The username of the sender.
- `message`: The content of the message.
- `read`: A boolean value indicating whether the message has been read (always `true` in the response since the server marks them as read).
## API Endpoints

### 1. Send Message

Send a message from one user to another.

- **URL:** `/send`
- **Method:** `POST`
- **Content-Type:** `application/json`
- **Request Body:**

```json
{
  "from_user": "user_1",
  "to_user": "user_2",
  "message": "Hello, user_2!"
}
```
- **Success Response:**

  - **Code:** 200
  - **Content:**
```json
  {
    "status": "Message sent"
  }
```
- **Error Response:**

  - **Code:** 400
  - **Content:**
```json
  {
    "error": "Invalid request"
  }
  ```

### 2. Get Unread Messages

Get all unread messages for a specific user.

- **URL:** `/messages`
- **Method:** `GET`
- **URL Params:**

  `user=[username]`

- **Success Response:**

  - **Code:** 200
  - **Content:**

```json
  [
    {
      "from_user": "user_1",
      "message": "Hello, user_2!",
      "read": true
    }
  ]
```
- **Error Response:**

  - **Code:** 400
  - **Content:**
```json
  {
    "error": "Invalid request"
  }
```
## Testing with Postman

### 1. Test the Send Message API:

1. Open Postman.
2. Click the "+" button to create a new request tab.
3. Set the request method to "POST" using the dropdown menu.
4. Enter the URL: `http://127.0.0.1:5000/send`
5. Click the "Headers" tab below the URL.
6. Add a new key-value pair in the headers. Set the key to `Content-Type` and the value to `application/json`.
7. Click the "Body" tab, choose "raw", and set the format to "JSON".
8. Enter the JSON payload:
```json
{
  "from_user": "user_1",
  "to_user": "user_2",
  "message": "Hello, user_2!"
}
```
9. Click the "Send" button. You should receive a response with the status "Message sent" and a 200 status code.

### 2. Test the Get Unread Messages API:

1. Open Postman.
2. Click the "+" button to create a new request tab.
3. Set the request method to "GET" using the dropdown menu.
4. Enter the URL: `http://127.0.0.1:5000/messages?user=user_2`
5. Click the "Send" button. You should receive a response with a list of unread messages for "user_2" and a 200 status code. The response should look like this:
```json
[
  {
    "from_user": "user_1",
    "message": "Hello, user_2!",
    "read": true
  }
]
```
## Unit Test
### Testing the Application with test_chat_server.py

`test_chat_server.py` contains unit tests for the chat server APIs. To run the tests, make sure your chat server is running, and then execute the following command in your terminal:

```bash
python test_chat_server.py
```

The test script contains two test cases:

### 1. Test Send Message API:

This test case sends a POST request to the `/send` endpoint with a JSON payload containing `from_user`, `to_user`, and `message`. The test verifies that the server returns a 200 status code and the expected response indicating that the message was sent successfully.

### 2. Test Get Unread Messages API:

This test case sends a GET request to the `/messages` endpoint with the `user` parameter set to a valid username. The test verifies that the server returns a 200 status code and the expected list of unread messages for the specified user.
