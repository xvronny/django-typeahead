jQuery(function ($) {
    $("[tjs_config]:not([disabled])").each(function (i, element) {
        var $element = $(element), config = {};
        try {
            config = JSON.parse($element.attr('tjs_config'));
        }
        catch (x) { }
        var i = 0;
        var arguments = [];
        arguments.push(config.options);
        for (i = 0; i < config.datasets.length; ++i) {
            let dataset = config.datasets[i];
            dataset['source'] = eval(dataset.source);
            arguments.push(dataset);
        }
        $element.typeahead(...arguments);
    });
});
