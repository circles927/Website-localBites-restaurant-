from flask import Flask, render_template
from flask_talisman import Talisman
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

# Allow specific CDN hosts for scripts/styles/fonts/images.
# Adjust hosts to match the exact CDNs you use (code.jquery.com, cdn.jsdelivr.net, cdnjs.cloudflare.com, etc.)
csp = {
    "default-src": ["'self'"],
    "script-src": [
        "'self'",
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    ],
    "style-src": [
        "'self'",
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    ]
}

Talisman(app, force_https=False, content_security_policy=csp, content_security_policy_nonce_in=['script-src'])
Bootstrap5(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/index.html", methods=["GET"])
def index2():
    return render_template("index.html")

@app.route("/contact.html", methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route("/about.html", methods=["GET"])
def about():
    return render_template("about.html")
