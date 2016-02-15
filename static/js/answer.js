$(function(){

	//点击答案选择
	$(".answer").click(function(){
		var post_url = $('#post_url').val();
		var aid = $(this).attr('aid');
		var next_url = $("#next_url").val();
		var csrf = $("input[name=csrfmiddlewaretoken]").val();
		$.post(post_url,{answer_id:aid,csrfmiddlewaretoken:csrf},function(res){
			if(res.status == 1){
				location.href=next_url;
			}
		},'json');
	});
});
