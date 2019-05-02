from waitress import serve
from app import create_app
from config import ProdConfig
from paste.translogger import TransLogger

app = create_app(config=ProdConfig)
app_with_logs = TransLogger(app, setup_console_handler=False)
serve(app_with_logs, host='0.0.0.0', port='7000')
