
        function search(query) {
           
            $.ajax({
                url: "data",
                type: "GET",
                data: {query: query},
                dataType: "json",
                success: function(data){
                    $(".container").empty();

                    $.each(data['reviews'], function(i, item){   
                        var $div = $("<div>", {"class": "row mb-10"});
                        var $title = $("<div>", {"class": "title col-3"});                        
                        var $country = $("<div>", {"class": "country col-1"});
                        $title.html(item.title);
                        $country.html(item.country);
                        $($div).append($title);
                        $($div).append($country);   
                        var $reviews = $("<div>", {"class": "reviews col-8"});
                        var $reviews_row = $("<div>", {"class": "row"});
                        $reviews.append($reviews_row);
                        $.each(item['reviews'], function(i, review){
                            
                            var $review = $("<div>", {"class": "review col"});
                            $review.html(review); 
                            $($reviews_row).append($review);
                        });
                        $($div).append($reviews);
                        $(".reviews-container").append($div);
                      
                    });   
                    
                    
                    $.each(data['marks'], function(i, item){   
                        var $div = $("<div>", {"class": "row"});
                        var $title = $("<div>", {"class": "title col-3"});                        
                        $title.html(item.title);
                        $($div).append($title);
                        var $marks = $("<div>", {"class": "marks col-8"});
                        $marks.html(item.rank);                        
                        $($div).append($marks);
                        $(".marks-container").append($div);
                      
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


   


