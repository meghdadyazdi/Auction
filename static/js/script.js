$(document).ready(function () {
  $("#auction-set-time").click(function () {
    $("#auction_start").removeClass("d-none");
    $("#auction_time-select").addClass("d-none");
    var time_quantity = $("#time-quantity").val();
    var time_scale = $("#time-scale").val();
    $("#auction-time-quantity").html(time_quantity);
    $("#auction-time-scale").html(time_scale);
    $("#announce-time").removeClass("d-none");

    if (time_scale == "Minutes") {
      var auction_time = time_quantity * 60 + 1;
    }
    if (time_scale == "Hours") {
      var auction_time = time_quantity * 60 * 60 + 1;
    }
    if (time_scale == "Days") {
      var auction_time = time_quantity * 60 * 60 * 24 + 1;
    }
    console.log(auction_time);
    var endFix = new Date();

    endFix = Date.parse(endFix) / 1000 + auction_time;
    $("#end-time-fix-form").val(endFix);
    $("#auction-time-form").val(auction_time);
    // $("#auction-price-form").val(112);
    console.log(endFix);
    tt = $("#auction_time_start").val();
    console.log(time_scale);
    console.log(time_quantity);
  });

  





  $("#1a").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#1a").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(1)
    $("#higher-bid-user").val($("#user-name").val())
    
  });

  $("#5a").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#5a").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(5)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#10a").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#10a").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(10)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#20a").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#20a").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(20)
    $("#higher-bid-user").val($("#user-name").val())
  });



  $("#10b").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#10b").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(10)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#20b").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#20b").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(20)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#50b").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#50b").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(50)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#100b").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#100b").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(100)
    $("#higher-bid-user").val($("#user-name").val())
  });


  $("#50c").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#50c").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(50)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#100c").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#100c").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(100)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#200c").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#200c").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(200)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#500c").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#500c").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(500)
    $("#higher-bid-user").val($("#user-name").val())
  });


  $("#200d").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#200d").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(200)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#500d").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#500d").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(500)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#1000d").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#1000d").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(1000)
    $("#higher-bid-user").val($("#user-name").val())
  });

  $("#5000d").click(function () {
    $(".btn-danger").addClass("d-none");
    $("#5000d").removeClass("d-none");
    $("#higher-bid-confirm").removeClass("d-none");
    $("#confirm-bid").removeClass("d-none");
    $("#higher-bid").val(5000)
    $("#higher-bid-user").val($("#user-name").val())
  });



















  if ($("#auction_status").val() == 1) {
    $("#auction_duration").addClass("d-none");
    $("#before_auction").addClass("d-none");
    var endFix = $("#end-time-fix").val();
    //console.log(endFix);

    var days;
    var hours;
    var minutes;
    var seconds;
    $.fn.makeTimer = function () {
      var now = new Date();
      now = Date.parse(now) / 1000;
      var timeLeft = endFix - now;
      days = Math.floor(timeLeft / 86400);
      hours = Math.floor((timeLeft - days * 86400) / 3600);
      minutes = Math.floor((timeLeft - days * 86400 - hours * 3600) / 60);
      seconds = Math.floor(
        timeLeft - days * 86400 - hours * 3600 - minutes * 60);
    //   console.log(now);
    //   console.log(endFix);
    //   console.log(endFix - now);

      if (hours < "10") {
        hours = "0" + hours;
      }
      if (minutes < "10") {
        minutes = "0" + minutes;
      }
      if (seconds < "10") {
        seconds = "0" + seconds;
      }

    //   console.log(hours);
    //   console.log(minutes);
    //   console.log(seconds);
    //   console.log(days);
      

      if (hours >= 0 && minutes >= 0 && seconds >= 0 && days >= 0) {
        //console.log(days);
        $("#days").html(days + "<span class='digits'>Days</span>");
        $("#hours").html(hours + "<span class='digits'>Hours</span>");
        $("#minutes").html(minutes + "<span class='digits'>Minutes</span>");
        $("#seconds").html(seconds + "<span class='digits'>Seconds</span>");
      }
      else{
          $("#bidding").addClass('d-none');
          $("#status-highest").addClass('d-none');
          $("#end-auction-winner").removeClass('d-none');
          $("#winner").removeClass('d-none');
      }
    };
    var now = new Date();
    now = Date.parse(now) / 1000;
    //console.log((endFix - now) / 1000);
    // interval = setInterval($.fn.makeTimer, 1000); //setInterval(function () {makeTimer();}, 1000);
    if ((endFix - now) > 0) {
        // clearInterval($.fn.makeTimer);
        setInterval($.fn.makeTimer, 1000);
    }
  }
  //console.log($("#bid-offer").val())
  if ((endFix - now) < 0){
        $("#bidding").addClass('d-none');
        $("#status-highest").addClass('d-none');
        $("#end-auction-winner").removeClass('d-none');
        $("#winner").removeClass('d-none');
    }
});
