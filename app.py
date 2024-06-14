from flask import Flask, session, request, render_template, flash, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os, csv
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Hardcoded user credentials (for demo purposes)
users = {
    'shab': {'password': 'shab'}
}

# User class for Flask-Login (replace with your actual User model if using a database)
class User(UserMixin):
    pass

# Load user function for Flask-Login (replace with your actual user loading logic)
@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        user = User()
        user.id = user_id
        return user
    return None

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Your SMTP server address
app.config['MAIL_PORT'] = 587  # Your SMTP server port
app.config['MAIL_USERNAME'] = 'YourEmail'  # Your email username
app.config['MAIL_PASSWORD'] = 'Your Pasword'  # Your email password
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USE_SSL'] = False  # Disable SSL

mail = Mail(app)

# Initialize jlpt_counters
jlpt_counters = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0}
for level in ['1', '2', '3', '4', '5']:
    file_path = f"data_N{level}.csv"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            last_row = None
            for row in reader:
                last_row = row
            if last_row is not None:
                jlpt_counters[level] = int(last_row[4])  # Assuming JLPT counter is in 5th column
    else:
        jlpt_counters[level] = 0

#@app.after_request
#def add_header(response):
#    response.cache_control.no_store = True
#    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User()
            user.id = username
            login_user(user)
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('jlpt'))  # Redirect to 'jlpt' endpoint
        else:
            return 'Invalid username/password combination'
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        logout_user()
        session.pop('logged_in', None)
        session.pop('username', None)
        return redirect(url_for('login'))


@app.route('/', strict_slashes=False)
def index():
    print("Main Page")
    return render_template('index.html')

@app.route('/submit', methods=['POST'], strict_slashes=False)
def form_submit():
    if request.method == 'POST':
        # Access form data
        jlpt_level = request.form['jlpt_level']
        if jlpt_level not in ['1', '2', '3', '4', '5']:
            flash("Invalid JLPT level!")
            return redirect(url_for('index'))
        test_center = request.form['test_center']
        full_name = request.form['full_name'].upper()
        gender = request.form['gender']
        dob_year = request.form['dob_year']
        dob_month = request.form['dob_month']
        dob_day = request.form['dob_day']
        pass_code = request.form['pass_code']
        native_language = request.form['native_language']
        nationality = request.form['nationality']
        adress = request.form['adress']
        country = request.form['country']
        zip_code = request.form['zip_code']
        phone_number = request.form['phone_number']
        email = request.form['email']
        institute = request.form['institute']
        place_learn_jp = request.form['place_learn_jp']
        reason_jlpt = request.form['reason_jlpt']
        occupation = request.form['occupation']
        occupation_details = request.form['occupation_details']
        media_jp = request.form.getlist('media_jp')
        media = ''.join(choice if choice in media_jp else ' ' for choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        communicate_teacher = request.form.getlist('communicate_teacher')
        teacher = ''.join(choice if choice in communicate_teacher else ' ' for choice in ['1', '2', '3', '4'])
        communicate_friends = request.form.getlist('communicate_friends')
        friends = ''.join(choice if choice in communicate_friends else ' ' for choice in ['1', '2', '3', '4'])
        communicate_family = request.form.getlist('communicate_family')
        family = ''.join(choice if choice in communicate_family else ' ' for choice in ['1', '2', '3', '4'])
        communicate_supervisor = request.form.getlist('communicate_supervisor')
        supervisor = ''.join(choice if choice in communicate_supervisor else ' ' for choice in ['1', '2', '3', '4'])
        communicate_colleagues = request.form.getlist('communicate_colleagues')
        colleagues = ''.join(choice if choice in communicate_colleagues else ' ' for choice in ['1', '2', '3', '4'])
        communicate_CUSTOMERS = request.form.getlist('communicate_CUSTOMERS')
        customers = ''.join(choice if choice in communicate_CUSTOMERS else ' ' for choice in ['1', '2', '3', '4'])
        jlpt_n1 = request.form['jlpt_n1']
        jlpt_n2 = request.form['jlpt_n2']
        jlpt_n3 = request.form['jlpt_n3']
        jlpt_n4 = request.form['jlpt_n4']
        jlpt_n5 = request.form['jlpt_n5']
        n1_result = request.form['n1_result']
        n2_result = request.form['n2_result']
        n3_result = request.form['n3_result']
        n4_result = request.form['n4_result']
        n5_result = request.form['n5_result']

        jlpt_n1 = ' ' if jlpt_n1 == '0' else jlpt_n1
        jlpt_n2 = ' ' if jlpt_n2 == '0' else jlpt_n2
        jlpt_n3 = ' ' if jlpt_n3 == '0' else jlpt_n3
        jlpt_n4 = ' ' if jlpt_n4 == '0' else jlpt_n4
        jlpt_n5 = ' ' if jlpt_n5 == '0' else jlpt_n5

        if jlpt_level in jlpt_counters:
            jlpt_counters[jlpt_level] += 1
        
        print(jlpt_counters)
        # Create a string to write to the The candidate information in the file.
        string = f"\"{jlpt_level.strip()}\",\"24B\",\"8210101\",\"{jlpt_level.strip()}\",\"{jlpt_counters.get(jlpt_level, 0):04}\",\"{full_name.strip()}\",\"{gender.strip()}\",\"{dob_year.strip()}\",\"{dob_month.strip()}\",\"{dob_day.strip()}\",\"{pass_code.strip()}\",\"{native_language.strip()}\",\"{place_learn_jp.strip()}\",\"{reason_jlpt.strip()}\",\"{occupation.strip()}\",\"{occupation_details.strip()}\",\"{media}\",\"{teacher}\",\"{friends}\",\"{family}\",\"{supervisor}\",\"{colleagues}\",\"{customers}\",\"{jlpt_n1}\",\"{jlpt_n2}\",\"{jlpt_n3}\",\"{jlpt_n4}\",\"{jlpt_n5}\",\"{n1_result.strip()}\",\"{n2_result.strip()}\",\"{n3_result.strip()}\",\"{n4_result.strip()}\",\"{n5_result.strip()}\""
        data_string = f'"{jlpt_counters.get(jlpt_level, 0):04}","{jlpt_level}","{test_center}","{full_name}","{gender}","{dob_year}","{dob_month}","{dob_day}","{pass_code}","{native_language}","{nationality}","{adress}","{country}","{zip_code}","{phone_number}","{email}","{institute}"'

        # Create separate files for each JLPT level
        data_file = f"data_N{jlpt_level}.csv"
        infor_file = f"infos_N{jlpt_level}.csv"

        # Write the string and infor_string to their respective files
        with open(data_file, 'a') as f:
            f.write(string + '\n')

        with open(infor_file, 'a') as f:
            f.write(data_string + '\n')
        
        form_data = {
            'JLPT Level': request.form['jlpt_level'],
            'Full Name': request.form['full_name'].upper(),
            'Gender': request.form['gender'].upper(),
            'Year Of Birth': request.form['dob_year'],
            'Month of Birth': request.form['dob_month'],
            'Day Of Birth': request.form['dob_day'],
            'Nationality': request.form['nationality'].upper(),
            'Pass code': request.form['pass_code'],
            'Native_language': request.form['native_language'].upper(),
            'nationality': request.form['nationality'].upper(),
            'adress': request.form['adress'].upper(),
            'country': request.form['country'].upper(),
            'zip_code': request.form['zip_code'],
            'phone_number': request.form['phone_number'],
            'email': request.form['email'],
            'institute': request.form['institute'].upper(),
        }
        
        return render_template('confirm.html', form_data=form_data)

@app.route('/confirm', methods=['POST'], strict_slashes=False)
def confirm():
    print("confirm Page")
    form_data = request.form.to_dict()
    full_name = form_data['Full Name']
    email = form_data['email']
    #send_email(full_name, email)
    return render_template('success.html')


def send_email(full_name, email):
    sender = 'Your Email'
    msg = Message('JLPT Inscription', sender=sender, recipients=[email])  # Change recipient email address
    msg.body = f"Dear {full_name},\n\nThank you for submitting the form. Your JLPT level is {email}.\n\nBest regards,\nMrCloud."
    mail.send(msg)

@app.route('/JLPT', strict_slashes=False)
def jlpt():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        #route to display The JLPT Levels Pages
        return render_template('jlpt.html')

@app.route('/JLPT/N<level>', strict_slashes=False)
def get_data(level):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        data_file = f"data_N{level}.csv"
        infor_file = f"infos_N{level}.csv"
        data = []
        infor = []
        if os.path.exists(data_file):
            with open(data_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    data.append(row)
        if os.path.exists(infor_file):
            with open(infor_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    infor.append(row)
        return render_template('data.html', data=data, infor=infor, level=level)


@app.route('/delete/<level>/<int:row_number>', methods=['POST', 'GET'], strict_slashes=False)
def delete_row(level, row_number):
    data_file = f"data_N{level}.csv"
    data_file_2 = f"infos_N{level}.csv"
    deleted_info = f"deleted_info_N{level}.csv"

    if os.path.exists(data_file) and os.path.exists(data_file_2):
        with open(data_file, 'r') as f:
            rows = list(csv.reader(f))
        
        with open(data_file_2, 'r') as f:
            rows_2 = list(csv.reader(f))

        if 0 <= row_number < len(rows):
            name = rows[row_number][5]  # Assuming name is in the 6th column
            rows.pop(row_number)
            deleted_row = rows_2.pop(row_number)

            # store the deleted row in a separate file for logging
            with open(deleted_info, 'a') as f:
                f.write(','.join(deleted_row) + '\n')
            

            # Decrement JLPT counter for remaining rows
            for i in range(row_number, len(rows)):
                rows[i][4] = f"{int(rows[i][4]) - 1:04}"  # Assuming JLPT counter is in the 5th column
            
            for i in range(row_number, len(rows_2)):
                rows_2[i][0] = f"{int(rows_2[i][0]) - 1:04}"  # Assuming JLPT counter is in the 1st column

            new_raws = []
            for row in rows: # Join elements of the row with commas and wrap them in double quotes
                row_string = ','.join([f'"{i}"' for i in row])
                new_raws.append(row_string)
            
            with open(data_file, 'w', newline='') as f:
                for row in new_raws:
                    f.write(row + '\n')
            
            with open(data_file_2, 'w', newline='') as f:
                for row in rows_2:
                    f.write(','.join(row) + '\n')
            
            flash(f"{name} deleted successfully!")
            return redirect(url_for('get_data', level=level))  # Return the deleted row surrounded by double quotes
        else:
            flash("Row number out of range!")
    else:
        flash("Data file not found!")
    
    return redirect(url_for('get_data', level=level))



if __name__ == '__main__':
    app.run(debug=True)