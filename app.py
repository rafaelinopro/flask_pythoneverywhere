from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

# Route for the GitHub webhook

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./flask_pythoneverywhere')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route('/', methods=['GET'])
def home():
    return "<h1>Mamá mi primera aplicación</h1><p>This site is a prototype API for distant reading of science fiction novels WTFFFFFFFF!!!!.</p>"


if __name__ == '__main__':
    app.run()
