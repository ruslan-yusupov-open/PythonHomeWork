from flask import Flask, request
import os
import random
import datetime

# print(os.environ)

# exit()

if "FLASK_RANDOM_SEED" in os.environ:
    seed = os.environ["FLASK_RANDOM_SEED"]
else:
    print("PLEASE SET FLASK_RANDOM_SEED")
    exit(1)

    random.seed(seed)


class RandomNumber:
    def __init__(self):
        self.rand = random.randint(1, 100)
        self.guess_attempts = 0
        self.start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


rand_num = RandomNumber()

app = Flask(__name__)
app.config['DEBUG'] = True
# app.config['SECRET_KEY'] = os.environ['S']

app.config.update(
    DEBUG=True,
    # SECRET_KEY=os.environ['S'],
)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'Число загадано {}, попыток сделано {}'.format(rand_num.start_time, rand_num.guess_attempts), 200


@app.route('/guess', methods=['GET', 'POST'])
def guessp():
    if "number" in request.form:
        number = int(request.form["number"])
    else:
        return 'post number not set', 400

    if number > rand_num.rand:
        return '<', 200
    if number < rand_num.rand:
        return '>', 200
    if number == rand_num.rand:
        rand_num.__init__()
        return '= загадываем новое', 200


@app.route('/guess/<int:number>', methods=['GET', 'POST'])
def guess(number):
    if number > rand_num.rand:
        return '<', 200
    if number < rand_num.rand:
        return '>', 200
    if number == rand_num.rand:
        rand_num.__init__()
        return '= загадываем новое', 200


if __name__ == '__main__':
    app.run()
