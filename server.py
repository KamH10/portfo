
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# ** Summary of running a flask server
#
# > cd C:\00-Kam\01-backup needed\05-Kam Books-Learning Videos\01-Learning Videos\Udemy\Python\00-Complete Python Developer in 2021_Neagoie\00-Notes-Code\code\1-tested\s19\s19e269_2Fn\webserver
# > scripts\activate 
#
# ** 1st way
# > set FLASK_ENV=development
# > python server.py
#
# - - - - - - - - - - - - - - - - - - - - 
# ** 2nd way
# > set FLASK_APP=server.py
# > set FLASK_ENV=development
# > python -m flask run    or > flask run
#
# - - - - - - - - - - - - - - - - - - - - 
# http://localhost:5000/    or  http://127.0.0.1:5000/
# > scripts\deactivate 
#
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from flask import Flask, render_template, url_for, request, redirect
import csv

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
app = Flask(__name__)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route('/')
def my_home():
    return render_template('index.html')

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route('/<string:page_name>')
def html_page(page_name):
    # print(f'** html_page() --> {page_name}')  # fDBG
    return render_template(page_name)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def write_to_text_file(data):
    # db_folder = 'db/'
    db_folder = 'portfo/db/'    # need to add 'portfo/' for pythonanywhere
    with open(db_folder + "database.txt", mode='a') as db1:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
    
        file = db1.write(f'{email},{subject},{message}\n')

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def write_to_csv_file(data):
    # db_folder = 'db/'
    db_folder = 'portfo/db/'    # need to add 'portfo/' for pythonanywhere
    with open(db_folder + "database.csv", mode='a', newline='') as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        
        csv_writer = csv.writer(db2, 
            delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email, subject, message])

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()

            # print(data) # fDBG
            write_to_text_file(data)
            write_to_csv_file(data)

            return redirect("/thank_you.html")
        except:
            return "Error: Did not save to the DB!"
    else:
        return 'Something went wrong!'
    

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# app.run(port=5000)
#
# **NOTE** Use the line above only for local delvelopment, using localhost.
# If you want to deploy your code to sites like PythonAnaywhere use the following.
# I could fix this using the following documentation under the 
# 'Do not use app.run()' section: https://help.pythonanywhere.com/pages/Flask/
#
if __name__ == '__main__':
    app.run()
