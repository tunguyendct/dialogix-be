# Dialogix - AI Chat Agent

A FastAPI-based backend for an AI chat agent using Azure OpenAI.

## Project Structure

```
dialogix-be/
│
├── app/
│   ├── main.py              # FastAPI app entrypoint
│   ├── config.py            # Environment config (dev/prod keys)
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── chat.py      # Chat endpoints
│   │   │   ├── message.py   # Message endpoints
│   │   │   ├── user.py      # User endpoints
│   │   │   └── auth.py      # Authentication endpoints
│   │   └── deps.py          # Auth/session dependencies
│   ├── core/
│   │   ├── openapi_client.py # Handles Azure OpenAI API calls
│   │   └── utils.py         # Utility functions
│   ├── models/
│   │   ├── base.py          # Base models
│   │   ├── chat.py          # Chat models
│   │   ├── message.py       # Message models
│   │   └── user.py          # User models
│   └── services/
│       ├── chat.py          # Chat service
│       ├── message.py       # Message service with AI integration
│       └── user.py          # User service
│
├── database/
│   ├── mongo.py             # MongoDB client
│   └── schemas.py           # DB schemas
│
├── .env                     # Environment variables
├── requirements.txt         # Project dependencies
└── run.py                   # Uvicorn server start
```

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with the following variables:

```
# MongoDB Configuration
MONGO_URL=your_mongodb_connection_string
DATABASE_NAME=dialogix
USER_COLLECTION=users
CHAT_COLLECTION=chats
MESSAGE_COLLECTION=messages

# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-05-15
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name

# Model Settings (optional)
DEFAULT_MAX_TOKENS=1000
DEFAULT_TEMPERATURE=0.7
```

6. Run the application: `python run.py`

## API Endpoints

- **Authentication**
  - POST `/api/v1/auth/login`: User login
  - POST `/api/v1/auth/register`: User registration

- **Users**
  - GET `/api/v1/users`: List all users
  - GET `/api/v1/users/{id}`: Get user by ID
  - POST `/api/v1/users`: Create a new user

- **Chats**
  - GET `/api/v1/chats`: List all chats
  - GET `/api/v1/chats/user/{user_id}`: List chats by user
  - GET `/api/v1/chats/{id}`: Get chat by ID
  - POST `/api/v1/chats`: Create a new chat

- **Messages**
  - GET `/api/v1/messages`: List all messages
  - GET `/api/v1/messages/chat/{chat_id}`: List messages by chat
  - GET `/api/v1/messages/{id}`: Get message by ID
  - POST `/api/v1/messages`: Create a new message (automatically generates AI response for user messages)

## Azure OpenAI Integration

This project uses Azure OpenAI for generating AI responses. When a user sends a message, the system:

1. Saves the user message
2. Retrieves the conversation history
3. Formats the messages for the Azure OpenAI API
4. Generates an AI response using the Azure OpenAI service
5. Saves the AI response as a new message

The Azure OpenAI client is implemented in `app/core/openapi_client.py` and is used by the message service in `app/services/message.py`.
