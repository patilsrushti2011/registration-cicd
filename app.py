
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not email:
            message = "Please enter your name and email."
        else:
            message = f"Thank you for registering, {name}!"

    return render_template("register.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
