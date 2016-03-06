var myApp = angular.module('shipper', ['ngRoute']);

var jobID = "123";

var LAT_PICK = 0;
var LONG_PICK = 0;
var LAT_DROP = 0;
var LONG_DROP = 0;
var ZOOM = 12;

myApp.config(function ($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl: 'static/temp/html/Main.html',
        controller: 'mainContrl'
    })

    .when('/unassigned', {
        templateUrl: 'static/temp/html/Unassigned.html',
        controller: 'unassignCntrl'
    })

    .when('/active', {
        templateUrl: 'static/temp/html/Active.html',
        controller: 'activeCntrl'
    })

    .when('/completed', {
        templateUrl: 'static/temp/html/Completed.html',
        controller: 'completedCntrl'
    })

    .when('/jobDetails', {
        templateUrl: 'static/temp/html/JobDetails.html',
        controller: 'detailsCntrl'
    })


    .when('/interests', {
        templateUrl: 'static/temp/html/Interests.html',
        controller: 'interestController'
    });
});



myApp.service('upload', function ($http) {
    this.post = function (file) {
        $http.post('/pdf', file);
    }
});

myApp.controller('mainContrl', function ($scope, $location) {
    $scope.onView = function (id,pickUp,dropLoc) {
        jobID = id;
        LAT_PICK = pickUp.coordinates[0];
        LONG_PICK = pickUp.coordinates[1];

        LAT_DROP = dropLoc.coordinates[0];
        LONG_DROP = dropLoc.coordinates[1];

        //        $(this).attr("jobid");
        //        alert("test "+jobID+"   "+id);
        $location.path('/jobDetails');

        //        Util.prototype.say("Success");


    }

});

myApp.controller('cntrl', function ($scope,$http) {

    $scope.allJobs = "";

    var postUsers = $http.get('http://127.0.0.1:8000/jobs/list/')
        postUsers.then(function(result) {
        $scope.allJobs = result.data;
});

    

    console.log("Test");

    $scope.tabs = [
    {
        title: 'home',
        url: 'one.tpl.html'
    }, {
        title: 'plus',
        url: 'two.tpl.html'
    }, {
        title: 'compass',
        url: 'three.tpl.html'
    }, {
        title: 'user',
        url: 'four.tpl.html'
    }
    ];

    $scope.currentTab = 'one.tpl.html';

    $scope.onClickTab = function (tab) {
        //        alert("click");
        $scope.currentTab = tab.url;
    }

    $scope.isActiveTab = function (tabUrl) {
        return tabUrl == $scope.currentTab;
    }


});

myApp.controller('homeControl', function ($scope) {


});

//exploreControl
myApp.controller('exploreControl', function ($scope) {

});



//interestController
myApp.controller('interestController', function ($scope) {

    $scope.card = {
        title: "card title",
        desc: "card desc card desc card desc card desc",

    };

});

//overlayCntrl



//unassignCntrl
myApp.controller('unassignCntrl', function ($scope, $location, $http) {

    $scope.unassignedJobs = "";

    var postUsers = $http.get('http://127.0.0.1:8000/jobs/pending/')
    postUsers.then(function(result) {
    console.log(result);
    $scope.unassignedJobs = result.data;
    console.log($scope.unassignedJobs);

    });
    });

myApp.controller('activeCntrl', function ($scope, $location, $http) {

    $scope.activeJobs = "";

    var postUsers = $http.get('http://127.0.0.1:8000/jobs/active/')
    postUsers.then(function(result) {
    $scope.activeJobs = result.data;

    });
    });

myApp.controller('completedCntrl', function ($scope, $location, $http) {

    $scope.completedJobs = "";

    var postUsers = $http.get('http://127.0.0.1:8000/jobs/complete/')
    postUsers.then(function(result) {
    $scope.completedJobs = result.data;

    });
    });


myApp.controller('detailsCntrl', function ($scope, $http) {
    $scope.jobDetail =""
    var postUsers = $http.get('http://127.0.0.1:8000/jobs/detail/'+jobID);
    postUsers.then(function(result) {
    $scope.jobDetail = result.data;
    });


    $scope.tabs = [{
        title: 'Job Detail',
        url: 'one.tpl.html'
        }, {
        title: 'Available Porters ',
        url: 'two.tpl.html'
        }];

    $scope.currentTab = 'one.tpl.html';

    $scope.onClickTab = function (tab) {
        $scope.currentTab = tab.url;
    }

    $scope.isActiveTab = function (tabUrl) {
        return tabUrl == $scope.currentTab;
    }

    $scope.allJobs = allJob_DATA;


});

myApp.directive('home', function () {
    return {
        templateUrl: "html/Home.html"
    };


});
myApp.directive('add', function () {
    return {
        templateUrl: "html/Add.html"
    };


});
myApp.directive('explore', function () {
    return {
        templateUrl: "html/Explore.html"
    };


});
myApp.directive('profile', function () {
    return {
        templateUrl: "html/Profile.html"
    };


});

//planSelector
myApp.directive('planSelector', function () {
    return {
        templateUrl: "html/Selector.html"
    };


});
//suggestion
myApp.directive('planSuggestion', function () {
    return {
        templateUrl: "html/Suggestion.html"
    };


});

myApp.directive('pageHeader', function () {
    return {
        templateUrl: "html/common/header.html"
    };


});

myApp.directive('pageFooter', function () {
    return {
        templateUrl: "html/common/footer.html"
    };


});

myApp.directive('gmap', function () {
    return {
        templateUrl: "html/GMap.html"
    };


});