from flask import Flask, request

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def process():
    page = "Hi there fellow human"
    form = request.form

    if form["material"] == "yes":
        if form["infinite"].lower() != "infinity":
            if form["food"] == "robot":
                page = "You are definitely a robot"
                
    return page

@app.route('/')
def menu():
    page = """<form method="post" action="/answer">
        
        <p>Are you made of metal ?</p>
            <div>
                <input type="radio" id="material1" name="material" value="yes" />
                <label for="material1">Yes</label>
                <input type="radio" id="material2" name="material" value="no" />
                <label for="material2">No</label>
                    
        <p>What is infinity + 1 ?<input type="text" name="infinite"></p>
        
        <p>Which is your favorite food ?</p>
            <select name="food" id="food_select">
                <option value="human">Human food</option>
                <option value="robot">Engine oil</option>
            </select>

        <br>
        <button type="submit">I'm not a robot</button>
        
    </form>
    
    """

    return page

app.run(host='0.0.0.0', port=81)