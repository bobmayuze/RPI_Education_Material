/* Lab 5 JavaScript File 
   Place variables and functions in this file */



function validate(formObj) {
  // put your validation code here
  // it will be a series of if statements
  
  var text = ""
  if (formObj.firstName.value == "") {
    text += "You must enter a first name\n";
  }
  
  if (formObj.lastName.value == "") {
    text += "You must enter a last name\n";
  }
  if (formObj.title.value == "") {
    text += "You must enter a title\n";
  }
  
  if (formObj.org.value == "") {
    text += "You must enter an organization\n";
  }
  if (formObj.pseudonym.value == "") {
    text += "You must enter a nickname\n";
  }
  
  if (formObj.comments.value == "") {
    text += "You must enter a comment\n";
  }

  if (text == "") {
    return true;
  }
  else {
    alert(text);
  }
  var y = document.forms["addForm"].length;
  for (i = 1; i < y-1; i++) { 
    if (document.forms["addForm"][i].value == "") {
    document.forms["addForm"][i].focus() 
    return false
    }
  }

function cleanComments() {
	document.getElementById("comments").innerHTML = ""; 	
}

function alertName() {
	firstName = document.getElementById("firstName").value;
	lastName = document.getElementById("lastName").value;
	nickname = document.getElementById("pseudonym").value;
	alert(firstName +" "+ lastName + " is " + nickname);	
}
