$(function(){
            //alert("Holaa");
            var_id =$("#usuario_id").attr("value");
            //alert("hola"+var_id);
            $.ajax({
                data: {'id' : var_id},
                url: '/consulta-evolucion-ajax',
                type: 'get',
                success: function(data){
                    //alert("hola"+data[0].fields.peso);
                    var dataSource = [];
                    var dataSource1 = [];
                    var dataSource2 = [];
                                for (var i = 0; i < data.length; i++) {

                                    //alert(data[i].fields.peso)

                                    
                                    dataSource.push({ state:data[i].fields.created, peso: data[i].fields.peso});
                                    dataSource1.push({ state:data[i].fields.created, pecho: data[i].fields.pecho, cintura: data[i].fields.cintura, cadera: data[i].fields.gluteos, hombro: data[i].fields.hombro});
                                    dataSource2.push({ state:data[i].fields.created, brazo: data[i].fields.brazo, antebrazo: data[i].fields.antebrazo, pierna: data[i].fields.pierna, pantorrillas: data[i].fields.pantorrillas});
                                    
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
                    ],
                    title: "Peso",
                    legend: {
                        verticalAlignment: "bottom",
                        horizontalAlignment: "center"
                    },
                    pointClick: function (point) {
                        this.select();
                    }
                }); 

            ///tronco////////

                $("#chartContainer2").dxChart({
                    dataSource: dataSource1,
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
                        { valueField: "pecho", name: "Pectoral" },
                        { valueField: "cintura", name: "Cintura" },
                        { valueField: "cadera", name: "Cadera" },
                        { valueField: "hombro", name: "Hombro" },
                    ],
                    title: "Tronco",
                    legend: {
                        verticalAlignment: "bottom",
                        horizontalAlignment: "center"
                    },
                    pointClick: function (point) {
                        this.select();
                    }
                });

            //extemidades
                $("#chartContainer3").dxChart({
                    dataSource: dataSource2,
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
                        { valueField: "brazo", name: "Brazo" },
                        { valueField: "antebrazo", name: "Antebrazo" },
                        { valueField: "pierna", name: "Pierna" },
                        { valueField: "pantorrillas", name: "Pantorrilla" },
                    ],
                    title: "Extremidades",
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
