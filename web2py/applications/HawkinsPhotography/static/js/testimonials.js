// Testimonials JS
// This is the js for the default/index.html view.
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

    self.add_rating = function () {
        // We disable the button, to prevent double submission.
        $.web2py.disableElement($("#add-post"));
        var sent_rating = self.vue.num_stars;
        var sent_content = self.vue.form_content;
        console.log(sent_rating);
        $.post(add_rating_url,
            // Data we are sending.
            {
                post_author: current_user_email,
                post_rating: sent_rating,
                post_content: sent_content
            },
            // What do we do when the post succeeds?
            function (data) {
                // Re-enable the button.
                $.web2py.enableElement($("#add-post"));
                // Clears the form.
                self.vue.num_stars = 0;
                self.vue.form_content = "";
                // Adds the post to the list of posts.
                var new_post = {
                    id: data.post_id,
                    post_author: current_user_email,
                    post_rating: sent_rating,
                    post_content: sent_content
                };
                self.vue.rating_list.unshift(new_post);
                // We re-enumerate the array.
                self.process_posts();
            });
        // If you put code here, it is run BEFORE the call comes back.
    };

    self.get_ratings = function() {
        $.getJSON(get_rating_list_url,
            function(data) {
                self.vue.rating_list = data.rating_list;
                self.process_posts();
                console.log("I got my list");
            }
        );
        console.log("I fired the get");
    };

    self.process_posts = function() {
        enumerate(self.vue.rating_list);
        self.vue.rating_list.map(function (e) {
             Vue.set(e, 'editing', false);
        });
    };

    self.set_editing = function(post_idx) {
        var p = self.vue.rating_list[post_idx];
        p.editing = true;
    };

    self.submit_rating = function(rating_idx) {
        var p = self.vue.rating_list[rating_idx];
        var sent_rating = p.post_rating;
        var sent_content = $("textarea#newtext").val();
        $.post(edit_rating_url,
            {
                rating_id: self.vue.rating_list[rating_idx].id,
                post_rating: sent_rating,
                post_content: sent_content
            }
            );
        p.editing = false;
    };

    self.edit_stars = function(rating_idx, star_idx){
        var p = self.vue.rating_list[rating_idx];
        p.post_rating = star_idx;
    };

    self.set_stars = function(star_idx) {
        // The user has set this as the number of stars for the post.
        self.vue.num_stars = star_idx;
    };

    self.delete_rating = function(rating_idx) {
        var p = self.vue.rating_list[rating_idx];
        $.post(delete_rating_url,
            {
                rating_id: self.vue.rating_list[rating_idx].id,
            }
            );
        self.vue.rating_list.splice(rating_idx, 1);
        self.process_posts();
        p.editing = false;
    };

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            form_rating: "",
            form_content: "",
            rating_list: [],
            current_user_email: current_user_email,
            star_indices: [1, 2, 3, 4, 5],
            num_stars: 0,
        },
        methods: {
            add_rating: self.add_rating,
            set_editing: self.set_editing,
            submit_rating: self.submit_rating,
            get_ratings: self.get_ratings,
            delete_rating: self.delete_rating,

            stars_out: self.stars_out,
            stars_over: self.stars_over,
            set_stars: self.set_stars,
            edit_stars: self.edit_stars,
        },
    });

    // If we are logged in, shows the form to add posts.
    if (is_logged_in) {
        $("#add_post").show();
    }

    // Gets the posts.
    self.get_ratings();

    return self;
};

var APP = null;

// No, this would evaluate it too soon.
// var APP = app();

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});