/*-----------------------------------------------------------------------------------

    Template Name: Balloons and Party Decoration HTML Template


    Note: This is Custom Js file

-----------------------------------------------------------------------------------

    [Table of contents]

    1. PRELOADER
    2.  slider-home-1
    3.  slider-home-2
    4.  review-slider
    5. balloon-slider
    6. balloon-slider
    7. feedback-slider
    8. weekly-hot-slider
    9. mobile-nav
    10. Cart Popup Start
    11. scrollTop
    12. pd-gallery
    13. accordion-item

-----------------------------------------------------------------------------------*/


// 1. PRELOADER
if ($("body")[0]) {
  $(window).on('load', function() {
    $("body").addClass("page-loaded");
  });
}

jQuery(document).ready(function($){
    if ( $.isFunction($.fn.owlCarousel) ) {
// 2.  slider-home-1


    $('.slider-home-1').owlCarousel({
        loop:true,
        arrows:false,
        autoplay:true,
        autoplayTimeout:4000,
        items:1
      })

// 3.  slider-home-2

    $('.slider-home-2').owlCarousel({
        loop:true,
        arrows:false,
        dot:true,
        autoplay:true,
        autoplayTimeout:4000,
        items:1
      })

// 4.  review-slider

    $('.review-slider').owlCarousel({
        loop:true,
        dot:false,
        arrows:true,
        autoplay:true,
        autoplayTimeout:4000,
        items:1,
        animateIn: 'fadeIn',
        animateOut: 'fadeOut',
        navText: ["<i class='fa-solid fa-angle-left'></i>","<i class='fa-solid fa-angle-right'></i>"],
      })

// 5. balloon-slider

    $('.balloon-slider').owlCarousel({
    loop:true,
    dot:true,
    nav:false,
    autoplay:true,
    autoplayTimeout:3000,
    responsive:{
        0:{
            items:1
        },
        480:{
            items:1
        },
        800:{
            items:2
        },
        1000:{
            items:3
        },
        1200:{
            items:4
        }
      }
    })

// 6. balloon-slider

    $('.product-slider').owlCarousel({
    loop:true,
    dot:true,
    nav:false,
    autoplay:true,
    autoplayTimeout:3000,
    responsive:{
        0:{
            items:1
        },
        800:{
            items:2
        },
        1000:{
            items:3
        },
        1200:{
            items:4
        },
        1400:{
            items:5
        }
      }
    })

// 7. feedback-slider

    $('.feedback-slider').owlCarousel({
    loop:true,
    dot:true,
    nav:false,
    autoplay:true,
    autoplayTimeout:3000,
    responsive:{
        0:{
            items:1
        },
        1000:{
            items:2
        },
        1200:{
            items:3
        }
      }
    })

// 8. weekly-hot-slider

    $('.weekly-hot-slider').owlCarousel({
    loop:true,
    dot:true,
    nav:false,
    autoWidth:true,
    autoplay:true,
    autoplayTimeout:3000,
    responsive:{
        0:{
            items:1
        },
        1200:{
            items:2
        }
      }
    })

    }

/* 9. mobile-nav */
        jQuery('.mobile-nav .menu-item-has-children').on('click', function($) {

          jQuery(this).toggleClass('active');

        }); 

        jQuery('#nav-icon4').on('click', function($){

            jQuery('#mobile-nav').toggleClass('open');

        });

        jQuery('#res-cross').on('click', function($){

           jQuery('#mobile-nav').removeClass('open');

        });


        jQuery('.bar-menu').on('click', function($){

            jQuery('#mobile-nav').toggleClass('open');
            jQuery('#mobile-nav').toggleClass('hmburger-menu');
            jQuery('#mobile-nav').show();

        });

        jQuery('#res-cross').on('click', function($){

           jQuery('#mobile-nav').removeClass('open');

        });
  
}) ;

/* 10. Cart Popup Start */

    jQuery('.pr-cart').on('click', function() {

      jQuery('.cart-popup').toggleClass('show-cart');

    });

// Cart Popup End

// 11. scrollTop

function inVisible(element) {
  var WindowTop = $(window).scrollTop();
  var WindowBottom = WindowTop + $(window).height();
  var ElementTop = element.offset().top;
  var ElementBottom = ElementTop + element.height();
  //animating the element if it is
  //visible in the viewport
  if ((ElementBottom <= WindowBottom) && ElementTop >= WindowTop)
    animate(element);
}

function animate(element) {
  //Animating the element if not animated before
  if (!element.hasClass('ms-animated')) {
    var maxval = element.data('max');
    var html = element.html();
    element.addClass("ms-animated");
    $({
      countNum: element.html()
    }).animate({
      countNum: maxval
    }, {
      //duration 5 seconds
      duration: 5000,
      easing: 'linear',
      step: function() {
        element.html(Math.floor(this.countNum) + html);
      },
      complete: function() {
        element.html(this.countNum + html);
      }
    });
  }

}

//When the document is ready
$(function() {
  //This is triggered when the
  //user scrolls the page
  $(window).scroll(function() {
    //Checking if each items to animate are 
    //visible in the viewport
    $("h2[data-max]").each(function() {
      inVisible($(this));
    });
  })
});



const items = document.querySelectorAll(".items");

for (let i = 0; i < items.length; i++) {
  items[i].addEventListener("click", function () {
    this.classList.toggle("open");
  });
}


/* 12. pd-gallery */

    $('.li-pd-imgs').on('click', function() {

      var img_src = "";

      $('.li-pd-imgs.nav-active').removeClass('nav-active');

      $(this).addClass('nav-active');

      img_src = $(this).find('img').attr('src');

      $('.pd-main-img').children('img').attr('src', img_src);

    });

/* 13. accordion-item */


$('.accordion-item .heading').on('click', function(e) {
    e.preventDefault();

    if($(this).closest('.accordion-item').hasClass('active')) {
        $('.accordion-item').removeClass('active');
    } else {
        $('.accordion-item').removeClass('active');

        $(this).closest('.accordion-item').addClass('active');
    }
    var $content = $(this).next();
    $content.slideToggle(100);
    $('.accordion-item .content').not($content).slideUp('fast');
});

function inVisible(element) {
  //Checking if the element is
  //visible in the viewport
  var WindowTop = $(window).scrollTop();
  var WindowBottom = WindowTop + $(window).height();
  var ElementTop = element.offset().top;
  var ElementBottom = ElementTop + element.height();
  //animating the element if it is
  //visible in the viewport
  if ((ElementBottom <= WindowBottom) && ElementTop >= WindowTop)
    animate(element);
}

function animate(element) {
  //Animating the element if not animated before
  if (!element.hasClass('ms-animated')) {
    var maxval = element.data('max');
    var html = element.html();
    element.addClass("ms-animated");
    $({
      countNum: element.html()
    }).animate({
      countNum: maxval
    }, {
      //duration 5 seconds
      duration: 5000,
      easing: 'linear',
      step: function() {
        element.html(Math.floor(this.countNum) + html);
      },
      complete: function() {
        element.html(this.countNum + html);
      }
    });
  }

}

//When the document is ready
$(function() {
  //This is triggered when the
  //user scrolls the page
  $(window).scroll(function() {
    //Checking if each items to animate are 
    //visible in the viewport
    $("h2[data-max]").each(function() {
      inVisible($(this));
    });
  })
});

let calcScrollValue = () => {
  let scrollProgress = document.getElementById("progress");
  let progressValue = document.getElementById("progress-value");
  let pos = document.documentElement.scrollTop;
  let calcHeight =
    document.documentElement.scrollHeight -
    document.documentElement.clientHeight;
  let scrollValue = Math.round((pos * 100) / calcHeight);
  if (pos > 100) {
    scrollProgress.style.display = "grid";
  } else {
    scrollProgress.style.display = "none";
  }
  scrollProgress.addEventListener("click", () => {
    document.documentElement.scrollTop = 0;
  });
  scrollProgress.style.background = `conic-gradient(#672b83 ${scrollValue}%, #d7d7d7 ${scrollValue}%)`;
};

window.onscroll = calcScrollValue;
window.onload = calcScrollValue;
