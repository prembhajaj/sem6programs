$.ajax(
    {
        type: "POST",
        url: '../api/doctor/create.php',
        dataType: 'json',
        data: {
            name: $("#name").val(),
            email: $("#email").val(),        
            password: $("#password").val(),
            phone: $("#phone").val(),
            gender: $("input[name='gender']:checked").val(),
            specialist: $("#specialist").val()
        },
        error: function (result) {
            alert(result.responseText);
        },
        success: function (result) {
            if (result['status'] == true) {
                alert("Successfully Added New Doctor!");
                window.location.href = '/medibed/doctor';
            }
            else {
                alert(result['message']);
            }
        }
    });
