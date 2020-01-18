from flask import Flask, render_template, request
import re
import lxml
import sqlite3 as sql
import time

app = Flask(__name__)

