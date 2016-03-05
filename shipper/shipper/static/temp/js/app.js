var myApp = angular.module('shipper', ['ngRoute']);

var jobID = "123";

var LAT = 12.9667;
var LONG = 77.5667;
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
    $scope.onView = function (id) {
        //        $(this).attr("jobid");
        //        alert("test "+jobID+"   "+id);
        $location.path('/jobDetails');

        //        Util.prototype.say("Success");


    }

});

myApp.controller('cntrl', function ($scope) {
    //    $scope.map = {
    //        center: {
    //            latitude: 45,
    //            longitude: -73
    //        },
    //        zoom: 8
    //    };

    //    $scope.currentJobID = "123";

//$scope.allJobs = allJob_DATA;

$scope.allJobs = "";
    // http://127.0.0.1:8000/jobs/list/
    $.getJSON( "http://127.0.0.1:8000/jobs/list/", function( data ) {
        

         var tempArray = JSON.parse(data);
  console.log(tempArray);
        $scope.allJobs = tempArray["features"];

        console.log($scope.allJobs);


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








//selectorCntrl
myApp.controller('unassignCntrl', function ($scope, $location) {

    $scope.unassignedJobs = [
    {
        title: "title1"
    }, {
        title: "title1"
    }, {
        title: "title1"
    }, {
        title: "title1"
    }, {
        title: "title1"
    }, {
        title: "title1"
    }
    ];

    //    alert("tst");
    //    $("#ex2").slider({});
    //    $("#ex3").slider({});
    //
    //    $(".date-picker").datepicker();

    $(".date-picker").on("change", function () {
        var id = $(this).attr("id");
        var val = $("label[for='" + id + "']").text();
        //$("#msg").text(val + " changed");
    });

    $scope.onNext = function () {
        alert("clicked");
        $location.path('/suggest');
    }



});


myApp.controller('detailsCntrl', function ($scope) {




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