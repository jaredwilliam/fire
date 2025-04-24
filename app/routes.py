# Defines the routes and views for the web application
from flask import Blueprint, render_template, request, redirect, url_for

main_routes = Blueprint("main", __name__)


@main_routes.route("/")
def index():
    return render_template("index.html")


@main_routes.route("/calculate", methods=["POST"])
def calculate():
    current_age = request.form.get("current_age")
    retirement_age = request.form.get("retirement_age")
    current_savings = request.form.get("current_savings")

    # Placeholder
    results = {
        "message": "Calculation Successful",
        "current_age": current_age,
        "retirement_age": retirement_age,
        "current_savings": current_savings,
    }

    return render_template("results.html", results=results)
