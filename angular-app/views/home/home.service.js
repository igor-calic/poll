(function(angular) {
    'use strict';

    var module = angular.module('app.services');

    module.service('HomeService', [ '$resource', function($resource) {
        var factory = {}

        factory.Questions = $resource(
            '/api/questions/:key',
            {
                key: '@key'
            },
            {
                'query': {
                    method: 'GET',
                    isArray: false
                }
            }
        );

        factory.UserAnswers = $resource(
            '/api/user/:userId/answers',
                {userId:'@userId'},
                {
                    'query': {
                        method: 'GET',
                        isArray: false
                    }
                }
                );
        return factory;

    }]);
})(window.angular);