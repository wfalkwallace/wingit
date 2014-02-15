$( document ).ready(function() {

	window.setTimeout(function() {
		$(".alert").fadeTo(500, 0).slideUp(500, function(){
			$(this).remove(); 
		});
	}, 2000);

	$( 'input[name="roundtrip"]' ).click(function() {
		$("#returning-input").removeClass('hidden');
	});
	$( "#one-way-toggle" ).click(function() {
		$("#returning-input").addClass('hidden');
	});

});
