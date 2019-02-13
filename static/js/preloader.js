  // document.body.onload = function(){
      // setTimeout(function(){
          // var preloader = document.getElementsByClassName("loading-window");
          // if( !preloader.classList.contains('done') )
              // {
                  // preloader.classList.add('done');
              // }
      // }, 1000);
	// //var p = document.getElementsByClassName("loading-window");
  // }
  
  document.addEventListener("DOMContentLoaded", function(event) {
  // document.body.onload = function(){
	  setTimeout(function(){
	  document.getElementById('loaderArea').classList.add('done');
	  },1000);
  })