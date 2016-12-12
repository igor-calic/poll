(function(angular) {
    'use strict';

    var module = angular.module('app.controllers');

    module.controller('HomeCtrl', [ '$scope', 'HomeService', function($scope, HomeService) {
        $scope.data = {};
        $scope.data.cb1 = true;
        $scope.data.cb2 = false;
        $scope.data.cb3 = false;
        $scope.data.cb4 = false;
        $scope.data.cb5 = false;
        $scope.data.submitDisabled = true;

        $scope.data.answers = []

        $scope.data.user = currentUser;

        $scope.toggle = function (answerId) {
            var idx = $scope.data.answers.indexOf(answerId);
            if (idx == -1) {
                $scope.data.answers.push(answerId);
            } else {
                $scope.data.answers.splice(idx, 1);
            }
        };

        $scope.isSelected = function (answerId) {
            return $scope.data.answers.indexOf(answerId) > -1;
        }

        $scope.selected = function(num) {
            return num == 1;
        }

        var init = function() {
            HomeService.Questions.query().$promise.then(function(questions) {
                $scope.data.questions = questions.items
                console.log('questions=', questions.items);
                return HomeService.UserAnswers.query({userId:currentUser.key}).$promise

            })
            .then(function(userAnswers) {
                console.log('userAnswers=',userAnswers.items )
                var answers = userAnswers.items
                $scope.data.answers = []
                if (answers) {
                    for (var i = 0 ; i < answers.length; i++) {
                        $scope.data.answers.push(answers[i].key.urlsafe)
                    }
                }
                $scope.data.submitDisabled = false;

            });
        }

        var save = function() {
            $scope.data.submitDisabled = true;
            var userAnswers = new HomeService.UserAnswers({userId:currentUser.key});
            userAnswers.answers = $scope.data.answers;
            var answer = userAnswers.$save(function() {
                console.log('answer=', answer)
                $scope.data.submitDisabled = false;
            })
        }

        $scope.save = save;

        init();
    }]);
})(window.angular);