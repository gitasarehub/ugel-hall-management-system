function formValidation()
{
var uid = document.registration.userid;
var uname = document.registration.username;
var uname1 = document.registration.username1;
var passid = document.registration.passid;
var uadd = document.registration.address;
var uhall = document.registration.hall;
var uphone = document.registration.phoneNumber;
var uemail = document.registration.email;
var umsex = document.registration.msex;
var ufsex = document.registration.fsex; 
if(userid_validation(uid,8))
{
    if(allLetter(uname))
{
    if(allLetter(uname1))
    {
        if(ValidateEmail(uemail))
{
if(passid_validation(passid,7,12))
{
    if(allnumeric(uphone))
    {
if(alphanumeric(uadd))
{ 
if(hallselect(hall))
{

if(validsex(umsex,ufsex))
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
return false;

} function userid_validation(uid,mx,my)
{
var uid_len = uid.value.length;
if (uid_len == 0 || uid_len >= my || uid_len < mx)
{
alert("Enter a valid id ");
uid.focus();
return false;
}
return true;
}
function passid_validation(passid,mx,my)
{
var passid_len = passid.value.length;
if (passid_len == 0 ||passid_len >= my || passid_len < mx)
{
alert("Password should not be empty / length be between "+mx+" to "+my);
passid.focus();
return false;
}
return true;
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
function alphanumeric(uadd)
{ 
var letters = /^[0-9a-zA-Z]+$/;
if(uadd.value.match(letters))
{
return true;
}
else
{
alert('User address must have alphanumeric characters only');
uadd.focus();
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
} function validsex(umsex,ufsex)
{
x=0;

if(umsex.checked) 
{
x++;
} if(ufsex.checked)
{
x++; 
}
if(x==0)
{
alert('Select Male/Female');
umsex.focus();
return false;
}
else
{
alert('Form Succesfully Submitted');
window.location.reload()
return true;
}
}