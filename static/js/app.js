$(document).ready(function() {
    $('#openSearch').click(function() {
        $('#searchField').toggleClass('hide slideInDown');
    });
    $('#searchClose').click(function() {
        $('#searchField').addClass('hide slideInDown');
    });

    $('#findServices').click(function() {
        $('#searchField').toggleClass('hide slideInDown');
    });
    // $('#searchClose').click(function() {
    //     $('#searchField').addClass('hide');
    // });
});