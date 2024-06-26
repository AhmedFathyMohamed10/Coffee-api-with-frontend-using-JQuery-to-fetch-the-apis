$(document).ready(function(){
    $('#fetch-coffees').click(function(){
        $.ajax({
            url: '/api/coffees/',
            method: 'GET',
            success: function(data) {
                $('#coffee-list').empty();
                data.forEach(function(coffee, index) {
                    let coffeeItem = `<li style="transition-delay: ${index * 0.1}s;">
                        <h3><a href="/menu/${coffee.id}/">${coffee.name}</a></h3>
                        <p>Description: ${coffee.description}</p>
                        <p>Price: ${coffee.price} $</p>`;
                    if (coffee.image) {
                        coffeeItem += `<img src="${coffee.image}" alt="${coffee.name}">`;
                    }
                    coffeeItem += `</li>`;
                    $('#coffee-list').append(coffeeItem);
                });

                // Add animation classes after appending the list items
                setTimeout(() => {
                    $('#coffee-list li').each(function(index) {
                        $(this).addClass('show');
                    });
                }, 100);
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    });
});


            