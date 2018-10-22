/**
 * Created by calujord on 20/10/18.
 */


var app = angular.module('CfnApp', ["ui.bootstrap"])
    .controller('PageCtrl', function($scope, $locale, $http, $uibModal) {
        $scope.page=1;
        $scope.datos = {};
        $scope.go = function(page){
            console.log(page);
            $scope.page = page;
        };
        $scope.accion_index = function(){
            $scope.page = "index";
        }

        $scope.mostrar = function(url_pdf){
            $scope.url_pdf = url_pdf;
            $scope.m = $uibModal.open({
              templateUrl: "/static/template/modal-pdf.html",
              windowUrl: "/static/template/modal-pdf.html",
              controller: "ModalShowImageCtrl",
              scope: $scope
            });
        };
        $scope.cancel = function(result){
            $scope.m.close();
        };
        $scope.print_pdf = function(url){

        };
        $scope.guardar = function(){
            $http({
                method : "GET",
                url : "/guardar.json",
                params: $scope.datos,
            }).then(function mySuccess(response) {
                $scope.datos = {};
                $scope.go(3);
            }, function myError(response) {
                console.log(response);
                $scope.myWelcome = response.statusText;
            });
        };
        $scope.print_hola = function(url, url_page){
            var myWindow = window.open("/static/pdf/apoyo-productivo.pdf", "MsgWindow", "width=800,height=900");
            myWindow.print();
            myWindow.close();

        };

    }).controller("ModalShowImageCtrl", function () {
    });