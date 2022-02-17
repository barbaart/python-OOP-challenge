from flask import Flask
import commands

app = Flask(__name__)

commands.register_commands(app)

if __name__ == '__main__':
    app.run()