//Navbar component
Vue.component('navbar', {
    data: function() {
      return {
        items: [{
            label: 'Home',
            link: ''
          },
          {
            label: 'Contact Us',
            link: ''
          }
        ]
      }
    },
    template: '#navbar-template'
  });
  
  //Carousel
  Vue.component('main-content', {
    data: function() {
      return {
        headerText: 'Gamer Zone'
      }
    },
    template: '#main-content-template'
  });
  
  
  //Create Vue app
  var vm = new Vue({
    el: '#app'
  });
  