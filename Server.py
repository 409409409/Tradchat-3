from flask import Flask, render_template, render_template_string, redirect
from flask_socketio import SocketIO
import sqlite3
import os

# Check if database files exist and track creation status
databases_created = []

if not os.path.exists("accounts.db"):
    databases_created.append("accounts.db")
if not os.path.exists("rooms_names.db"):
    databases_created.append("rooms_names.db")

# make basic databases
accounts_db = sqlite3.connect("accounts.db")
accounts = accounts_db.cursor()

room_names_db = sqlite3.connect("rooms_names.db")
room_names = room_names_db.cursor()

# Create tables if databases didn't exist
if not accounts_db_exists:
    accounts.execute('''
        CREATE TABLE accounts (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            DOB TEXT NOT NULL
        )
    ''')
    accounts_db.commit()

if not rooms_db_exists:
    room_names.execute('''
        CREATE TABLE rooms (
            roomname TEXT PRIMARY KEY,
            roomtype TEXT NOT NULL,
            invites TEXT
        )
    ''')
    room_names_db.commit()
