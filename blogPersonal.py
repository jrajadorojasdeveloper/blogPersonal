from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
posts = []

@app.route('/')
def index():
    return render_template('post.html', posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = posts[post_id]
    return render_template('show_post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
