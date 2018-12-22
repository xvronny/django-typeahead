jQuery(function ($) {
    var geonames = new Bloodhound({
      datumTokenizer: Bloodhound.tokenizers.whitespace,
      queryTokenizer: Bloodhound.tokenizers.whitespace,
      remote: {
        url: '/go/geonames/?q=%QUERY',
        wildcard: '%QUERY',
        transform: function (data) {        // we modify the prefetch response
          var newData = [];                 // here to match the response format
          data.forEach(function (item) {    // of the remote endpoint
            newData.push(item.name + ', ' + item.country_name);
          });
          return newData;
        }
      }
    });

    $(".typeahead").each(function (i, element) {
        var $element = $(element), data = {};
        $element.typeahead({
          hint: false,
          highlight: true,
          minLength: 1
        },
        {
          name: 'geonames',
          source: geonames
        });
    });
});
