var counter = 0;
var limit = 0;
function init() { 
  var saved = localStorage.getItem('savedPage');
  if (saved == null) {
    saved = 0;
    localStorage.setItem('savedPage', '0');
  }
  
  var pages = document.getElementsByClassName('page');
  for (var i = 0; i < pages.length; i++) {
    if (i == saved) {
      continue;
    }
    pages[i].style.display = 'none';
  }
  
  counter = parseInt(saved);
  limit = pages.length - 1;
}

function next() {
  var pages = document.getElementsByClassName('page');
  if (counter != limit) {
    pages[counter].style.display = 'none';
    counter++;
    pages[counter].style.display = 'inline';
    localStorage.removeItem('savedPage');
    localStorage.setItem('savedPage', counter.toString());
  }
}

function prev() {
  var pages = document.getElementsByClassName('page');
  if (counter != 0) {
    pages[counter].style.display = 'none';
    counter--;
    pages[counter].style.display = 'inline';
    localStorage.removeItem('savedPage');
    localStorage.setItem('savedPage', counter.toString());
  }
}
document.onkeydown=function(e){
  var code = e.keyCode;
  if (code == '39'){
    next();
  } else if (code == '37'){
    prev();
  }

}
