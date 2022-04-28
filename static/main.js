
        function search(query) {
           
            $.ajax({
                url: "data",
                type: "GET",
                data: {query: query},
                dataType: "json",
                success: function(data){
                    $(".container").empty();

                    $.each(data, function(i, item){   

                        var $div = $("<div>", {"class": "row"});
                        var $title = $("<div>", {"class": "title col"});                        
                        var $country = $("<div>", {"class": "country col"});
                        $title.html(item.title);
                        $country.html(item.country);
                        $($div).append($title);
                        $($div).append($country);   
                    
                        $.each(item['reviews'], function(i, review){
                            
                            var $review = $("<div>", {"class": "review col"});
                            $review.html(review); 
                            $($div).append($review);
                        });
                        $(".container").append($div);
                      
                    });                  
                }
            });
        }


        $(document).ready(function(){
     
            search();  
            $("#search").on("keyup", function(){
                search($(this).val());
            });            
        });


   


