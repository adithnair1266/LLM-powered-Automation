function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var phoneno = document.getElementById("phoneno").value;

    // Validate Username
    if(username.length<4 || username.length>20) {
        alert("Username should be between 4 and 20 characters");
        return false;
    }

    // Validate Password
    if(password.length<6) {
        alert("Password is too short");
        return false;
    }

    // Validate Email
    var emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if(!emailRegex.test(email)) {
        alert("Invalid Email");
        return false;
    }

    // Validate Phone Number
    var phonenoRegex = /^\d{10}$/;
    if(!phonenoRegex.test(phoneno)) {
        alert("Invalid Phone Number");
        return false;
    }

    return true;
}

function submitForm() {
    if(validateForm()) {
        document.getElementById("myForm").submit();
    }
}