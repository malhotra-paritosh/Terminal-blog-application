from menu import Menu

__author__ = 'paritosh'

from models.post import Post
from database import Database
from models.blog import Blog

Database.initialize()

menu = Menu()

menu.run_menu()