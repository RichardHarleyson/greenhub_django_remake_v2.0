/**
 * Created by Валентин on 29.05.2018.
 */

// Модальное окно записи на тест драйв
$(document).ready(function(){
		$("#f1_test_drive").submit(function(){
			var form_data = $(this).serialize();
			$.ajax({
				url: $('#f1_test_drive').attr('action'),
				type: "POST",
				data: form_data,
				success: function(data) {
					$('form[id=f1_test_drive]').trigger('reset');
					tdfa();
				},
				// error: function(){ ... }
			});
			return false
		});
});

function tdfa(){
    $( "#tdfa" ).removeClass( "hidden" );
}

// Модальное окно записи для звонка
$(document).ready(function(){
    $("#call-me-form").submit(function() { //устанавливаем событие отправки для формы с id=form
        var form_data = $(this).serialize(); //собераем все данные из формы
        $.ajax({
            url: $('#call-me-form').attr('action'), //путь до php фаила отправителя
            type: "POST",
            data: form_data,
            success: function() {
                $('form[id=call-me-form]').trigger('reset');
                cma();
            },
						// error: function(){ ... }
        });
        return false;
    });
});

function cma(){
    $( "#cma" ).removeClass( "hidden" );
}

// Человек хочет машину
$(document).ready(function(){
    $('.iwantcarform').submit(function (){
        var form_data = $(this).serialize(); //собераем все данные из формы
        $.ajax({
            url: "https://greenhub.pro/php/iwantcar.php", //путь до php фаила отправителя
            type: "POST", //Метод отправки
            data: form_data,
            success: function(data) {
                $('form[class=iwantcarform]').trigger('reset');
                iwa();
            }
        });
        return false;
    });
});

function iwa(){
    $("#iwa" ).removeClass( "hidden" );
}

//Убираем все со страницы
$(document).ready(function(){
    $('.clear_page').css({'cursor': 'pointer'});
    $('.clear_page').on('click', function(){
        $('#vehicle_global').empty();
        if($(this).attr("id") == 'show_fine_vehs' || $(this).attr("id") == 'show_available'){
            var data = {todo: 'available', veh_state: 'fine'};
            $.ajax({url: "https://greenhub.pro/veh_todo.php", type: "POST", data: data}).done(function( html ) {
                $("#vehicle_global").append(html);
                $('.hit').hide();
                $('.carousel').carousel('pause');
            });
        }
		if($(this).attr("id") == 'show_salon'){
            var data = {todo: 'salon'};
            $.ajax({url:"https://greenhub.pro/veh_todo.php", type: "POST", data: data}).done(function(html){
                $("#vehicle_global").append(html);
                $('.carousel').carousel('pause');
            });
        }
        if($(this).attr("id") == 'show_comming'){
            var data = {todo: 'comming'};
            $.ajax({url:"https://greenhub.pro/veh_todo.php", type: "POST", data: data}).done(function(html){
                $("#vehicle_global").append(html);
                $('.carousel').carousel('pause');
            });
        }
        if($(this).attr("id") == 'show_comming'){
            var data = {todo: 'comming'};
            $.ajax({url:"https://greenhub.pro/veh_todo.php", type: "POST", data: data}).done(function(html){
                $("#vehicle_global").append(html);
                $('.carousel').carousel('pause');
            });
        }
    });
});

$(document).ready(function(){
    $('#load_photo_btn').on('click', function(){
        $('#vehicle_block').empty();
        $.ajax({
            url:"https://greenhub.pro/tmp/cms/cms_todo.php",
            type:"POST",
            data: {todo: 'load_photos'},
            success: function(res){
                $('#vehicle_block').append(res);
            }
        });
    });
});

$(document).on('click','.set-photo',function(){
    var veh_data = {veh_id: $(this).attr('data-vehicle-id'), photo_id: $(this).attr('data-photo-id')};
    $.ajax({
        url:"https://greenhub.pro/tmp/cms/cms_set_photo.php",
        type:"POST",
        data:veh_data,
        success:function(res){
            // alert(res);
            $(res).empty();
            var html = "<h4>Фото установлено</h4>";
            $(res).append(html);
        }
    });
});
