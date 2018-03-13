odoo.define('petstore.petstore', function (require) {
    "use strict";
    var Class = require('web.Class');
    var Widget = require('web.Widget');
    var core = require('web.core');
    var utils = require('web.utils');
    var _t = core._t;
    var _lt = core._lt;
    var QWeb = core.qweb;

    core.HomePage = Widget.extend({
        init: function(parent) {
            this._super(parent);
            console.log("Hello JS, I'm inside of init.");
        },
        template: "HomePageTemplate",
        start: function() {
            this.$el.append("<div>Hello dear Odoo user!</div>");
            var greeting = new core.GreetingsWidget(this);
            return greeting.appendTo(this.$el);
        }
    });

    core.GreetingsWidget = Widget.extend({
        init: function(parent) {
            this._super(parent);
        },
        start: function() {
            this.$el.append("<div>We are so happy to see you again in this menu!</div>");
        }
    });

    core.action_registry.add('petstore.homepage', core.HomePage);

});