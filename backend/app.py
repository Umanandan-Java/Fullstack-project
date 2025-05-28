from flask import Flask, Response, request, jsonify, make_response
from flask_cors import CORS
import mysql.connector
import jwt
import datetime
# import mysql.connector

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)
app.config['SECRET_KEY'] = 'your_super_secret_key'  # Replace with a secure key in production

# --- DB Connection ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="chromePassword12",
        database="userdb"
    )

# --- JWT Verification ---
def verify_jwt():
    token = request.cookies.get('token')
    if not token:
        return None
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return decoded
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None

# --- Account Creation ---
@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    reg_no = data.get('reg_no')
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM useraccounts WHERE username = %s", (username,))
        if cursor.fetchone():
            return jsonify({'error': 'Username already exists'}), 409
        cursor.execute("Select * from useraccounts where reg_no = %s",(reg_no,))
        if cursor.fetchone():
            return jsonify({"error":'Already registered with this Registration Number'})

        cursor.execute("INSERT INTO useraccounts (reg_no,username,password) VALUES (%s,%s, %s)", (reg_no,username, password))
        connection.commit()
        return jsonify({'message': 'Account created successfully'}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        connection.close()

# --- Login (JWT) ---

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    Registration_no = data.get('registration_no') 
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Get user by username
        cursor.execute("SELECT * FROM useraccounts WHERE username = %s", (username,))
        user = cursor.fetchone()
        print(user)
        if user and user['password'] == password:
            

            # Check if the student has a profile
            cursor.execute("SELECT * FROM student_registration WHERE Registration_no = %s", (Registration_no,))
            profile = cursor.fetchone()

            # Create JWT token
            token = jwt.encode({
                'username': username,
                # 'registration_no': registration_no,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }, app.config['SECRET_KEY'], algorithm='HS256')

            
            redirect_url = f'/profile?Registration_no={Registration_no}' if profile else '/student-page'

            # Send token and redirect URL to frontend
            response = make_response(jsonify({
                'success': True,
                'redirect': redirect_url
            }))
            response.set_cookie('token', token, httponly=True, samesite='Strict')
            return response, 200

        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

    except mysql.connector.Error as err:
        return jsonify({'message': f"Database error: {err}"}), 500

    finally:
        cursor.close()
        connection.close()

# --- Student Submission (Protected) ---
@app.route('/datasubmission', methods=['POST'])
def handlesubmission():
    user = verify_jwt()
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401

    data = request.get_json()
    name = data.get('name')
    course = data.get('course')
    mobile = data.get('mobile')
    location = data.get('location')

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            "INSERT INTO students_info (name, course, mobile, location) VALUES (%s, %s, %s, %s)",
            (name, course, mobile, location)
        )
        connection.commit()
        return jsonify({'message': 'Student registered successfully'}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        connection.close()

# --- Admin Data View ---
@app.route('/admin/data', methods=['GET'])
def admin_data():
    user = verify_jwt()
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM students_info")
        result = cursor.fetchall()
        return jsonify(result), 200

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        connection.close()

# --- Logout ---
@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({'message': 'Logged out successfully'}))
    response.set_cookie('token', '', expires=0, httponly=True, samesite='Strict')
    return response, 200

# --- Staff Login ---
@app.route('/staff-login', methods=['POST'])
def staff_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM staff_account WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and user['password'] == password:
            token = jwt.encode({
                'username': username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }, app.config['SECRET_KEY'])

            response = make_response(jsonify({'success': True}))
            response.set_cookie('token', token, httponly=True, samesite='Strict')
            return response, 200

        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

    except mysql.connector.Error as err:
        return jsonify({'message': f"Error: {err}"}), 500

    finally:
        cursor.close()
        connection.close()

# --- Staff Registration ---
@app.route('/staff-registration', methods=['POST'])
def userdetails():
    data = request.get_json()
    print("inside the userdetails")
    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    applicationno = data.get('Application_no')
    registrationno = data.get('Registration_no')
    firstname = data.get('firstname')
    middlename = data.get('middlename')
    lastname = data.get('lastname')
    fathername = data.get('fathername')
    qualification = data.get('qualification')
    year = data.get('year')

    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO student_details (Application_no, Registration_no, First_name, Middle_name, Last_name, Father_name, Qualification, Year) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (applicationno, registrationno, firstname, middlename, lastname, fathername, qualification, year)
        )
        con.commit()
        return jsonify({"message": "Inserted Successfully"}), 201

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

# --- ID Search ---
@app.route('/id_search', methods=["POST"])
def searchById():
    data = request.get_json()
    base_query = "SELECT Application_no,Registration_no, firstname,middlename, lastname,fathername,qualification,year,application_status FROM student_registration WHERE 1=1"
    values = []
    print("inside the api call")
    for field in ['Application_no', 'Registration_no']:
        if data.get(field):
            base_query += f" AND {field} LIKE %s"
            values.append(f"%{data[field]}%")

    try:
        print('inside the try block')
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(base_query, values)
        results = cursor.fetchall()
        print(results)
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@app.route('/student-registration', methods=['POST'])
def staff_registration():

    application_no = request.form.get('Application_no')
    registration_no = request.form.get('Registration_no')
    firstname = request.form.get('firstname')
    middlename = request.form.get('middlename')
    lastname = request.form.get('lastname')
    fathername = request.form.get('fathername')
    qualification = request.form.get('qualification')
    year = request.form.get('year')
    passport_size_photo = request.files.get('passport_size_photo')
    tenth_memo = request.files.get('tenth_memo')
    inter_marksheet = request.files.get('inter_marksheet')
    degree_marksheet = request.files.get('degree_marksheet')
    degree_tc = request.files.get('degree_tc')

    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)


        # Read file contents as bytes, or None if no file uploaded
        passport_size_photo_data = passport_size_photo.read() if passport_size_photo else None
        tenth_memo_data = tenth_memo.read() if tenth_memo else None
        inter_marksheet_data = inter_marksheet.read() if inter_marksheet else None
        degree_marksheet_data = degree_marksheet.read() if degree_marksheet else None
        degree_tc_data = degree_tc.read() if degree_tc else None

        # Insert into your table (adjust table & column names accordingly)
        query = """
            INSERT INTO student_registration (
                Application_no, Registration_no, firstname, middlename, lastname, fathername,
                qualification, year, tenth_memo, inter_marksheet, degree_marksheet, degree_tc,passport_size_photo
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """
        cursor.execute(query, (
            application_no, registration_no, firstname, middlename, lastname, fathername,
            qualification, year, tenth_memo_data, inter_marksheet_data, degree_marksheet_data, degree_tc_data,passport_size_photo_data
        ))

        con.commit()
        cursor.close()

        return jsonify({"message": "Student Registration successful"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

    
# userimage



@app.route('/user-details', methods=['GET'])
def get_user_details():
    Registration_no = request.args.get('registration_number')

    if not Registration_no:
        return jsonify({"error": "Registration number is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT Application_no, Registration_no, firstname, middlename, lastname,
               fathername, qualification, year,application_status
        FROM student_registration
        WHERE Registration_no = %s
    """, (Registration_no,))
    user = cursor.fetchone()
    print(user)
    cursor.close()
    conn.close()

    if user:
        # Generate a pseudo URL pointing to the image endpoint
        user["image_url"] = f"http://localhost:5000/user-image?registration_number={Registration_no}"
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

from flask import send_file
from io import BytesIO

@app.route('/user-image', methods=['GET'])
def get_user_image():
    Registration_no = request.args.get('registration_number')

    if not Registration_no:
        return jsonify({"error": "Registration number is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT passport_size_photo FROM student_registration WHERE Registration_no = %s", (Registration_no,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row and row[0]:
        image_blob = row[0]  # Binary data
        return send_file(BytesIO(image_blob), mimetype='image/jpeg')
    else:
        return jsonify({"error": "Image not found"}), 404
    



# --- ID Search ---
@app.route('/alldata', methods=["POST"])
def searchAllData():
    base_query = "SELECT Application_no,Registration_no, firstname,middlename, lastname,fathername,qualification,year,application_status FROM student_registration WHERE 1=1"
    
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(base_query)
        results = cursor.fetchall()
        print(results)
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)