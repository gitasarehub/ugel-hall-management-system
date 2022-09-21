function formValidation()
{
var uid = document.registration.passcode;
var uname = document.registration.surname;
var uname1 = document.registration.othernames;
var password = document.registration.password;
var password2 = document.registration.password2;
var uhall = document.registration.hall;
var uphone = document.registration.contact;
var uemail = document.registration.email;
var gender = document.registration.gender;
var staff_type = document.registration.staff_type;

    if(userid_validation(uid))
    {
    if(passwordcheck(password,password2))
    {
    if(allLetter(uname))
    {
    if(allLetters(uname1))
    {
    if(ValidateEmail(uemail))
    {
    if(passid_validation(password,7))
    {
    if(allnumeric(uphone))
    {
    if(hallselect(uhall))
    {
    if(staff_typeselect(staff_type))
    {
    if(validsex(gender))
    {
    }
    }
    } 
    } 
    }
    }
    }
    }
    }
    }
    return false;
}

function userid_validation(uid)
{
var uid_len = uid.value.length;
if (uid_len <= 0)
{
alert("Enter a valid Passcode");
uid.focus();
return false;
}
return true;
}

function passwordcheck(my,mx){
if(String(my)==String(mx)){
    return true;
}else{
    alert("Passwords do not match!");
    mx.focus();
    return false;
}
}

function passid_validation(password,my)
{
var password_len = password.value.length;
if (password_len == my ||password_len > my)
{
    return true;
}
    else{
    alert("Password should not be empty or length must be greater than "+my);
    passid.focus();
}
}

function allLetter(uname)
{ 
var letters = /^[A-Za-z]+$/;
if(uname.value.match(letters))
{
return true;
}
else
{
alert('Name must have alphabet characters only');
uname.focus();
return false;
}
}

function allLetters(uname1)
{ 
var letters = /^[A-Za-z ]+$/;
if(uname1.value.match(letters))
{
return true;
}
else
{
alert('Other Names must have alphabet characters only');
uname1.focus();
return false;
}
}

function hallselect(uhall)
{
if(uhall.value == "Default")
{
alert('Select your hall from the list');
uhall.focus();
return false;
}
else
{
return true;
}
}

function staff_typeselect(staff_type)
{
if(staff_type.value == "Default")
{
alert('Select your hall from the list');
staff_type.focus();
return false;
}
else
{
return true;
}
}

function allnumeric(uphone)
{ 
var numbers = /^[0-9]+$/;
if(uphone.value.match(numbers))
{
return true;
}
else
{
alert('Phone number must have numeric characters only');
uphone.focus();
return false;
}
}
function ValidateEmail(uemail)
{
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
if(uemail.value.match(mailformat))
{
return true;
}
else
{
alert("You have entered an invalid email address!");
uemail.focus();
return false;
}
} function validsex(gender)
{
x=0;

if(gender.checked) 
{
x++;
}
if(x==0)
{
alert('Select Male/Female');
gender.focus();
return false;
}
else
{
alert('Form Succesfully Submitted');
window.location.reload()
return true;
}
}