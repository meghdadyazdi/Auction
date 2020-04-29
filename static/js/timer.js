

var time_quantity = document.getElementById("time-quantity");
var time_scale = document.getElementById("time-scale");
console.log(time_scale);

if (time_scale == "Minutes") {var auction_time = time_quantity * 60;}
if (time_scale == "Hours") {var auction_time = time_quantity * 60 * 60;}
if (time_scale == "Days") {var auction_time = time_quantity * 60 * 60 * 24;}    


var nowFix = new Date();
nowFix = (Date.parse(nowFix) / 1000) + auction_time;
//console.log(nowFix);
var days; 
var hours;
var minutes;
var seconds;



function makeTimer() {

	//		var endTime = new Date("29 April 2018 9:56:00 GMT+01:00");	
		
            

			var now = new Date();
            now = (Date.parse(now) / 1000);
            
            //var endTime = new Date("29 April 2020 15:31:30 GMT+01:00");			
            //endTime = (Date.parse(endTime) / 1000);
            //endTime = 3600;

            //var timeLeft = endTime - now;
            var timeLeft = nowFix - now;
           
            //console.log(timeLeft)
            

			days = Math.floor(timeLeft / 86400); 
			hours = Math.floor((timeLeft - (days * 86400)) / 3600);
			minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
			seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
  
			if (hours < "10") { hours = "0" + hours; }
			if (minutes < "10") { minutes = "0" + minutes; }
            if (seconds < "10") { seconds = "0" + seconds; }

            if (hours >= 0 && minutes >= 0 && seconds >= 0 && days >= 0){
                $("#days").html(days + "<span class='digits'>Days</span>");
                $("#hours").html(hours + "<span class='digits'>Hours</span>");
                $("#minutes").html(minutes + "<span class='digits'>Minutes</span>");
                $("#seconds").html(seconds + "<span class='digits'>Seconds</span>");
            }

                

    }

    
    setInterval(function() { makeTimer(); }, 1000);