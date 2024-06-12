from flask import Flask, request, render_template
from models.submit import submit
import os, csv
from flask_mail import Mail, Message


app = Flask(__name__)

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
        jlpt_counters[level] = 1

print(jlpt_counters)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def form_submit():
    if request.method == 'POST':
        # Access form data
        jlpt_level = request.form['jlpt_level']
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
        # Create a string to write to the file
        string = f"\"{jlpt_level.strip()}\",\"24B\",\"8210101\",\"{jlpt_level.strip()}\",\"{jlpt_counters.get(jlpt_level, 0):04}\",\"{full_name.strip()}\",\"{gender.strip()}\",\"{dob_year.strip()}\",\"{dob_month.strip()}\",\"{dob_day.strip()}\",\"{pass_code.strip()}\",\"{native_language.strip()}\",\"{place_learn_jp.strip()}\",\"{reason_jlpt.strip()}\",\"{occupation.strip()}\",\"{occupation_details.strip()}\",\"{media}\",\"{teacher}\",\"{friends}\",\"{family}\",\"{supervisor}\",\"{colleagues}\",\"{customers}\",\"{jlpt_n1}\",\"{jlpt_n2}\",\"{jlpt_n3}\",\"{jlpt_n4}\",\"{jlpt_n5}\",\"{n1_result.strip()}\",\"{n2_result.strip()}\",\"{n3_result.strip()}\",\"{n4_result.strip()}\",\"{n5_result.strip()}\""
        infor_string = f"\"{full_name}\", \"{email}\", \"{phone_number}\", \"{adress}\", \"{country}\", \"{zip_code}\""


        # Create separate files for each JLPT level
        data_file = f"data_N{jlpt_level}.csv"
        infor_file = f"infos_N{jlpt_level}.csv"

        # Write the string and infor_string to their respective files
        with open(data_file, 'a') as f:
            f.write(string + '\n')

        with open(infor_file, 'a') as f:
            f.write(infor_string + '\n')

        
        form_data = {
            'JLPT Level': request.form['jlpt_level'],
            'Full Name': request.form['full_name'].upper(),
            'Gender': request.form['gender'].upper(),
            'Year Of Birth': request.form['dob_year'],
            'Month of Birth': request.form['dob_month'],
            'Day Of Birth': request.form['dob_day'],
            'Pass code': request.form['pass_code'],
            'Native_language': request.form['native_language'].upper(),
            'nationality': request.form['nationality'].upper(),
            'adress': request.form['adress'].upper(),
            'country': request.form['country'].upper(),
            'zip_code': request.form['zip_code'],
            'phone_number': request.form['phone_number'],
            'email': request.form['email'],
            'institute': request.form['institute'].upper(),
            'place_learn_jp': request.form['place_learn_jp'].upper(),
        }
        
        return render_template('confirm.html', form_data=form_data)

@app.route('/confirm', methods=['POST'])
def confirm():
    form_data = request.form.to_dict()
    sender = 'Your Email'
    msg = Message('JLPT Inscription', sender=sender, recipients=[form_data['email']])  # Change recipient email address
    msg.body = f"Dear {form_data['Full Name']},\n\nThank you for submitting the form. Your JLPT level is {form_data['JLPT Level']}, Your Passcode is : {form_data['Pass code']}.\n\nBest regards,\nMrCloud."
    mail.send(msg)
    return render_template('success.html')


@app.route('/JLPT/N<level>')
def get_data(level):
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


if __name__ == '__main__':
    app.run(debug=True)