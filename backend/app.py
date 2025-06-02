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
def get_db_connection_2():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="chromePassword12",
        database="student"
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

@app.route('/student_create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

   
    try:
        connection = get_db_connection_2()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student_registration_account WHERE username = %s", (username,))
        if cursor.fetchone():
            return jsonify({'error': 'Username already exists'}), 409

        cursor.execute(
            "INSERT INTO student_registration_account (username, password) VALUES (%s, %s)",
            (username,password)
        )
        connection.commit()
        return jsonify({'message': 'Account created successfully'}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

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
def student_registration():
    try:
        conn = get_db_connection_2()
        cursor = conn.cursor()

        data = request.form
        files = request.files

        # Helper function to safely get binary file data
        def get_file_bytes(file_key):
            return files[file_key].read() if file_key in files and files[file_key].filename != '' else None

        # Fetch form data and optional file uploads
        values = (
            data.get('username'),
            data.get('student_name'),
            data.get('father_name'),
            data.get('mother_name'),
            data.get('gender'),
            data.get('marital_status'),
            data.get('state'),

            data.get('dob'),
            data.get('religion'),
            data.get('caste'),
            data.get('nationality'),
            data.get('aadhar_number'),
            data.get('mobile_number'),
            data.get('physically_challenged'),
            data.get('locality'),
            data.get('course_category'),
            data.get('course_of_application'),
            data.get('degree_group') or None,
            data.get('degree_college_name') or None,
            data.get('degree_year_of_passing') or None,
            data.get('degree_reg_number') or None,
            data.get('degree_aggregate_percentage') or None,
            data.get('inter_group'),
            data.get('inter_college_name'),
            data.get('inter_year_of_passing'),
            data.get('inter_reg_number'),
            data.get('inter_aggregate_percentage'),
            data.get('tenth_school_name'),
            data.get('tenth_year_of_passing'),
            data.get('tenth_reg_number'),
            data.get('tenth_aggregate_percentage'),
            get_file_bytes('passport_size_photo'),
            get_file_bytes('tenth_memo'),
            get_file_bytes('inter_marksheet'),
            get_file_bytes('degree_marksheet'),  # optional
            get_file_bytes('degree_tc')          # optional
        )

        sql = """
            INSERT INTO student_registration (username,
            student_name, father_name, mother_name, gender, marital_status,
            dob, religion, caste, nationality, aadhar_number, mobile_number,
            physically_challenged, locality, state,course_category, course_of_application,
            degree_group, degree_college_name, degree_year_of_passing, degree_reg_number,
            degree_aggregate_percentage, inter_group, inter_college_name, inter_year_of_passing,
            inter_reg_number, inter_aggregate_percentage, tenth_school_name, tenth_year_of_passing,
            tenth_reg_number, tenth_aggregate_percentage, passport_size_photo, tenth_memo,
            inter_marksheet, degree_marksheet, degree_tc) VALUES (
                %s, %s, %s, %s, %s,%s,
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s, %s,%s)
            """

        cursor.execute(sql, values)
        conn.commit()

        return jsonify({"message": "Student registered successfully"}), 200

    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"message": "Database error", "error": str(e)}), 500

    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({"message": "Server error", "error": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
    
# userimage



@app.route('/user-details', methods=['GET'])
def get_profile_details():
    username = request.args.get('username')
    print("inside this python")
    if not username:
        return jsonify({"error": "student name is required"}), 400

    conn = get_db_connection_2()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT student_name,
               father_name, mother_name, dob,caste
        FROM student_registration
        WHERE username = %s
    """, (username,))
    user = cursor.fetchone()
    print(user)
    cursor.close()
    conn.close()

    if user:
        # Generate a pseudo URL pointing to the image endpoint
        user["image_url"] = f"http://localhost:5000/user-image?username={username}"
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

from flask import send_file
from io import BytesIO

@app.route('/user-image', methods=['GET'])
def get_user_image():
    username = request.args.get('username')

    if not username:
        return jsonify({"error": "Registration number is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT passport_size_photo FROM student_registration WHERE username = %s", (username,))
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