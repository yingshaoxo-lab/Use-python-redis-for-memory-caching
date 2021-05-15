import redis
from flask import Flask

# make redis
redis_cache = redis.Redis(host='localhost', port=6379, db=0, password="redis_password")

# make flask app
app = Flask(__name__)


@app.route('/set/<string:key>/<string:value>')
def set(key, value):
    if redis_cache.exists(key):
        pass
    else:
        redis_cache.set(key, value)
    return "OK"


@app.route('/get/<string:key>')
def get(key):
    if redis_cache.exists(key):
        return redis_cache.get(key)
    else:
        return f"{key} is not exists"


app.run("127.0.0.1", port="9111", debug=True)
