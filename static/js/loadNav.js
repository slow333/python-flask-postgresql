async function loadMenu(){
   let responseNav = await fetch('/static/html/nav.html');
   let navText = await responseNav.text();
   let nav = document.createElement('nav');
   nav.classList.add('navbar');
   nav.innerHTML = navText;
   document.body.prepend(nav); 
      // highlight current url after nav is loaded
   const currentUrl = window.location.pathname;
   const navLinks = nav.querySelectorAll('a');
   navLinks.forEach(link => {
     if (link.getAttribute('href') === currentUrl) {
         link.classList.add('currentUrl');
         let parent = link.parentElement.parentElement.parentElement;
         parent.firstElementChild.classList.add('currentUrl');
         let parentA = link.parentElement.parentElement;
         // while (parentA && parentA.firstElementChild.tagName !== 'A') {
         //    console.log(parentA.firstElementChild.tagName);
         //   parentA = parentA.parentElement;
         // }
         // if (parentA) {
         // // parentA는 link의 상위 a 태그입니다.
         // parentA.classList.add('currentUrl');
         // }
      }
   });
}
loadMenu().catch(error => new Error(error.message));

// highlight current url
// document.addEventListener('DOMContentLoaded', function() {
//   const currentUrl = window.location.pathname;
//   console.log("Current URL:", currentUrl); // Debugging line
//   const navLinks = document.querySelectorAll('.navbar a');
//   navLinks.forEach(link => {
//     console.log("Checking link:", link.getAttribute('href')); // Debugging line
//     if (link.getAttribute('href') === currentUrl) {
//       link.classList.add('currentUrl');
//       console.log("Matched link:", link); // Debugging line
//     }
//   });
// });