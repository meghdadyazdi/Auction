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
      $("#end-time-fix-form").val(endFix)
      $("#auction-time-form").val(auction_time)
      console.log(endFix);
      tt = $("#auction_time_start").val();
      console.log(time_scale);
      console.log(time_quantity);
    



  });

  $("#auction_start").click(function () {
      $("#auction_start").addClass("d-none");
  });
    
    
    if ($("#auction_status").val() == 1) {
      $("#auction_duration").addClass("d-none");
      var endFix = $("#end-time-fix").val();
      console.log(endFix);

      

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
          timeLeft - days * 86400 - hours * 3600 - minutes * 60
        );
        console.log(now);
        console.log(endFix);
        console.log(endFix - now);
        
        if (hours < "10") {
          hours = "0" + hours;
        }
        if (minutes < "10") {
          minutes = "0" + minutes;
        }
        if (seconds < "10") {
          seconds = "0" + seconds;
        }
        if (hours >= 0 && minutes >= 0 && seconds >= 0 && days >= 0) {
          //console.log(days);
          $("#days").html(days + "<span class='digits'>Days</span>");
          $("#hours").html(hours + "<span class='digits'>Hours</span>");
          $("#minutes").html(minutes + "<span class='digits'>Minutes</span>");
          $("#seconds").html(seconds + "<span class='digits'>Seconds</span>");
        }
      };
      setInterval($.fn.makeTimer, 1000); //setInterval(function () {makeTimer();}, 1000);
    }
  
});
