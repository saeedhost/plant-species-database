import sqlite3

def get_data():
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    user_input= input("Enter plant name: ")
    c.execute("SELECT * FROM Database_databasemodel WHERE plant_name ='"+user_input+"'")

    results = c.fetchall()

    conn.close()

    if results:
        for result in results:
            print(result)
    else:
        print("No results found.")
        
get_data()

