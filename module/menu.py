from flask import render_template as render # type: ignore
def getMenu():
  return render('nav.html')


def getCurrentUrl():
  return '''
const currentUrl = window.location.pathname;
const nav = document.querySelector('.navbar');
const navLinks = nav.querySelectorAll('a');
navLinks.forEach(link => {
  if (link.getAttribute('href') === currentUrl) {
      link.classList.add('currentUrl');
      let parent = link.parentElement.parentElement.parentElement;
      parent.firstElementChild.classList.add('currentUrl');
  }
});  
  '''