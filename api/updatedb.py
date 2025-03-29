from flask import Flask
from flask_migrate import Migrate,upgrade
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:difyai123456@192.168.243.130/dify'  # 替换为你的数据库 URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
# 初始化应用
app = create_app()
migrade = Migrate(app, db)
if __name__ == "__main__":
    with app.app_context():
        print("Starting database upgrade...")
        upgrade()
        print("Database upgrade completed.")