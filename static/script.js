let currentStep = 0;
        const steps = document.querySelectorAll(".step");

        function showStep(stepIndex) {
            steps.forEach((step, index) => {
                step.classList.toggle("active", index === stepIndex);
            });
        }

        function nextStep() {
            if (currentStep < steps.length - 1) {
                const activeStep = steps[currentStep];
        
                // Run validations for the current step
                if (!validateCurrentStep(activeStep)) {
                    return; // Stop execution if validation fails
                }
        
                // Show or hide navigation buttons based on current step
                if (currentStep === 0) { // Step 1: JLPT Level and Test Site
                    if (document.getElementById("jlpt_level").value < 1 || document.getElementById("jlpt_level").value > 5) {
                        window.alert("Please select a valid JLPT level (N1 to N5).");
                        return;
                    }
        
                    if (document.getElementById("test_center").value !== "Rabat") {
                        window.alert("Please select a valid test center.");
                        return;
                    }
                } else if (currentStep === 1) { // Step 2: Personal Information
                    const fullNameInput = activeStep.querySelector('#full_name');
                    const pattern = /^[A-Za-z\s]+$/;
                    if (!pattern.test(fullNameInput.value)) {
                        window.alert("Please enter a valid Given Name (letters and spaces only).");
                        return;
                    }
                } else if (currentStep === 2) { // Date of birth, Pass Code
                    const dob_year = document.getElementById("dob_year").value;
                    const dob_month = document.getElementById("dob_month").value;
                    const dob_day = document.getElementById("dob_day").value;
        
                    if (dob_year < 1900 || dob_year > new Date().getFullYear()) {
                        window.alert("Please enter a valid year of birth.");
                        return;
                    }
                    if (!validateDayOfBirth(dob_day, dob_month)) {
                        return; // Stop further execution if day of birth is invalid
                    }
        
                    const pass_code = document.getElementById("pass_code").value;
                    if (pass_code.length !== 8) {
                        window.alert("Please enter a valid 8-character pass code.");
                        return;
                    }
                } else if (currentStep === 3) { // Step 3: Native Language and Nationality
                    const native_language = document.getElementById("native_language").value;
                    if (![701, 606, 408, 411, 430, 0].includes(parseInt(native_language))) {
                        window.alert("Please select the correct native language.");
                        return;
                    }
        
                    const nationalityInput = activeStep.querySelector('#nationality');
                    if (!nationalityInput.value) {
                        window.alert("Please enter a valid nationality.");
                        return;
                    }
                } else if (currentStep === 4) { // Step 4: Address Information
                    const addressInput = activeStep.querySelector('#adress');
                    if (!addressInput.value) {
                        window.alert("Please enter a valid address.");
                        return;
                    }
        
                    const countrySelect = activeStep.querySelector('#countrySelect');
                    const otherCountryInput = activeStep.querySelector('#otherCountry');
                    if (countrySelect.value === "other" && !otherCountryInput.value) {
                        window.alert("Please specify your country.");
                        return;
                    }
                } else if (currentStep === 5) { // Step 5: ZIP Code, Phone Number, Email
                    const zipCodeInput = activeStep.querySelector('#zip_code');
                    const zipCodePattern = /^\d{5}$/; // Moroccan ZIP Code format
                    if (!zipCodePattern.test(zipCodeInput.value)) {
                        window.alert("Please enter a valid Moroccan ZIP Code.");
                        return;
                    }
        
                    const phoneNumberInput = activeStep.querySelector('#phone_number');
                    const phoneNumberPattern = /^(?:\+212|0)([ \-_/]*)(\d{9})$/; // Moroccan phone number format
                    if (!phoneNumberPattern.test(phoneNumberInput.value)) {
                        window.alert("Please enter a valid Moroccan phone number.");
                        return;
                    }
        
                    const emailInput = activeStep.querySelector('#email');
                    if (!emailInput.checkValidity()) {
                        window.alert("Please enter a valid email address.");
                        return;
                    }
                } else if (currentStep === 6) { // Step 6: Institute
                    if (!activeStep.querySelector("#institute").value) {
                        window.alert("Please enter a valid institute.");
                        return;
                    }
                } else if (currentStep === 7) { // Step 7: Reason for Taking the Exam
                    if (!activeStep.querySelector('#reason_jlpt').value) {
                        window.alert("Please select a reason for taking the exam.");
                        return;
                    }
                } else if (currentStep === 8) { // Step 8: Occupation
                    if (!activeStep.querySelector('#occupation').value) {
                        window.alert("Please select an occupation.");
                        return;
                    }
                } else if (currentStep === 9) { // Step 9: Occupation Details
                    if (!activeStep.querySelector('#occupation_details').value) {
                        window.alert("Please select occupation details.");
                        return;
                    }
                }
        
                // Move to the next step and show it
                currentStep++;
                showStep(currentStep);
        
                // Show or hide navigation buttons based on current step after moving
                if (currentStep === steps.length - 1) {
                    // Last step reached, hide next button and show submit button
                    document.getElementById('nextBtn').style.display = 'none';
                    document.getElementById('submitBtn').style.display = 'inline-block';
                } else {
                    // Show previous button if not the first step
                    document.getElementById('prevBtn').style.display = 'inline-block';
                }
            }
        }

        function prevStep() {
            if (currentStep > 0) {
                currentStep--;
                showStep(currentStep);
            }
        }

        showStep(currentStep); // Initialize form by showing the first step

        function selectJlptLevel(level) {
            document.getElementById("jlpt_level").value = level;
            const buttons = document.querySelectorAll("#jlptLevelButtons .btn");
            buttons.forEach((button, index) => {
                button.classList.toggle("active", 5 - index === level);
            });
        }

        function validateDayOfBirth(dob_day, dob_month) {
            if (dob_month < 1 || dob_month > 12) {
                // Invalid month
                window.alert("Please enter a valid month of birth.");
                return false;
            }
        
            if (dob_day < 1 || dob_day > 31) {
                // Day out of range
                window.alert("Please enter a valid day of birth.");
                return false;
            }
        
            if (dob_day > 30 && (dob_month == 4 || dob_month == 6 || dob_month == 9 || dob_month == 11)) {
                // Months with 30 days max
                window.alert("Please enter a valid day of birth for this month.");
                return false;
            }
        
            if (dob_month == 2) {
                // February, checking for leap year
                const currentYear = new Date().getFullYear();
                const isLeapYear = (year) => (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
        
                if (isLeapYear(currentYear) && dob_day > 29) {
                    window.alert("Please enter a valid day of birth for February in a leap year.");
                    return false;
                } else if (!isLeapYear(currentYear) && dob_day > 28) {
                    window.alert("Please enter a valid day of birth for February in a non-leap year.");
                    return false;
                }
            }
        
            // All validations passed
            return true;
        }
        function validateCurrentStep(activeStep) {
            // Implement validation logic specific to each step here, if needed
            return true; // Return true if validation passes
        }