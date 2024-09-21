// $(document).ready(function() {
//     $(".customer-logos").slick({
//         slidesToShow: 6,
//         slidesToScroll: 1,
//         aotoplay: true,
//         autoplaySpeed: 1500,
//         arrows: false,
//         dots: false,
//         pauseOnHover:false,
//         responsive: [
//             {
//                 breakpoint:768,
//                 settings:{
//                     slidesToShow:4
//                 }
//             },
//             {
//                 breakpoint:520,
//                 settings:{
//                     slidesToShow:3
//                 }
//             }
//         ]
//     });
// });



  // const image = document.getElementById("d1");

  // image.addEventListener("click", function() {
  //   if (image.classList.contains("clicked")) {
  //     image.classList.remove("clicked"); // Remove the "clicked" class on the second click
  //   } else {
  //     image.classList.add("clicked"); // Add the "clicked" class on the first click
  //   }
  // });

  const slider = document.querySelector('.slider');
  let currentPosition = 0;

  function animateSlider() {
    currentPosition -= 200; // Adjust based on card width
    slider.style.transform = `translateX(${currentPosition}px)`;
    if (currentPosition <= -1200) {
      currentPosition = 0;
      slider.style.transform = 'translateX(0)';
    }
  }

  setInterval(animateSlider, 2000); // Adjust the interval as needed
