$(function(){
            
            var_id =$("#usuario_id").attr("value");
            //alert("hola"+var_id);
            $.ajax({
                data: {'id' : var_id},
                url: '/consulta-evolucion-ajax',
                type: 'get',
                success: function(data){
                    //alert("hola"+data[0].fields.peso);
                    
                    var dataSource = [];
                                for (var i = 0; i < data.length; i++) {

                                    //alert(data[i].fields.peso)
                                    
                                    dataSource.push({ state:data[i].fields.created, peso: data[i].fields.peso, pecho: data[i].fields.pecho, cintura: data[i].fields.cintura, cadera: data[i].fields.gluteos});
                                    
                                }

                    $("#chartContainer").dxChart({
                    dataSource: dataSource,
                    commonSeriesSettings: {
                        argumentField: "state",
                        type: "bar",
                        hoverMode: "allArgumentPoints",
                        selectionMode: "allArgumentPoints",
                        label: {
                            visible: true,
                            format: "fixedPoint",
                            precision: 0
                        }
                    },
                    series: [
                        { valueField: "peso", name: "Peso" },
                        { valueField: "pecho", name: "Pecho" },
                        { valueField: "cintura", name: "Cintura" },
                        { valueField: "cadera", name: "Cadera" },
                    ],
                    title: " Tu peso y tus medidas ",
                    legend: {
                        verticalAlignment: "bottom",
                        horizontalAlignment: "center"
                    },
                    pointClick: function (point) {
                        this.select();
                    }
                }); 

                }
            });
        });