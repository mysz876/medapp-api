from application import create_app

app = create_app()
ctx = app.app_context()
ctx.push()
ctx.pop()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
