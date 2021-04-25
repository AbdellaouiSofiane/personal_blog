$(document).ready(function(){
	$('#submit').on('click', function(){
		let serializedData = $('#share-post').serialize();
		$.ajax({
			url : $('#share-post').data('url'),
			data : serializedData,
			type : 'post',
			success : function(response) {
				$('#share-post')[0].reset();
				$('#success-msg').html('Email successfully sent to ' + response.email)
			}
		})
	});
});