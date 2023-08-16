$(function ($){
    $('#form_ajaxL').submit(function (e){
        e.preventDefault()
        console.log('Form action:', this.action);
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',

            success: function (response){
                console.log('ok  -',response)

                window.location.reload()
            },
            error:function (response){
                console.log('err  -',response)
                if (response.status === 400){
                    $('.alert-danger').text(response.responseJSON.error).removeClass('d-none')
                }
            }
        })
    })
})
$(function () {
    $('#form_ajaxR').submit(function (e) {
        e.preventDefault();
        console.log('Form action:', this.action);
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                console.log('ok  -', response);
                window.location.reload()
            },
            error: function (xhr, status, error) {
                console.log('err  -', xhr.responseJSON);
                if (xhr.status === 400) {
                    $('.alert-danger').text(xhr.responseJSON.error).removeClass('d-none');
                }
            }
        });
    });
});
$(function ($){
    $('#form_ajaxRS').submit(function (e){
        e.preventDefault()
        console.log('Form action:', this.action);
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',

            success: function (response){
                console.log('ok  -',response)

                window.location.href = '/'
            },
            error:function (response){
                console.log('err  -',response)
                if (response.status === 400){
                    $('.alert-danger').text(response.responseJSON.error).removeClass('d-none')
                }
            }
        })
    })
})


const authModal = document.getElementById("auth");
const forgotPasswordModal = document.getElementById("forgotPasswordModal");
const toggleModalsButton = document.getElementById("toggleModalsButton");

toggleModalsButton.addEventListener("click", function() {
    authModal.classList.toggle("d-none");  // Переключаем видимость модального окна для авторизации
    forgotPasswordModal.classList.toggle("d-none"); // Переключаем видимость модального окна для восстановления пароля
});
