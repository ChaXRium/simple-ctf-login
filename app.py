from flask import Flask, request

app = Flask(__name__)

flag = "CTF{you_bypassed_the_login!}"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            return f"<h2>Welcome, admin!</h2><p>The flag is: {flag}</p>"
        else:
            return "<p>Login failed</p>"

    return '''
        <h2>Login</h2>
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)  # For Replit compatibility
