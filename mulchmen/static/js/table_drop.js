$(function(){
    $(".dropdown-menu").on('click', 'a', function(){
        $(this).parents('.dropdown').find('button').text($(this).text());
    });
 });