const register = document.getElementById('register')
const surname = document.getElementById('surname')
const othernames = document.getElementById('othernames')
const username = document.getElementById('username')
const password = document.getElementById('password')
const password2 = document.getElementById('password2')
const uphone = document.getElementById('contact')
const uemail = document.getElementById('email')
const staff_type = document.getElementById('staff_type')
const errorElement= document.getElementById('error')
const sex = document.getElementById('gender')


register.addEventListener('submit', (e) => {
    let messages = []

    if (password.value.length || password2.value.length <= 7){
        messages.push('Password length must be longer than 7 characters')
        password.focus()
    }

    if(password.value !== password2.value){
        messages.push('Your Passwords do not match!')
        password2.focus()
    }

    if(allLetter(surname) == false){
        messages.push ('Name must have alphabet characters only!')
        surname.focus()
    }

    if(allLetters(othernames) == false){
        messages.push ('Other names can have alphabet characters and spaces only')
        othernames.focus()
    }

    if(gender(sex) == false){
        messages.push ('Please select your gender!')
        sex.focus()
    }

    if(allnumeric(uphone) == false){
        messages.push ('Contact should be only numbers')
        uphone.focus()
    }

    if(ValidateEmail(uemail) == false){
        messages.push ('Enter a valid Email!')
        uemail.focus()
    }

    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(",\n")
    }
})



function allLetter(uname){ 
    var letters = /^[A-Za-z]+$/;
    if(uname.value.match(letters))
        {
            return true;
        }
    else
        {
            return false;
        }
}

function allLetters(uname1){ 
    var letters = /^[A-Za-z ]+$/;
    if(uname1.value.match(letters))
        {
            return true;
        }
    else
        {
            return false;
        }
}


function gender(sex){
    if(sex.value === '' || sex.value == null)
        {
            return false;
        }
    else
        {
            return true;
        }
    }

function allnumeric(uphone){ 
    var numbers = /^[0-9]+$/;
    if(uphone.value.match(numbers))
        {
            return true;
        }
    else
        {
            return false;
        }
}

function ValidateEmail(uemail){
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(uemail.value.match(mailformat))
        {
            return true;
        }
    else
        {
            return false;
        }
}