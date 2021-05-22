from flask import Flask, render_template,request,redirect,url_for
from flask_mysqldb import MySQL,MySQLdb
import bcrypt 

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "bankita"

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def base():
    return render_template("base.html")


@app.route('/register/', methods=['GET','POST'])
def register():

    if request.method == 'POST' :
        Customer_id = request.form['customer_id']
        Customer_name = request.form['customer_name']
        Address = request.form['address']
        Phone = request.form['phone']
        Email = request.form['email']
        Password = request.form['password']
        Type = request.form['Type']
        Account_id = request.form['customer_id']

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO customer  (Customer_id, Customer_name, Address, Phone, Email, Password) VALUES (%s,%s,%s,%s,%s,%s)", (Customer_id, Customer_name, Address, Phone, Email, Password))
        cur.execute("INSERT INTO account  (Account_id, Customer_id, type) VALUES (%s,%s,%s)", (Account_id, Customer_id, Type))

        mysql.connection.commit()

        cur.close()
        
        return render_template("base.html")

    return render_template("register.html")

@app.route('/loginCustomer/', methods=['GET','POST'])
def logincustomer():

    if request.method == 'POST' :
        Email = request.form['email']
        Password = request.form['password']
        
        cur = mysql.connection.cursor()

        query = 'SELECT Email, Password FROM customer \
        where Email=\'%s\' and Password=\'%s\' '
        query = query % (Email, Password)
        cur.execute(query)
        mysql.connection.commit()
        rows =cur.fetchall()
        accept_Login = True
        if (len(rows)) == 0:
            accept_Login = False

        if accept_Login == False:

            return render_template("loginCustomer.html")
        elif Email == rows[0][0] and Password == rows[0][1]:
            accept_Login = True

            return render_template("halamanCustomer.html")
        
        cor.close()

    else:
        return render_template("loginCustomer.html")

@app.route('/base.html/', methods=['GET'])
def logoutcutomer():

    return render_template("base.html")

@app.route('/loginAdmin/', methods=['GET','POST'])
def loginadmin():

    
    if request.method == 'POST' :
        Username = request.form['username']
        Password = request.form['password']
        
        cur = mysql.connection.cursor()

        query = 'SELECT username, Password FROM admin \
        where username=\'%s\' and Password=\'%s\' '
        query = query % (Username, Password)
        cur.execute(query)
        mysql.connection.commit()
        rows =cur.fetchall()
        accept_Login = True
        if (len(rows)) == 0:
            accept_Login = False

        if accept_Login == False:

            return render_template("loginAdmin.html")
        elif Username == rows[0][0] and Password == rows[0][1]:
            accept_Login = True

            return render_template("halamanAdmin.html")
        
        cor.close()

    else:
        return render_template("loginAdmin.html")

@app.route('/information/', methods=['POST'])
def information():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from account ")
    rv = cur.fetchall()

    return render_template("information", value=rv)


if __name__ == "__main__":
    app.run(debug=True)