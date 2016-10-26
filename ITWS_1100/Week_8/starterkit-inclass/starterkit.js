jQuery(document).ready(function() {

// #10 - shorthand for ready function
// $(function() {	


	// do something here
	// FIND ME: Using Selectors and Events

	// #1
	// $("#orderedlist").addClass("red");

	// #2
	// $("#orderedlist > li").addClass("blue");

	// #3
	$("#orderedlist  li:last").hover(function() {
		$(this).addClass("green");
	}, function() {
		$(this).removeClass("green");
	});


	// #4 (notice, like a for loop, it retrieves each of the list in orderedlist
	$("#orderedlist").find("li").each(function(i) {
	   $(this).append(" BAM! " + i);
	});
	
	// $4b
	// $("#orderedlist > li").append(" Wham! ");
	
	// // #5 - forms - reset first form
	// $("#reset").click(function() {
	// 	$("form")[0].reset();
	// });
	
	// #5b - reset all forms
	$("#reset").click(function() {
		$("form").each(function() {
			this.reset();
		});
	});
	
	// #6 - filter and not
	$("li").not(":has(ul)").css("border", "1px solid black");
	$("li").filter(":has(ul)").css("border", "5px dotted red");
	
	// #7pre - add background to all a tags
	$("a").css("background", "#9FF");

	// #7 - add background color to all anchors with a name attribute
	$("a[name]").css("background", "#eee");
	
	// #8 - FAQ next
	$('#faq').find('dd').hide().end().find('dt').click(function() {
		$(this).next().slideToggle();
	});
	
	// or like this
	// $('#faq dd').hide().end().find('dt').click(function() {
	// 	$(this).next().slideToggle();
	// });

  // #9 - operate on the parent of the selection
 	$("a").hover(function() {
		$(this).parents("p").addClass("highlight");
	}, function() {
		$(this).parents("p").removeClass("highlight");
	});
 
  // Extra - animate
	$('#orderedlist2 li').mouseover(function() {
	   $(this).animate({"height": 100}, "slow");
	});

	$('#orderedlist2 li').click(function() {
   $(this).animate({"height": 10}, "slow");
 });



});