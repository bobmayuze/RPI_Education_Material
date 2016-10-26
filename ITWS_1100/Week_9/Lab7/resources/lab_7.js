$(document).ready(function() {  
  $.ajax({
   	 type: "GET",
   	 url: "lab7jsontemplate.json",
   	 dataType: "json",
   	 success: function(responseData, status){
   	  // var output = "<ul>";
      var output = ""  
     	$.each(responseData.menuItem, function(i, item) {
       	// output += '<h1>' + item.menuName + '</h1>';
        output += '<a href="'+ item.menuURL +'">'+ item.menuName + item.menuDesc +'</a></br>'
      });
      // output += "</ul>";
      $('#PleasePutThem').html(output);
    }
  });
});
