const anasayfaMainLeft   = document.querySelector(".anasayfa-main-left");
const hamburger          = document.querySelector(".hamburger");

hamburger.addEventListener("click", () =>{
    anasayfaMainLeft.classList.toggle("show");
});

const anasayfaMainRight = document.querySelector(".anasayfa-main-right");
const angleLeft         = document.querySelector(".angle-left");

angleLeft.addEventListener("click", () =>{
    anasayfaMainRight.classList.toggle("show");
});

$('#picker').datetimepicker({
    timepicker: false,
    datepicker: true,
    format: 'y-m-d',
    value: '2021-7-2',
    inline: true,
    disabledWeekDays: [5, 6]
});