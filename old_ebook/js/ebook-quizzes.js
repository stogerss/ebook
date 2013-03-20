function quiz(question) {
  if (document.getElementById(question + '_answer').checked) {
    document.getElementById(question + '_results').innerHTML = "That is correct!";
  } else {
    var choices = document.getElementsByName(question);
    for (var i = 0; i < choices.length; i++) {
      if (choices[i].checked) {
        var selected = choices[i].value;
        break;
      }
    }
    
    if (selected) {
      document.getElementById(question + '_results').innerHTML = "Sorry \"" + selected + "\" was incorrect.";
    } else {
      document.getElementById(question + '_results').innerHTML = "You have not selected anything.";
    }
    
  }
}
