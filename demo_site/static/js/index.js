var Text = Backbone.Model.extend({
    urlRoot: "/api/text"
});

var Alert = Backbone.View.extend({
    el: '#alert-message',

    template: _.template($('#alert-template').html()),

    render: function() {
        this.$el.html(this.template(this.model.attributes));
    }
});

var AlertMessage = Backbone.Model.extend();

var TexterForm = Backbone.View.extend({
    el: '#texter-form',

    events: {
        "submit": "submit"
    },

    initialize: function (options) {
        this.alert = new Alert({model: new AlertMessage()});
    },

    submit: function (event) {
        event.preventDefault();
        var data = {};
        this.$el.serializeArray().forEach(function (e) {
            data[e.name] = e.value
        });

        var text = new Text(data);
        text.save(null, {
            success: _.bind(function(model, response) {
                this.alert.model.set({
                    'message': "Message Sent!",
                    'type': "success"
                });
                this.alert.render();
            }, this),
            error: _.bind(function(model, response) {
                this.alert.model.set({
                    'message': response.responseJSON.message,
                    'type': "danger"
                });
                this.alert.render();
            }, this)
        });
    }
});

(function() {
    new TexterForm();
})();
