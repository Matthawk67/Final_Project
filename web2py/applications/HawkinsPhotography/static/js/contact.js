// Contact JS
// This is the js for the default/contact.html view.
var app = function() {

    var self = {};

    var show_form = false;

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function(a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };

    // Enumerates an array.
    var enumerate = function(v) { var k=0; return v.map(function(e) {e._idx = k++;});};

    self.send_contact_info = function() {
        var sent_first_name = $("textarea#first").val();
        var sent_last_name = $("textarea#last").val();
        var sent_email = $("textarea#email").val();
        var sent_phone_number = $("textarea#phone").val();
        var sent_region_or_city = $("textarea#region").val();
        var sent_services = $("textarea#services").val();

        //console.log(sent_first_name);
        //console.log(sent_last_name);
        //console.log(sent_email);
        //console.log(sent_phone_number);
        //console.log(sent_region_or_city);
        //console.log(sent_services);

        if(sent_first_name === '' || sent_last_name === '' || sent_email === '' || sent_phone_number === '' || sent_region_or_city === '' || sent_services === ''){
            $(function() {
                $('#flasherror').delay(500).fadeIn('normal', function() {
                    $(this).delay(2500).fadeOut();
                });
        });
            return undefined
        }

        $.ajax({
            type: 'POST',
            url: send_contact_url,
            data: {
                first_name: sent_first_name,
                last_name: sent_last_name,
                email: sent_email,
                phone_number: sent_phone_number,
                region: sent_region_or_city,
                services: sent_services
            },
            dataType: "text",
    });
        $("textarea#first").val('');
        $("textarea#last").val('');
        $("textarea#email").val('');
        $("textarea#phone").val('');
        $("textarea#region").val('');
        $("textarea#services").val('');

        $(function() {
            $('#flash').delay(500).fadeIn('normal', function() {
            $(this).delay(2500).fadeOut();
        });
    });

  };


// Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            first_name: "",
            last_name: "",
            user_email: "",
            phone_number: "",
            region_or_city: "",
            services: ""
        },
        methods: {
            send_contact_info: self.send_contact_info,
        }

    });

    return self;
};

var APP = null;

// No, this would evaluate it too soon.
// var APP = app();

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});