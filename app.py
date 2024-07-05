from ext import app

if __name__ == "__main__":
    from routes import index, register, login, product
    app.run(debug=True)
