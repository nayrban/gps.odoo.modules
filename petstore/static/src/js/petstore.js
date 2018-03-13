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
        template: "HomePageTemplate",
        init: function(parent) {
            this._super(parent);
            this.name = "Mordecai";
        },
        start: function() {
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