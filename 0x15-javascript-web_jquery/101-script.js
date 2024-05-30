// JavaScript script that adds, removes and clears LI elements from
// a list when the user clicks:

$(function() {
    var addItem = $('#add_item');
    var removeItem = $('#remove_item');
    var clearList = $('#clear_list');
    var newItem = '<li>Item</li>';

    $(addItem).click(function () {
        $('UL.my_list').append(newItem);
    });

    $(removeItem).click(function () {
        $('UL.my_list li:last').remove();
    });

    $(clearList).click(function () {
        $('UL.my_list').empty(newItem);
    });
});
