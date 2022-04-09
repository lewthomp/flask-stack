import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint("auth", __name__, url_prefix="/auth")
