#!d:/__MyDocuments/installations/Miniconda3-x86_64/envs/webserver/python.exe

from wsgiref.handlers import CGIHandler
from application import app

CGIHandler().run(app)

