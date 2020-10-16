const url_backend = 'http://127.0.0.1:' + PORT +'/information_cpu/get_information_cpu';
var limit_records;

$(function(){  
    get_info();
    $('#button_sort_asc').click(function(){
        sort_table_asc();
    });
    $('#button_sort_desc').click(function(){
        sort_table_desc();
    });
});

function get_info(){
    var url = url_backend;
    var timeout = 10000;
    var error_timeout = 'Внимание! Время ожидания ответа сервера истекло';
    var error_default = 'Внимание! Произошла ошибка, попробуйте отправить информацию еще раз';
    
    $.ajax({
        type: 'GET',
        url: url,
        dataType: 'JSON',
        timeout: timeout,
        success: function(data){
            print_limit_table(data);
            print_aggregated_tables(data);
            limit_records = data;
        },
        error: function(request, error){
            if (error == "timeout") {
                alert(error_timeout);
            }
            else {
                alert(error_default);
            }
        }
    });
}

function print_limit_table(data){
    $.each(data['limit_records'], function(key, value) {
        $('.table_last_limit_tbody').append('<tr>' + 
        '<td>' + value['id'] + '</td>' + 
        '<td>' + value['date_time'] + '</td>' + 
        '<td>' + value['load_cpu'] + '</td>' + 
        '</tr>');
    });
}

function print_aggregated_tables(data){
    $('.aggregated_table_last_limit').append('<tr>' + 
    '<td>' + data['aggregated_last_limit_min'] + '</td>' + 
    '<td>' + data['aggregated_last_limit_max'] + '</td>' + 
    '<td>' + data['aggregated_last_limit_avg'] + '</td>' + 
    '</tr>');
    $('.aggregated_table_all').append('<tr>' + 
    '<td>' + data['aggregated_all_min'] + '</td>' + 
    '<td>' + data['aggregated_all_max'] + '</td>' + 
    '<td>' + data['aggregated_all_avg'] + '</td>' + 
    '</tr>');
}

function sort_table_asc()
{
    console.log(limit_records['limit_records']);
    limit_records['limit_records'].sort(function(a, b) {
        return a.load_cpu - b.load_cpu;
    });
    $('.table_last_limit tbody').empty();
    print_limit_table(limit_records);
}

function sort_table_desc()
{
    console.log(limit_records['limit_records']);
    limit_records['limit_records'].sort(function(a, b) {
        return b.load_cpu - a.load_cpu;
    });
    $('.table_last_limit tbody').empty();
    print_limit_table(limit_records);
}