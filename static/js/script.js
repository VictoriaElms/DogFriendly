function validate(){
    let name = 
        document.getElementById("name").value;
    let email =
        document.getElementById("email").value;
    let subjectTitle=
        document.getElementById("subjectTitle").value;
    let comments = 
        document.getElementById("comments").value;
    let error_message= 
        document.getElementById("error_message");

    error_message.style.padding = "10px";

    let errors = [];

    if (name.length <3) {
        errors.push("Please Enter a valid Name");}
    if (email.indexOf("@") == -1 || email.length < 6){
        errors.push("Please Enter a Valid Email");}
    if (subjectTitle.length < 5){
        errors.push("Please Enter a Correct Subject");}
    if (comments.length <= 30) {
        errors.push("Please Enter more than 40 Characters");}
    if (errors.length > 0){
        error_message.innerHTML = errors.join("<br>");
        return false;}
    else {
        alert("Form Submitted Successfully!");
        return true; }
     
    }
    
