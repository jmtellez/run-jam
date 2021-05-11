import billboard
from flask import Flask

app = Flask(__name__)

chart = billboard.ChartData('hot-100')

@app.route('/')
def index():
    return "run-jam"

@app.route('/hot-100')
def return_hot_100():
    return chart[0].title

def main():
    for song in chart:
        print(song.title)

if __name__=="__main__":
    main() 
    app.run(debug=True)