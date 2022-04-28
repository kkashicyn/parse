
        function search(query) {
           
            $.ajax({
                url: "data",
                type: "GET",
                data: {query: query},
                dataType: "json",
                success: function(data){
                    $(".container").empty();
                    $("table").empty();
                    $.each(data['reviews'], function(i, item){ 
                         
                        var review_container = ''; 
                        $.each(item['reviews'], function(i, review){
                            review_container = review_container + review + '<br><br>';
                        });                        
                        $tr = $("<tr><td class='title'>"+item['title']+"</td><td class='country'>"+item['country']+"</td><td class='review'>"+review_container+"</td></tr>");                                                
                        $(".reviews_table").append($tr);

                    });   
                    
                    
                    $.each(data['marks'], function(i, item){                                          
                        $tr = $("<tr><td class='title'>"+item['title']+"</td><td class='marks'>"+item.rank+"</td></tr>");                                                
                        $(".marks_table").append($tr);
                      
                    });                     
                }
            });
        }


        
        $(document).ready(function(){
            search();  

            $("#search").on("keyup", function(){
                search($(this).val());
            });            

            var copyBtn = document.querySelector('#copy_btn');
            copyBtn.addEventListener('click', function () {
              var urlField = document.querySelector('#table1');                       
              var range = document.createRange();              
              range.selectNode(urlField);            
              window.getSelection().addRange(range);                             
              document.execCommand('copy');
            }, false);

            var copyBtn = document.querySelector('#copy_btn2');
            copyBtn.addEventListener('click', function () {
              var urlField = document.querySelector('#table2');                       
              var range = document.createRange();              
              range.selectNode(urlField);            
              window.getSelection().addRange(range);                             
              document.execCommand('copy');
            }, false);

            

        });


   


