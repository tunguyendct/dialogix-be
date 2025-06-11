ai-chat-agent/
│
├── app/
│   ├── main.py              # FastAPI app entrypoint
│   ├── config.py            # Environment config (dev/prod keys)
│   ├── api/
│   │   ├── endpoints/
│   │   │   └── chat.py      # /chat POST endpoint
│   │   └── deps.py          # Auth/session dependencies
│   ├── core/
│   │   ├── openai_client.py # Handles OpenAI API calls
│   │   └── utils.py         # Utility functions
│   ├── models/
│   │   └── chat.py          # Pydantic models
│   └── services/
│       └── chat.py          # Core chat logic
│
├── database/
│   ├── mongo.py             # MongoDB client
│   └── schemas.py           # DB schemas
│
├── .env                     # Environment variables
├── requirements.txt
└── run.py                   # Uvicorn server start
