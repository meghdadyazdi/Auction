$(document).ready(function () {
    //here when button with id=start-auctionis clicked, the value of time-quantity and
    //time-scale is saved.
  $("#start-auction").click(function () {
    $("#start-auction").
    var time_quantity = $("#time-quantity").val();
    var time_scale = $("#time-scale").val();
    console.log(time_scale);
    if (time_scale == "Minutes") {auction_time = time_quantity * 60;}
    if (time_scale == "Hours") {auction_time = time_quantity * 60 * 60;}
    if (time_scale == "Days") {auction_time = time_quantity * 60 * 60 * 24;}  
  //I want to define nowFix but auction_time is not recognized
  var nowFix = new Date();
  nowFix = Date.parse(nowFix) / 1000 + auction_time;
  //console.log(nowFix);
  console.log(auction_time);
  var days;
  var hours;
  var minutes;
  var seconds;
  $.fn.makeTimer = function () {
      var now = new Date();
      now = Date.parse(now) / 1000;
      var timeLeft = nowFix - now;
      days = Math.floor(timeLeft / 86400);
      hours = Math.floor((timeLeft - days * 86400) / 3600);
      minutes = Math.floor((timeLeft - days * 86400 - hours * 3600) / 60);
      seconds = Math.floor(
        timeLeft - days * 86400 - hours * 3600 - minutes * 60
      );
      //console.log(timeLeft);
      if (hours < "10") {hours = "0" + hours;}
      if (minutes < "10") {minutes = "0" + minutes;}
      if (seconds < "10") {seconds = "0" + seconds;}
      if (hours >= 0 && minutes >= 0 && seconds >= 0 && days >= 0) {
          //console.log(days);
          $("#days").html(days + "<span class='digits'>Days</span>");
          $("#hours").html(hours + "<span class='digits'>Hours</span>");
          $("#minutes").html(minutes + "<span class='digits'>Minutes</span>");
          $("#seconds").html(seconds + "<span class='digits'>Seconds</span>");
      }
    }
  setInterval($.fn.makeTimer,1000); //setInterval(function () {makeTimer();}, 1000);
  });
});