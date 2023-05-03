from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World</h1>"

@app.route('/second')
def second():
    return "<h2>This is the second page</h2>"

@app.route('/third/subthird')
def third():
    return "<h3>This is the subpage of the third page</h3>"

@app.route('/page/<int:page_id>')
def dynamic_page(page_id):
    return f"This is page {page_id}"

if __name__ == '__main__':
    app.run(debug=False)
