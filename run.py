import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

env = os.getenv('ENVIRONMENT', 'development')
port = int(os.getenv('PORT', 5001))

if __name__ == '__main__':
  uvicorn.run('app.main:app', host='127.0.0.1', port=port, reload=(env == 'development'))