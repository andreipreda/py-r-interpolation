from app import create_app
from config import Config

dev_app = create_app(config=Config)
dev_app.run(host='localhost', port=7000)