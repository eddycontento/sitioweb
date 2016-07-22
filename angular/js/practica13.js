var app = angular.module("app",["ngResource"]);

app.controller('controlador', function($scope,materia,alumno){
	$scope.enviar=true;
  	$scope.formulario=true;
  	$scope.informacion=true;
	$scope.materia1=materia.get();
	$scope.alumno1=alumno.get();
	var bandera=false;
	$scope.validarAlumno = function(){
		var bandera=false;
    	for (var i = 0; i < $scope.alumno1.length; i++) {
    		//alert("ccd");
    		
    		if ($scope.buscarAlumno==$scope.alumno1[i].cedula) {
    			$scope.cedulaAux=$scope.alumno1[i].cedula;
    			bandera=true;
    			//alert("hola");
    			if (bandera) {
					$scope.formulario=false;
					$scope.listaMateria=true;
					$scope.informacion=false;
					$scope.nombres=$scope.alumno1[i].nombres;
					$scope.apellidos=$scope.alumno1[i].apellidos;
					$scope.correo=$scope.alumno1[i].correo;
					$scope.mensaje="Alumno esta registrado, con Cedula: ";
					/*$scope.n="Nombre: ";
					$scope.c="Cedula: ";
					$scope.co="Correo: "; */   			
    			}
    		}else{
    			$scope.cedulaAux=$scope.buscarAlumno;
    			$scope.mensaje="el alumno no esta registrado, con Cedula: ";
    		}

    	}
  	}
  	//$scope.matricula = function(){

  	//}

	

		
	
	
});

app.factory('materia', ['$resource', function($resource){
	return $resource("http://127.0.0.1:8000/materia/",{},
		{get:{method:"GET",pararms:{},isArray:true}}); 
		
	}
]);

app.factory('alumno', ['$resource', function($resource){
	return $resource("http://127.0.0.1:8000/alumno/",{},
		{get:{method:"GET",pararms:{},isArray:true}}); 
		
	}
]);