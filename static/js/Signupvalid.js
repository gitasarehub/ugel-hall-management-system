const form = document.getElementById('registration');
const uid = document.getElementById('userid');
const surname = document.getElementById('surname');
const othernames = document.getElementById('othernames');
const username = document.getElementById('username');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');
const uphone = document.getElementById('contact');
const uemail = document.getElementById('email');
const staff_type = document.getElementById('staff_type');


form.addEventListener('submit', (e) =>{
    e.preventDefault();

    checkInputs();
});

function checkInputs(){
    //get the values from the inputs
    // const usernameValue = username.value.trim()
    const uemailValue = uemail.value.trim()
    const surnameValue = surname.value.trim()
    const othernamesValue = othernames.value.trim()
    const passwordValue = password.value.trim()
    const password2Value = password2.value.trim()
    const uphoneValue = uphone.value.trim()
    const staff_typeValue = staff_type.value.trim()
    const uidValue = uid.value.trim()

    if(userid_validation(uidValue))
    {
        if(passwordcheck(passwordValue,password2Value))
        {
            if(allLetter(surnameValue))
                {
                if(allLetters(othernamesValue))
                    {
                    if(ValidateEmail(uemailValue))
                        {
                        if(passid_validation(passwordValue,7))
                            {
                            if(allnumeric(uphoneValue))
                                {
                                // if(hallselect(uhall))
                                    // {
                                    if(staff_typeselect(staff_typeValue))
                                        {
                                        // if(validsex(gender))
                                        //     {
                                        //         }
                                            }
                                        // } 
                                    } 
                                }
                            }
                        }
                    }
                }
            }else
            {
                return false;
            }

}


// function formValidation()
// {
// var uid = document.registration.passcode;
// var uname = document.registration.surname;
// var uname1 = document.registration.othernames;
// var password = document.registration.password;
// var password2 = document.registration.password2;
// var uhall = document.registration.hall;
// var uphone = document.registration.contact;
// var uemail = document.registration.email;
// var gender = document.registration.gender;
// var staff_type = document.registration.staff_type;

    // if(userid_validation(uid))
    // {
    //     if(passwordcheck(password,password2))
    //     {
    //     if(allLetter(uname))
    //     {
    //     if(allLetters(uname1))
    //     {
    //     if(ValidateEmail(uemail))
    //     {
    //     if(passid_validation(password,7))
    //     {
    //     if(allnumeric(uphone))
    //     {
    //     if(hallselect(uhall))
    //     {
    //     if(staff_typeselect(staff_type))
    //     {
    //     if(validsex(gender))
    //     {
    //     }
    //     }
    //     } 
    //     } 
    //     }
    //     }
    //     }
    //     }
    //     }
    //     return false;
    // }
    
// }

function userid_validation(uid){
var uid_len = uid.value.length;
if (uid_len = 0){
    alert("Enter a valid Passcode!");
    uid.focus();
    return false;
    }
else
    {
    return true;
    }
}

function passwordcheck(my,mx){
if(my==mx)
    {
        return true;
    }
else
    {
        alert("Passwords do not match!");
        mx.focus();
        return false;
    }
}


function passid_validation(password,my)
{
var password_len = password.value.length;
if (password_len >= my)
    {
        return true;
    }
else
    {
    alert("Your Password length should be more than "+my);
    passid.focus();
    }
}

function allLetter(uname){ 
var letters = /^[A-Za-z]+$/;
if(uname.value.match(letters))
    {
    return true;
    }
else
    {
    alert('Name must have alphabet characters only');
    uname.focus();
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
    alert('Other Names must have alphabet characters only');
    uname1.focus();
    }
}

function hallselect(uhall){
if(uhall.value == "")
    {
    alert('Select your hall from the list');
    uhall.focus();
    }
else
    {
    return true;
    }
}

function staff_typeselect(staff_type){
if(staff_type.value == "")
    {
    alert('Select your hall from the list');
    staff_type.focus();
    }
else
    {
    return true;
    }
}

function gender(sex){
    if(gender.value == "")
        {
        alert('Select your gender');
        gender.focus();
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
    alert('Phone number must have numeric characters only');
    uphone.focus();
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
    alert("You have entered an invalid email address!");
    uemail.focus();
    }
}