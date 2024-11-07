/*=============== SEARCH ===============*/
const searchButton = document.getElementById('search-button'),
    searchClose = document.getElementById('search-close'),
    searchContent = document.getElementById('search-content')

if (searchButton) {
    searchButton.addEventListener('click', () =>{
        searchContent.classList.add('show-search')
    })
}

if (searchClose) {
    searchClose.addEventListener('click', () =>{
        searchContent.classList.remove('show-search')
    })
}


/*=============== LOGIN ===============*/
const loginButton = document.getElementById('login-button'),
    loginClose = document.getElementById('login-close'),
    loginContent = document.getElementById('login-content')

if (loginButton) {
    loginButton.addEventListener('click', () =>{
        loginContent.classList.add('show-login')
    })
}

if (loginClose) {
    loginClose.addEventListener('click', () =>{
        loginContent.classList.remove('show-login')
    })
}

                // HOME SWIPER

                document.addEventListener('DOMContentLoaded', function () {
                    let swiperHome = new Swiper('.home__swiper', {
                      loop: true,
                      spaceBetween: 16,
                      grabCursor: true,
                      slidesPerView: 'auto',
                      centeredSlides: true, // Если нужно по центру
                      
                      navigation: {
                        nextEl: '.swiper-button-next',
                        prevEl: '.swiper-button-prev',
                      },
                      
                      autoplay: {
                        delay: 3000, // Время в миллисекундах между слайдами (3 секунды)
                        disableOnInteraction: false, // Продолжать автопрокрутку после взаимодействия с пользователем (например, после прокрутки вручную)
                      },
                      
                      breakpoints: {
                        1150: {
                          slidesPerView: 1,
                          centeredSlides: false, // Если не нужно центрировать на больших экранах
                        }
                      }
                    });
                  });

/*=============== FEATURED SWIPER ===============*/

document.addEventListener('DOMContentLoaded', function () {
    let swiperFeatured = new Swiper('.featured__swiper', {
      loop: true,
      spaceBetween: 16,
      grabCursor: true,
      slidesPerView: 'auto',
      centeredSlides: true, // Если нужно по центру
      
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      
      breakpoints: {
        1150: {
          slidesPerView: 4,
          centeredSlides: false, // Если не нужно центрировать на больших экранах
        }
      }
    });
  });


/*=============== NEW SWIPER ===============*/
document.addEventListener('DOMContentLoaded', function () {
  let swiperNew = new Swiper('.new__swiper', {
      loop: true,
      spaceBetween: 16,
      slidesPerView: 'auto',
      navigation: { // Добавляем навигацию
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
      },
      breakpoints: {
          1150: {
              slidesPerView: 3,
          }
      }
  });
});

/*=============== TESTIMONIAL SWIPER ===============*/

document.addEventListener('DOMContentLoaded', function () {
    let swiperTestimonial = new Swiper('.testimonial__swiper', {
      loop: true,
      spaceBetween: 16,
      grabCursor: true,
      slidesPerView: 'auto',
      centeredSlides: true, // Если нужно по центру
      
      breakpoints: {
        1150: {
          slidesPerView: 4,
          centeredSlides: false, // Если не нужно центрировать на больших экранах
        }
      }
    });
  });
/*=============== SHOW SCROLL UP ===============*/ 
const scrollUp = () => {
    const scrollUp = document.getElementById('scroll-up')

    this.scrollY >= 350 ? scrollUp.classList.add('show-scroll') : scrollUp.classList.remove('show-scroll')
}

window.addEventListener('scroll', scrollUp)

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

const scrollActive = () => {
    const scrollDown = window.scrollY

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight,
              sectionTop = current.offsetTop - 58,
              sectionId = current.getAttribute('id'),
              sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']')

        if(scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight) {
            sectionsClass.classList.add('active-link')
        } else {
            sectionsClass.classList.remove('active-link')
        }
    })
}

window.addEventListener('scroll', scrollActive)


/*=============== DARK LIGHT THEME ===============*/ 
const themeButton = document.getElementById('theme-button')
const darkTheme = 'dark-theme'
const iconTheme = 'ri-sun-line'

const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')

const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'ri-moon-line' : 'ri-sun-line'

// We validate if the user previously chose a topic
if (selectedTheme) {
    // If the validation is fulfilled, we ask what the issue was to know if we activated or deactivated the dark theme
    document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
    themeButton.classList[selectedIcon === 'ri-moon-line' ? 'add' : 'remove'](iconTheme)
}

// Activate / deactivate the theme manually with the button
themeButton.addEventListener('click', () => {
    // Add or remove the dark / icon theme
    document.body.classList.toggle(darkTheme)
    themeButton.classList.toggle(iconTheme)

    // We save the theme and the current icon that the user chose
    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})


/*=============== SCROLL REVEAL ANIMATION ===============*/

const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400,
    reset: true,
})

sr.reveal(`.home__data`, `.featured__container`, `.new__container`, `.testimonial__container`, `.footer`)
sr.reveal(`.services__card`, {interval: 100})
sr.reveal(`.discount__data`, {origin: 'left'})
sr.reveal(`.discount__images`, {origin: 'right'})


document.addEventListener('DOMContentLoaded', function () {
  const catalog = document.querySelector('.catalog');
  const dropdown = catalog.querySelector('.dropdown');

  catalog.addEventListener('mouseenter', function () {
      const catalogRect = catalog.getBoundingClientRect();
      const dropdownHeight = dropdown.offsetHeight;

      // Проверяем, достаточно ли места внизу экрана для выпадения вниз
      if (catalogRect.bottom + dropdownHeight > window.innerHeight) {
          dropdown.classList.add('upwards');
      } else {
          dropdown.classList.remove('upwards');
      }
  });
});


document.addEventListener("DOMContentLoaded", function() {
  // Находим все кнопки с классом "cart-btn"
  const cartButtons = document.querySelectorAll(".cart-btn");

  cartButtons.forEach(button => {
      button.addEventListener("click", function(event) {
          const bookId = this.getAttribute("data-book-id");
          
          // Отправка AJAX-запроса на добавление книги в корзину
          fetch(`/cart/add/${bookId}/`, {
              method: "GET", // Можно использовать POST, если изменить представление
              headers: {
                  "X-Requested-With": "XMLHttpRequest"
              }
          })
          .then(response => response.json())
          .then(data => {
              if (data.success) {
                  alert(data.message); // Сообщение о добавлении книги в корзину
              } else {
                  alert("Не удалось добавить книгу в корзину.");
              }
          })
          .catch(error => console.error("Ошибка:", error));
      });
  });
});