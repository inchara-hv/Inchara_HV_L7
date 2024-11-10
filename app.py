from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    with sqlite3.connect("chocolate_house.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS seasonal_flavors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                flavor_name TEXT NOT NULL,
                available_season TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredient_name TEXT NOT NULL,
                quantity_in_stock INTEGER NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer_suggestions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                flavor_suggestion TEXT NOT NULL,
                allergy_concerns TEXT
            )
        ''')

# Route to the homepage
@app.route('/')
def index():
    return render_template("index.html")

# Route to view and add seasonal flavors
@app.route('/flavors', methods=['GET', 'POST'])
def seasonal_flavors():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    
    if request.method == 'POST':
        flavor_name = request.form['flavor_name']
        available_season = request.form['available_season']
        #check flavour is already exist
        existing_flavour=cursor.fetchone()
        if existing _flavour:
        error_message=falvour already exists!"
        return
        render_template("seasonal_flavour.html",error_message=error_message)
        
        cursor.execute("INSERT INTO seasonal_flavors (flavor_name, available_season) VALUES (?, ?)", 
                       (flavor_name, available_season))
        conn.commit()
        return redirect(url_for('seasonal_flavors'))

    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()
    conn.close()
    return render_template("seasonal_flavors.html", flavors=flavors)

# Route to view and add ingredients
@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    
    if request.method == 'POST':
        ingredient_name = request.form['ingredient_name']
        quantity_in_stock = request.form['quantity_in_stock']
        cursor.execute("INSERT INTO ingredients (ingredient_name, quantity_in_stock) VALUES (?, ?)", 
                       (ingredient_name, quantity_in_stock))
        conn.commit()
        return redirect(url_for('ingredients'))

    cursor.execute("SELECT * FROM ingredients")
    ingredients = cursor.fetchall()
    conn.close()
    return render_template("ingredients.html", ingredients=ingredients)

# Route to view and add customer suggestions
@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()

    
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        flavor_suggestion = request.form['flavor_suggestion']
        allergy_concerns = request.form['allergy_concerns']
        cursor.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)", 
                       (customer_name, flavor_suggestion, allergy_concerns))
        conn.commit()
        return redirect(url_for('suggestions'))

    cursor.execute("SELECT * FROM customer_suggestions")
    suggestions = cursor.fetchall()
    conn.close()
    return render_template("suggestions.html", suggestions=suggestions)

# Run the application
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
