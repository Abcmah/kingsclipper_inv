let sidebar = document.querySelector(".sidebar");
const dropdownMenu = document.querySelector(".dropdown-menu");
let sidebarBtn = document.querySelector(".sidebarBtn");
let searchBox = document.querySelector('.bx-search');

let logo = document.querySelector('.logo-image');
sidebarBtn.onclick = function() {
  sidebar.classList.toggle("active");
  if(sidebar.classList.contains("active")){
  sidebarBtn.classList.replace("bx-menu" ,"bx-menu-alt-right");
}else
  sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");

  
  
  
}

//-------------------------------------------------------------------------//
let card = document.querySelector('#tm');

function deterColor(colour){
    if(colour ==='lightgreen'){
       
        setColour(colour)
    }
    else if(colour ==='red'){
        setColour(colour)
    }
    else{
        setColour(colour)
    }
location.reload()
}
//set the color once the page has loaded if its available
window.addEventListener('load',() => {
    color = localStorage.getItem('lcolor')
    if(color!= null){
        render(color)
    }
    else{
        render('purple')
    }
})
function setColour(color){
    localStorage.setItem('lcolor',color)
    scolor = localStorage.getItem('lcolor')
    render(scolor)
}
function render(color){
    sidebar.style.backgroundColor = color;
    dropdownMenu.style.backgroundColor = color;
    card.style.backgroundColor = color;
    let bar = document.querySelector('#'+color);
    bar.style.height = 38 +'px'
    bar.style.width = 38 +'px'

}

//from denis ivy

const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}