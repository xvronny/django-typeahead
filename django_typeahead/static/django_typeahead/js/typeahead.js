jQuery(function ($) {
    $("[tjs_config]:not([disabled])").each(function (i, element) {
        var $element = $(element), arguments = {};
        try {
            arguments = JSON.parse($element.attr('tjs_config'));
        }
        catch (x) { }
        if (arguments.options && arguments.datasets) {
            $element.typeahead(arguments.options, arguments.datasets);
        }
    });
});
