'use strict';

//angular.module('app.services', ['cs.utilities', 'ngResource']);
angular.module('app.services', ['ngResource']);
angular.module('app.controllers', ['app.services']);

angular.module('PollApp',['ngMaterial', 'ngMessages', 'material.svgAssetsCache', 'app.routes', 'app.services', 'app.controllers'])




/**
Copyright 2016 Google Inc. All Rights Reserved.
Use of this source code is governed by an MIT-style license that can be in foundin the LICENSE file at http://material.angularjs.org/license.
**/