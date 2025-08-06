// Когда html документ готов (прорисован)
$(document).ready(function () {
    // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
    var successMessage = $("#jq-notification");

    // // Ловим собыитие клика по кнопке добавить в корзину
    $(document).on("click", ".add-to-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке корзины и берем оттуда значение
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Получаем id товара из атрибута data-good-id
        var good_id = $(this).data("good-id");

        // Из атрибута href берем ссылку на контроллер django
        var add_to_cart_url = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                good_id: good_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Сообщение
                successMessage.html(data.message);
                successMessage.addClass("show").fadeIn(400);
                // Через 3сек убираем сообщение
                setTimeout(function () {
                    successMessage.removeClass("show").fadeOut(400);
                }, 3000);

                // Обновляем количество товаров в корзине из ответа сервера
                if (data.cart_total_quantity !== undefined) {
                    goodsInCartCount.text(data.cart_total_quantity);
                } else {
                    // Fallback: increment by 1
                    cartCount++;
                    goodsInCartCount.text(cartCount);
                }

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },

            error: function (xhr, status, error) {
                console.log("Ошибка при добавлении товара в корзину:", error);
                console.log("Response:", xhr.responseText);

                // Show error message to user
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    successMessage.html(xhr.responseJSON.error);
                    successMessage.removeClass("alert-success").addClass("alert-danger").addClass("show");
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.removeClass("show").fadeOut(400);
                        successMessage.removeClass("alert-danger").addClass("alert-success");
                    }, 3000);
                }
            },
        });
    });

    // // Ловим собыитие клика по кнопке удалить товар из корзины
    $(document).on("click", ".remove-from-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке корзины и берем оттуда значение
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Получаем id корзины из атрибута data-cart-id
        var cart_id = $(this).data("cart-id");
        // Из атрибута href берем ссылку на контроллер django
        var remove_from_cart = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: remove_from_cart,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
            },
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Сообщение
                successMessage.html(data.message);
                successMessage.addClass("show").fadeIn(400);
                // Через 3сек убираем сообщение
                setTimeout(function () {
                    successMessage.removeClass("show").fadeOut(400);
                }, 3000);

                // Обновляем количество товаров в корзине из ответа сервера
                if (data.cart_total_quantity !== undefined) {
                    goodsInCartCount.text(data.cart_total_quantity);
                } else {
                    // Fallback: decrement by quantity deleted
                    cartCount -= data.quantity_deleted;
                    goodsInCartCount.text(Math.max(0, cartCount));
                }

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },

            error: function (xhr, status, error) {
                console.log("Ошибка при удалении товара из корзины:", error);
                console.log("Response:", xhr.responseText);

                // Show error message to user
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    successMessage.html(xhr.responseJSON.error);
                    successMessage.removeClass("alert-success").addClass("alert-danger").addClass("show");
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.removeClass("show").fadeOut(400);
                        successMessage.removeClass("alert-danger").addClass("alert-success");
                    }, 3000);
                }
            },
        });
    });

    // Количество товара - обработчики для увеличения/уменьшения
    // Обработчик события для уменьшения значения
    $(document).on("click", ".decrement", function () {
        // Берем ссылку на контроллер django из атрибута data-cart-change-url
        var url = $(this).data("cart-change-url");
        // Берем id корзины из атрибута data-cart-id
        var cartID = $(this).data("cart-id");
        // Ищем ближайший input с количеством
        var $input = $(this).closest(".input-group").find('input[type="text"]');
        // Берем значение количества товара
        var currentValue = parseInt($input.val());
        // Если количества больше одного, то только тогда делаем -1
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            // Запускаем функцию определенную ниже
            // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    // Обработчик события для увеличения значения
    $(document).on("click", ".increment", function () {
        // Берем ссылку на контроллер django из атрибута data-cart-change-url
        var url = $(this).data("cart-change-url");
        // Берем id корзины из атрибута data-cart-id
        var cartID = $(this).data("cart-id");
        // Ищем ближайший input с количеством
        var $input = $(this).closest(".input-group").find('input[type="text"]');
        // Берем значение количества товара
        var currentValue = parseInt($input.val());

        $input.val(currentValue + 1);

        // Запускаем функцию определенную ниже
        // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
            },
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                // Сообщение
                successMessage.html(data.message);
                successMessage.addClass("show").fadeIn(400);
                // Через 3сек убираем сообщение
                setTimeout(function () {
                    successMessage.removeClass("show").fadeOut(400);
                }, 3000);

                // Обновляем количество товаров в корзине из ответа сервера
                if (data.cart_total_quantity !== undefined) {
                    var goodsInCartCount = $("#goods-in-cart-count");
                    goodsInCartCount.text(data.cart_total_quantity);
                } else {
                    // Fallback: manual calculation
                    var goodsInCartCount = $("#goods-in-cart-count");
                    var cartCount = parseInt(goodsInCartCount.text() || 0);
                    cartCount += change;
                    goodsInCartCount.text(Math.max(0, cartCount));
                }

                // Меняем содержимое корзины
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (xhr, status, error) {
                console.log("Ошибка при изменении количества товара в корзине:", error);
                console.log("Response:", xhr.responseText);

                // Show error message to user
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    successMessage.html(xhr.responseJSON.error);
                    successMessage.removeClass("alert-success").addClass("alert-danger").addClass("show");
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.removeClass("show").fadeOut(400);
                        successMessage.removeClass("alert-danger").addClass("alert-success");
                    }, 3000);
                }
            },
        });
    }

    // Auto-hide notifications after 2 seconds
    $(".notification-toast").each(function (index) {
        var notification = $(this);
        if (notification.is(":visible")) {
            setTimeout(function () {
                notification.alert("close");
            }, 2000 + index * 200); // Stagger multiple notifications
        }
    });

    // Function to show dynamic notifications (for AJAX calls)
    window.showNotification = function (message, type = "success") {
        var notification = $("#jq-notification");
        var messageSpan = $("#jq-notification-message");
        var icon = notification.find("i");

        // Update notification class and icon based on type
        notification.removeClass("alert-success alert-danger alert-info alert-primary");
        icon.removeClass("fa-check-circle fa-exclamation-triangle fa-info-circle fa-bell");

        switch (type) {
            case "success":
                notification.addClass("alert-success");
                icon.addClass("fa-check-circle");
                break;
            case "error":
            case "danger":
                notification.addClass("alert-danger");
                icon.addClass("fa-exclamation-triangle");
                break;
            case "info":
                notification.addClass("alert-info");
                icon.addClass("fa-info-circle");
                break;
            default:
                notification.addClass("alert-primary");
                icon.addClass("fa-bell");
        }

        // Set message and show notification
        messageSpan.text(message);
        notification.fadeIn();

        // Auto-hide after 2 seconds
        setTimeout(function () {
            notification.alert("close");
        }, 2000);
    };

    // При клике по значку корзины открываем всплывающее(модальное) окно
    $("#modalButton").click(function () {
        $("#exampleModal").appendTo("body");

        $("#exampleModal").modal("show");
    });

    // Собыите клик по кнопке закрыть окна корзины
    $("#exampleModal .btn-close").click(function () {
        $("#exampleModal").modal("hide");
    });

    // Обработчик события радиокнопки выбора способа доставки
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});
