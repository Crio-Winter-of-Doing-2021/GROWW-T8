var chatterbotUrl = '{% url "chatterbot" %}';
$(function () {
    var INDEX = 0;
    $("#chat-submit").click(function (e) {
        e.preventDefault();
        var msg = $("#chat-input").val();
        if (msg.trim() == "") {
            return false;
        }
        get_message(msg, "self");
        var buttons = [
            {
                name: "Existing User",
                value: "existing",
            },
            {
                name: "New User",
                value: "new",
            },
        ];
        setTimeout(function () {
            // generate_message(msg, "user");
            get_message(msg,"user");
        }, 1000);
    });

    // function generate_message(msg, type) {
    //     INDEX++;
    //     var str = "";
    //     str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg " + type + '">';
    //     str += '          <span class="msg-avatar">';
    //     str +=
    //         '            <img src="https://img.icons8.com/windows/32/000000/webcam-man.png"/>';
    //     str += "          </span>";
    //     str += '          <div class="cm-msg-text">';
    //     str += msg;
    //     str += "          </div>";
    //     str += "        </div>";
    //     $(".chat-logs").append(str);
    //     $("#cm-msg-" + INDEX)
    //         .hide()
    //         .fadeIn(300);
    //     if (type == "self") {
    //         $("#chat-input").val("");
    //     }
    //     $(".chat-logs")
    //         .stop()
    //         .animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
    // }

    function add_message(msg, type){
        INDEX++;
        var str = "";
        str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg " + type + '">';
        // str += '          <span class="msg-avatar">';
        // str +=
        //     '            <img src="https://img.icons8.com/windows/32/000000/webcam-man.png"/>';
        // str += "          </span>";
        str += '          <div class="cm-msg-text">';
        str += msg;
        str += "          </div>";
        str += "        </div>";
        $(".chat-logs").append(str);
        $("#cm-msg-" + INDEX)
            .hide()
            .fadeIn(300);
        if (type == "self") {
            $("#chat-input").val("");
        }
        $(".chat-logs")
            .stop()
            .animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
    }

    function get_message(msg,type) {
        if (type == 'self') {
            add_message(msg,type);
        }
        else {
            var inputData = {
                'text': msg
            }

            var $submit = $.ajax({
                type: 'POST',
                url: chatterbotUrl,
                data: JSON.stringify(inputData),
                contentType: 'application/json'
            });

            $submit.done(function(res) {
                add_message(res.text,type);
            });

            $submit.fail(function() {
                // TODO: Handle errors
            });
        }
    }

    function generate_button_message(buttons) {
        /* Buttons should be object array 
        [
          {
            name: 'Existing User',
            value: 'existing'
          },
          {
            name: 'New User',
            value: 'new'
          }
        ]
      */
        INDEX++;
        var btn_obj = buttons
            .map(function (button) {
                return (
                    '              <li class="button"><a href="javascript:;" class="btn btn-primary chat-btn" chat-value="' +
                    button.value +
                    '">' +
                    button.name +
                    "</a></li>"
                );
            })
            .join("");
        var str = "";
        // str += "<div id='cm-msg-" + INDEX + '\' class="chat-msg user">';
        // str += '          <span class="msg-avatar">';
        // str +=
        //     '            <img src="https://img.icons8.com/windows/32/000000/webcam-man.png">';
        // str += "          </span>";
        // str += '          <div class="cm-msg-text">';
        // str += msg;
        // str += "          </div>";
        str += '          <div class="cm-msg-button">';
        str += "            <ul>";
        str += btn_obj;
        str += "            </ul>";
        str += "          </div>";
        str += "        </div>";
        $(".chat-logs").append(str);
        $("#cm-msg-" + INDEX)
            .hide()
            .fadeIn(300);
        $(".chat-logs")
            .stop()
            .animate({ scrollTop: $(".chat-logs")[0].scrollHeight }, 1000);
        $("#chat-input").attr("disabled", true);
    }

    $(document).delegate(".chat-btn", "click", function () {
        var value = $(this).attr("chat-value");
        var name = $(this).html();
        $("#chat-input").attr("disabled", false);
        $(this).prop( "disabled", true );
        get_message(value, "self");
        get_message(value, "user");
    });

    $("#chat-circle").click(function () {
        $("#chat-circle").toggle("scale");
        $(".chat-box").toggle("scale");
        if ($(".chat-msg").length == 0) {
            let msg = "Hey! How are you doing?\n I'm here to help you &#128516;"
            add_message(msg, "user");

            var buttons = [
                {
                    name: "Invest using a credit/debit card",
                    value: "Can I invest using a credit/debit card?",
                },
                {
                    name: "I need to add a bank account",
                    value: "Why do I need to add a bank account?",
                },
            ];
            generate_button_message(buttons);
        }
    });

    $(".chat-box-toggle").click(function () {
        $("#chat-circle").toggle("scale");
        $(".chat-box").toggle("scale");
    });
});
