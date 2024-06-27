
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
  items = ['Item 1', 'Item 2', 'Item 3']
  return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
  item_name = request.form['item_name']
  items.append(item_name)
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)
