from flask import request

jlpt_counters = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0
    }

def submit():
    if request.method == 'POST':
        # Access form data
        jlpt_level = request.form['jlpt_level']
        test_center = request.form['test_center']
        full_name = request.form['full_name']
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

        if jlpt_level in jlpt_counters:
            jlpt_counters[jlpt_level] += 1
        
        print(jlpt_counters)
    
        string = f"\"{jlpt_level.strip()}\",\"24B\",\"8210101\",\"{jlpt_level.strip()}\",\"{jlpt_counters.get(jlpt_level, 0):04}\",\"{full_name.strip()}\",\"{gender.strip()}\",\"{dob_year.strip()}\",\"{dob_month.strip()}\",\"{dob_day.strip()}\",\"{pass_code.strip()}\",\"{native_language.strip()}\",\"{place_learn_jp.strip()}\",\"{reason_jlpt.strip()}\",\"{occupation.strip()}\",\"{occupation_details.strip()}\",\"{media}\",\"{teacher}\",\"{friends}\",\"{family}\",\"{supervisor}\",\"{colleagues}\",\"{customers}\",\"{jlpt_n1.strip()}\",\"{jlpt_n2.strip()}\",\"{jlpt_n3.strip()}\",\"{jlpt_n4.strip()}\",\"{jlpt_n5.strip()}\",\"{n1_result.strip()}\",\"{n2_result.strip()}\",\"{n3_result.strip()}\",\"{n4_result.strip()}\",\"{n5_result.strip()}\""
        infor_string = f"\"{full_name}\", \"{email}\", \"{phone_number}\", \"{adress}\", \"{country}\", \"{zip_code}\""

        print(string)
        print(infor_string)
        return 'Form submitted successfully!'
