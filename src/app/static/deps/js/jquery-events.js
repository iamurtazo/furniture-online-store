// Когда html документ готов (прорисован)
$(document).ready(function () {
    // Auto-hide notifications after 2 seconds
    $('.notification-toast').each(function(index) {
        var notification = $(this);
        if (notification.is(':visible')) {
            setTimeout(function () {
                notification.alert('close');
            }, 2000 + (index * 200)); // Stagger multiple notifications
        }
    });
    
    // Function to show dynamic notifications (for AJAX calls)
    window.showNotification = function(message, type = 'success') {
        var notification = $('#jq-notification');
        var messageSpan = $('#jq-notification-message');
        var icon = notification.find('i');
        
        // Update notification class and icon based on type
        notification.removeClass('alert-success alert-danger alert-info alert-primary');
        icon.removeClass('fa-check-circle fa-exclamation-triangle fa-info-circle fa-bell');
        
        switch(type) {
            case 'success':
                notification.addClass('alert-success');
                icon.addClass('fa-check-circle');
                break;
            case 'error':
            case 'danger':
                notification.addClass('alert-danger');
                icon.addClass('fa-exclamation-triangle');
                break;
            case 'info':
                notification.addClass('alert-info');
                icon.addClass('fa-info-circle');
                break;
            default:
                notification.addClass('alert-primary');
                icon.addClass('fa-bell');
        }
        
        // Set message and show notification
        messageSpan.text(message);
        notification.fadeIn();
        
        // Auto-hide after 2 seconds
        setTimeout(function () {
            notification.alert('close');
        }, 2000);
    };

    // При клике по значку корзины открываем всплывающее(модальное) окно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Собыите клик по кнопке закрыть окна корзины
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обработчик события радиокнопки выбора способа доставки
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});