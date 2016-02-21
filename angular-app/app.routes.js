(function(angular) {
    'use strict';

    var app = angular.module('app.routes', ['ngRoute']);

    app.config(['$routeProvider', function($routeProvider) {
        $routeProvider.

        when('/home', {

            templateUrl: '/ng/views/home/home.tpl.html',
            controller: 'HomeCtrl'
        }).

        otherwise({

            redirectTo: '/home'
        });
    }]);

})(window.angular);