(function() {
    window.SPX_CONF = {
        ptype: 1,
        retag_min_page_views: 2,
        
        regular_script: function() {
            // yandex metrics
            // GDN
        },
        
        retag_script: function() {
            // popunder            
            // advmaker
            // target mailru
            // VK retag
            // etc    
        }        
    };
    
     var s = document.createElement( 'script' );
     s.setAttribute( 'src', '//www.dmpcloud.net/spx/framework.js' );
     document.body.appendChild(s);
    
})()
