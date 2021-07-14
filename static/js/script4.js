/* ==================SHOW SEARCH BOX ================= */

// $(document).ready(function() {
 
//     $(".fa-search").click(function() {
//        $(".input-group1").toggle();
//        $("input[type='text']").focus();
//      });
 
// });



/*==================== SHOW MENU ====================*/
const navLeftMenu = document.getElementById('left-menu'),
      navRightMenu = document.getElementById('right-menu'),
      navLeftToggle = document.getElementById('nav-toggle'),
      navRightToggle = document.getElementById('toggle-right')

/*===== MENU SHOW =====*/
/* Validate if constant exists */
if(navLeftToggle){
    navLeftToggle.addEventListener('click', () =>{
        navLeftMenu.classList.toggle('show-menu')
    })
}
if(navRightToggle){
    navRightToggle.addEventListener('click', () =>{
        navRightMenu.classList.toggle('show-menu')
    })
}

