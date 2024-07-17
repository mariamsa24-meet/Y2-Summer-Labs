from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ( """
    <html>
    <head><title>Welcome to My Photo Gallery</title></head>
    <body>
        <h1>Welcome to My Photo Gallery</h1>
        <p>This gallery contains three types of photos: food, pets, and outer space.</p><br/>
        <a href="/food1">Next food photo</a>
    </html>
    """)

@app.route('/food1')
def food1():
    return("""
    <html>
    <head><title>Food Photo 1</title></head>
    <body>
        <h1>Food Photo 1</h1>
        <img calss='food' src="https://en.wikipedia.org/wiki/Food#/media/File:Good_Food_Display_-_NCI_Visuals_Online.jpg" style="width:500px;">
        <p>Here's a photo of delicious food!</p>
        <a href='/home'>Back to home</a><br/>
        <a href='/food2'>Next food photo</a>
    </body>
    </html>
    """)

@app.route('/food2')
def food2():
    return("""
    <html>
    <head><title>Food Photo 2</title></head>
    <body>
        <h1>Food Photo 2</h1>
        <img calss='food' src="https://en.wikipedia.org/wiki/Sushi#/media/File:Sushi_platter.jpg" style="width:500px;">
        <p>Here's another delicious food photo!</p>
        <a href=/home'>Back to home</a><br/>
        <a href='/food3'>Next food photo</a>
    </body>
    </html>
    """)

@app.route('/food3')
def food3():
    return ("""
    <html>
    <head><title>Food Photo 3</title></head>
    <body>
        <h1>Food Photo 3</h1>
        <img calss='food' src="https://en.wikipedia.org/wiki/Quarter_Pounder#/media/File:McDonald's_Quarter_Pounder_with_Cheese,_United_States.jpg" style="width:500px;">
        <p>Here's another tasty food photo!</p>
        <a href='/home'>Back to home</a><br/>
        <a href='/pet1'>Next pet photo</a>
    </body>
    </html>
    """)

@app.route('/pet1')
def pet1():
    return ( """
    <html>
    <head><title>Pet Photo 1</title></head>
    <body>
        <h1>Pet Photo 1</h1>
        <img calss='food' src="https://en.wikipedia.org/wiki/Cat#/media/File:Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg" style="width:500px;">
        <p>Here's a lovely pet photo!</p>
        <a href='/home'>Back to home</a><br/>
        <a href='/pet2'>Next pet photo</a>
    </body>
    </html>
    """)

@app.route('/pet2')
def pet2():
    return ("""
    <html>
    <head><title>Pet Photo 2</title></head>
    <body>
        <h1>Pet Photo 2</h1>
        <img calss='food' src="https://en.wikipedia.org/wiki/Golden_hamster#/media/File:Golden_hamster_front_1.jpg" style="width:500px;">
        <p>Here's another adorable pet photo!</p>
        <a href='/home'>Back to home</a><br/>
        <a href='/pet3'>Next pet photo</a>
    </body>
    </html>
    """)

@app.route('/pet3')
def pet3():
    return ("""
    <html>
    <head><title>Pet Photo 3</title></head>
    <body>
        <h1>Pet Photo 3</h1>
        <img calss='food' src="https://en.wikipedia.org/wiki/Oranda#/media/File:Orange_Oranda.jpg" style="width:500px;">
        <p>Here's one more cute pet photo!</p>
        <a href='/home'>Back to home</a><br/>
        <a href='/space1'>Next space photo</a>
    </body>
    </html>
    """)

@app.route('/space1')
def space1():
    return ("""
    <html>
    <head><title>Space Photo 1</title></head>
    <body>
        <h1>Space Photo 1</h1>
        <img calss='food' src="https://en.wikipedia.org/wiki/Wikipedia:Featured_pictures/Space/Looking_out#/media/File:The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA's_Solar_Dynamics_Observatory_-_20100819.jpg"  style="width:500px;">
        <p>Here's an amazing outer space photo!</p>
        <a href='/home'>Back to home</a><br/>
        <a href='/space2'>Next space photo</a>
    </body>
    </html>
    """)

@app.route('/space2')
def space2():
    return('''
    <html>
    <head><title>Space Photo 2</title></head>
    <body>
        <h1>Space Photo 2</h1>
        <p>Here's another breathtaking space photo!</p>
        <img calss='food' src="https://simple.wikipedia.org/wiki/Outer_space#/media/File:LH_95.jpg" style="width:500px;">
        <a href='/home'>Back to home</a><br/>
        <a href='/space3'>Next space photo</a>
    </body>
    </html>
    ''')

@app.route('/space3')
def space3():
    return("""
    <html>
    <head><title>Space Photo 3</title></head>
    <body>
        <h1>Space Photo 3</h1>
        <p>Here's one more awe-inspiring space photo!</p>
        <img calss='food' src="https://en.wikipedia.org/wiki/Outer_space#/media/File:Webb's_First_Deep_Field.jpg" style="width:500px;">
        <a href='/home'>Back to home</a><br/>
        <a href='/pet1'>Next pet photo</a>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)