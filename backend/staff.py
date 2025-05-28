# # --- Login (set JWT cookie) ---
# from flask import request, jsonify, make_response
# import jwt
# import datetime
# import mysql.connector
# from app import app, get_db_connection 

# @app.route('/staff-login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')

#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)

#     try:
#         cursor.execute("SELECT * FROM staff_account WHERE username = %s", (username,))
#         user = cursor.fetchone()

#         if user and user['password'] == password:
#             token = jwt.encode({
#                 'username': username,
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
#             }, app.config['SECRET_KEY'])

#             response = make_response(jsonify({'success': True}))
#             response.set_cookie('token', token, httponly=True, samesite='Strict')
#             return response, 200

#         return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

#     except mysql.connector.Error as err:
#         return jsonify({'message': f"Error: {err}"}), 500

#     finally:
#         cursor.close()
#         connection.close()
