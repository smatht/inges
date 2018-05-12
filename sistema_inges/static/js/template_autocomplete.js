$(document).ready(function() {
    var ALGOLIA_APPID = 'K6YI21FQ9O';
    var ALGOLIA_SEARCH_APIKEY = 'f58dcf6a99def4dd6d15c795136c0b9c';
    var ALGOLIA_INDEX_NAME = 'plant_pagos';
    var NB_RESULTS_DISPLAYED = 5;
    // #2- Algolia API Client Initialization
    var algoliaClient = new algoliasearch(ALGOLIA_APPID, ALGOLIA_SEARCH_APIKEY);
    var index = algoliaClient.initIndex(ALGOLIA_INDEX_NAME);
    var lastQuery = '';
    var coment = document.getElementById('id_comentario');
    console.log(coment);
    $(coment).textcomplete([
      {
        // #3 - Regular expression used to trigger the autocomplete dropdown
        match: /(^|\s)#(\w*(?:\s*\w*))$/,
        // #4 - Function calbenled at every new keystroke
        search: function(query, callback) {
          lastQuery = query;
          index.search(lastQuery, { hitsPerPage: NB_RESULTS_DISPLAYED })
            .then(function searchSuccess(content) {
              if (content.query === lastQuery) {
                callback(content.hits);
              }
            })
            .catch(function searchFailure(err) {
              console.error(err);
            });
        },
        // #5 - Template used to display each result obtained by the Algolia API
        template: function (hit) {
          // Returns the highlighted version of the name attribute
          return hit.desc;
        },
        // #6 - Template used to display the selected result in the textarea
        replace: function (hit) {
          return hit.desc.trim() + ' ';
        }
      }
    ], {
//      footer: '&lt;div style="text-align: center; display: block; font-size:12px; margin: 5px 0 0 0;"&gt;Powered by &lt;a href="http://www.algolia.com"&gt;&lt;img src="https://www.algolia.com/assets/algolia128x40.png" style="height: 14px;" /&gt;&lt;/a&gt;&lt;/div&gt;'
    });
});