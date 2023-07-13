
//función en jquery que suma y multiplica dos números
  $(document).ready(function(){

    $("#sumar").click(function(){

        var a= parseInt($("#num1").val());
        var b= parseInt($("#num2").val());
        var suma=a+b;
        $("#resultado").val(suma);
    });

    $("#multiplicar").click(function(){
        var a= parseInt($("#num1").val());
        var b= parseInt($("#num2").val());
        var multi=a*b;
        $("#resultado").val(multi);

    });

});