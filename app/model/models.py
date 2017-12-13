from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
    weixin = db.Column(db.String, unique=True)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    

    def __init_(self, id, public_id, name, password, admin, weixin):
        self.id = id
        self.public_id = public_id
        self.name = name
        self.password = password
        self.admin = admin
        self.weixin = weixin

    def __repr__(self):
        return '<id {}'.format(self.id)

class News(db.Model):
    
    __tablename__ = "news"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    public_id = db.Column(db.String(50), unique=True)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    update_by = relationship("user", backref="name")
    update_by = db.Column(db.String(50), nullable=False)
    # release_time = db.Column(db.DateTime, nullable=False)
    views = db.Column(db.Integer)
    body = db.Column(db.Text)
    summary = db.Column(db.String(150), nullable=False)
    is_hot = db.Column(db.Boolean)
    is_del = db.Column(db.Boolean)
    news_type = db.Column(db.String(20))
    news_keys = db.Column(db.String(80))
    thumb = db.Column(db.String(80))

    def __init_(self, id, title, public_id, create_time, update_time, update_by, release_time, views, body, summary, is_hot, is_del, news_type, news_keys, thumb):
        self.id = id
        self.title = title
        self.public_id = public_id
        self.create_time = create_time
        self.update_time = update_time
        self.update_by = update_by
        self.release_time = release_time
        self.views = views
        self.body = body
        self.summary = summary
        self.is_hot = is_hot
        self.is_del = is_del
        self.news_type = news_type
        self.news_keys = news_keys
        self.thumb = thumb

    def __repr__(self):
        return '<id {}'.format(self.id)