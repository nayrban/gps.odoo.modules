odoo.define('petstore.input', function (require) {
    "use strict";
    var Class = require('web.Class');
    var Widget = require('web.Widget');
    var core = require('web.core');
    var utils = require('web.utils');
    var _t = core._t;
    var _lt = core._lt;
    var QWeb = core.qweb;

    core.InputPage = Widget.extend({
        template: "InputTemplate",
        init: function(parent) {
            this._super(parent);
        },
        start: function() {
        }
    });


    core.action_registry.add('petstore.input', core.InputPage);

});