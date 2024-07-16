from flask import Flask

app = Flask(_name_)

@app.route('/home')
def home():
    return """
    <html>
    <head><title>Welcome to My Photo Gallery</title></head>
    <body>
        <h1>Welcome to My Photo Gallery</h1>
        <p>This gallery contains three types of photos: food, pets, and outer space.</p>
    </html>
    """

@app.route('/food1')
def food1():
    return """
    <html>
    <head><title>Food Photo 1</title></head>
    <body>
        <h1>Food Photo 1</h1>
        <img src="" alt="salad" style="width:500px;">
        <p>Here's a photo of delicious food!</p>
        <p><a href="/home">Back to home</a></p>
        <p><a href="/food2">Next food photo</a></p>
    </body>
    </html>
    """

@app.route('/food2')
def food2():
    return """
    <html>
    <head><title>Food Photo 2</title></head>
    <body>
        <h1>Food Photo 2</h1>
        <img src="" alt="salad" style="width:500px;">
        <p>Here's another delicious food photo!</p>
        <p><a href="/home">Back to home</a></p>
        <p><a href="/food3">Next food photo</a></p>
    </body>
    </html>
    """

@app.route('/food3')
def food3():
    return """
    <html>
    <head><title>Food Photo 3</title></head>
    <body>
        <h1>Food Photo 3</h1>
        <img src="" alt="salad" style="width:500px;">
        <p>Here's another tasty food photo!</p>
        <p><a href="/home">Back to home</a></p>
        <p><a href="/pet1">Next pet photo</a></p>
    </body>
    </html>
    """

@app.route('/pet1')
def pet1():
    return """
    <html>
    <head><title>Pet Photo 1</title></head>
    <body>
        <h1>Pet Photo 1</h1>
        <img src="" alt="salad" style="width:500px;">
        <p>Here's a lovely pet photo!</p>
        <p><a href="/home">Back to home</a></p>
        <p><a href="/pet2">Next pet photo</a></p>
    </body>
    </html>
    """

@app.route('/pet2')
def pet2():
    return """
    <html>
    <head><title>Pet Photo 2</title></head>
    <body>
        <h1>Pet Photo 2</h1>
        <img src="" alt="salad" style="width:500px;">
        <p>Here's another adorable pet photo!</p>
        <p><a href="/home">Back to home</a></p>
        <p><a href="/pet3">Next pet photo</a></p>
    </body>
    </html>
    """

@app.route('/pet3')
def pet3():
    return """
    <html>
    <head><title>Pet Photo 3</title></head>
    <body>
        <h1>Pet Photo 3</h1>
        <img src="" alt="salad" style="width:500px;">
        <p>Here's one more cute pet photo!</p>
        <p><a href="/home">Back to home</a></p>
        <p><a href="/space1">Next space photo</a></p>
    </body>
    </html>
    """

@app.route('/space1')
def space1():
    return """
    <html>
    <head><title>Space Photo 1</title></head>
    <body>
        <h1>Space Photo 1</h1>
        <img src="" alt="salad" style="width:500px;">
        <p>Here's an amazing outer space photo!</p>
        <p><a href="/home">Back to home</a></p>
        <p><a href="/space2">Next space photo</a></p>
    </body>
    </html>
    """

@app.route('/space2')
def space2():
    return """
    <html>
    <head><title>Space Photo 2</title></head>
    <body>
        <h1>Space Photo 2</h1>
        <p>Here's another breathtaking space photo!</p>
        <img src="" alt="salad" style="width:500px;">
        <p><a href="/home">Back to home</a></p>
        <p><a href="/space3">Next space photo</a></p>
    </body>
    </html>
    """

@app.route('/space3')
def space3():
    return """
    <html>
    <head><title>Space Photo 3</title></head>
    <body>
        <h1>Space Photo 3</h1>
        <p>Here's one more awe-inspiring space photo!</p>
        <img src="" alt="salad" style="width:500px;">
        <p><a href="/home">Back to home</a></p>
        <p><a href="/pet1">Next pet photo</a></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)    