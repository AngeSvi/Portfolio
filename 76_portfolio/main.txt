from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index(): 
  return f"""<html><body>
  <p><a href = "/home">Go home</a></p>
  </body>
  </html>"""
  

@app.route('/home') 
def home(): 
  page = """html
  
  <html>
    
  <head>
    <title>Home</title>
  </head>


  <body>
  <h1>Replit website</h1> 
  <h2>Welcome to our website!</h2>

  <p><a href="/portfolio">Go to the portfolio</a></p>
  <p><a href="/linktree">Go to the the linktree</a></p>
  
</body>
  
</html>
  
  """
  
  return page

@app.route('/portfolio')
def portfolio():
    return """<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title>My portfolio</title>
        <link href="static/style.css" rel="stylesheet" type="text/css" />
    </head>


    <body>
        
        <h1 class="ange">Ange - Portfolio</h1>

        <h2 class="day">Day 13</h2>
        <img src="static/portfolio_pictures/squirrel.jpg" width = 30%>
        <p><a href="https://replit.com/@ninetteSvi/day-13100-days">Grade generator</a></p>
        <p><h3>Challenge</h3>
            <ul>
                <li>You are going to ask the user to type in the name of a test, maximum score they could receive, and how many points they received.</li>
                <li>Figure out the percentage the user received and round to 2 decimal places.</li>
                <li>Use if/elif statements to show users the letter grade they received.</li>
                <li>At the end, the user should see the letter grade they received and the percentage correct.</li>
            </ul>
        </p>
        
        <h2>Day 26</h2>
        <img src="static/portfolio_pictures/shark.jpg" width = 30%>
        <p><a href = "https://replit.com/@ninetteSvi/day26100-days-of-code">iPod</a></p>
        <p><h3>Challenge</h3>
            <ul>
                <li>Use a while true loop to create a title for a music player.</li>
                <li>Allow the user to select to play a song and use subroutine called 'play' when they select the song.</li>
                <li>Give the user the option to exit the program.</li>
                <li>The title should pop up and pause along with the menu options.</li>
                <li>If the user chooses anything else, start again by clearing the screen.</li>
            </ul>   
        </p>
        
        <h2>Day 31</h2>
        <img src="static/portfolio_pictures/sparrow.jpg" width = 30%>
        <p><a href = "https://replit.com/@ninetteSvi/Day31100-days">Music app</a></p>
        <p><h3>Challenge</h3>

            <ul>
                <li>Create a classic user interface using string manipulation.</li>
                <li>Create these two user interfaces (below) using everything you know about extensions to print statements and f-strings.</li>
                <li>The second one is a bit more tricky as it involves alignment.</li>
                <li>There are no input statements. This is all about using print and variables in interesting ways. However, you may want to create a subroutine to make the color changing easier (like you did on Day 29).</li>
             </ul>    
        </p>
        
        <h2>Day 43</h2>
        <img src="static/portfolio_pictures/spider.jpg" width = 30%>
        <p><a href = "https://replit.com/@ninetteSvi/Day43100Days">BINGO</a></p>
        <p><h3>Challenge</h3>
            <ul>
                <li>Randomly generate a series of number between 0 and 90. Allocate each number to a place in a 2D list.</li>
                <li>The numbers should be in numerical order, left to right and should not be repeated.</li>
                <li>The center square should not contain a number. It should contain the word 'BINGO!'.</li>
                <li>When the program is run, the bingo card should be displayed on screen.</li>
            </ul>    
        </p>
        
        <h2>Day 59</h2>
        <img src="static/portfolio_pictures/capibara.png" width = 30%>
        <p><a href = "https://replit.com/@ninetteSvi/Day59100Days">A Man A Plan A Canal Panama!</a></p>
        <p><h3>Challenge</h3>
            <ul>
                <li>Prompt the user to input a word.</li>
                <li>Analyze the word to see if it is a palindrome.</li>
                <li>Output a relevant 'yes/no message.</li>
            </ul>
        </p>
    
    </body>

</html>"""

@app.route('/linktree')
def linktree():
    return """<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>link tree</title>
    <link href="static/style2.css" rel="stylesheet" type="text/css" />
</head>

<body>
    <img src="static/portfolio_pictures/capibara.png", width=50%>
    <h1>Ange Svi</h1>
    <h4>Replit explorer</h4>
    <h2>Socials</h2>
    <p><a class="link" href="https://www.youtube.com/@gaellegarciadiaz1">YouTube (@gaellegarciadiaz1)</a></p>
    <p><a class="link" href="https://replit.com/@ninetteSvi">Replit (@ninetteSvi)</a></p>
    <p><a class="link" href="https://www.youtube.com/user/joueurdugrenier">YouTube (@joueurdugrenier)</a></p>
    
    
    <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>
"""

app.run(host='0.0.0.0', port=81)