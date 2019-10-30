from flask import *
import pymongo

app = Flask(__name__)
app.secret_key = b'JPtUKpetQiyfzGpBS5SM'


class MongoDB:

    def __init__(self, ):
        self.client = pymongo.MongoClient("mongodb://18.191.242.107:27017/?replicaSet=rs0")

        self.db = self.client['chat4love']
        self.messages = self.db['messages']
        self.users = self.db['users']

    # Message functions
    def get_messages(self):
        """Retrieves the messages from a chatroom."""
        results = self.messages.find({}, limit=50)
        return results

    def new_message(self, author, content):
        """Adds a message to the database."""
        message = {
            'user': author,
            'content': content
        }
        self.messages.insert_one(message)


db = MongoDB() # access mongodb replica set


@app.route('/')
def index():
    """
    Show chat page if logged in. Otherwise show login page.
    """
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template('chat4love.html', username=session['username'],)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']

        session['username'] = username
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/send-message/', methods=['GET'])
def send_message():
    author = session['username']
    content = request.args.get('msg', '')

    db.new_message(author, content)
    messages = db.get_messages()
    return render_template('messages.html', messages=messages)


@app.route('/get-messages/', methods=['GET'])  # Returns all the messages in a room
def get_messages():
    messages = db.get_messages()
    return render_template('messages.html', messages=messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


