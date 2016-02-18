import datetime as dt

from Ultimate_Machine.extensions import db
from Ultimate_Machine.models.relationships import tags_posts
from Ultimate_Machine.database import (
    Column,
    Model,
    SurrogatePK,
)


class Post(SurrogatePK, Model):

    __tablename__ = 'posts'

    title = db.Column(db.Text)
    slug = db.Column(db.Text)
    body = db.Column(db.Text)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tags = db.relationship('Tag', secondary=tags_posts, backref=db.backref('posts_br', lazy='dynamic'))

    def __init__(self, title, slug, body, **kwargs):
        db.Model.__init__(self, title=title, slug=slug, body=body, **kwargs)