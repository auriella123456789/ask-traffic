from flask import Flask, render_template, request
import google.generativeai as palm
import os

api_key = os.getenv("MAKERSUITE_API_TOKEN")
palm.configure(api_key=api_key)

model = {"model": "models/chat-bison-001"}

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    q = (request.form.get("q") 
    print(r)
    return(render_teplate("main.html"))

@app.route("/traffic_thailand", methods=["GET", "POST"])
def traffic_thailand():
    q = "thailand traffic"
    r = palm.chat(**model,messages=q)
    print(r)
    return(render_teplate("traffic_thailand.html", r=r.last))

if_name_== "_main_":
app.run()
