import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250))
    favorites = Column(Integer, ForeignKey('likes.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    followers = relationship('Followers')
    comments = relationship('Comments')
    posts = relationship('Posts')
    users = relationship('User')

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    instagram_handle = Column(String(1))
    following = Column(String(250), nullable=True)
    favorites = Column(Integer, ForeignKey('likes.id'))

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    who_wrote_comment = Column(String(250))
    likes_of_comment = Column(String(250))
    likes = Column(Integer, ForeignKey('likes.id'))
    

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comments = Column(String(250))
    likes = Column(Integer, ForeignKey('likes.id'))

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
