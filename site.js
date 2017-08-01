/*------------------------Declare Variables------------------*/

// Declares the size of various stats: the four main buttons, costs for
// those buttons, and an update counter
// {{
// 4 buttons
var points = 0;
var click_size = 1;
var machines = 0;
var speed = 100;

// 3 cost
var size_cost = 1;
var speed_cost = 1;
var machine_cost = 1;

// machines that collect automatically
var reserved_machines = 0;

// counter
var update_count = 0;
// }}

// Disable click-dragging pictures
// {{
$('img').on('dragstart', function(event) { event.preventDefault(); });
// }}

/* Update the game. Add points made by machines and update points html.
Every 20th run,
add one machine to reserved machines, and then change the "reserved
machines" html, and then restart the counter. */
// {{
function update() {
    update_count += 1;
    points += machines * .002 * (speed / 100);
    if (update_count >= 20) {
        reserved_machines += 1;
        $("#collecting").html("Reserved machines: " + reserved_machines);
        update_count = 0;
    }
    $("#stat2").html((Math.round(points * 100)/100));
    
}
// }}


// Adds click_size to total points, and updates html
// {{
$("#pic_point").click(function() {
    points += click_size;
    $("#stat2").html((Math.round(points * 100)/100));
});
// }}

// These three buttons all do three things each: if you can afford
// the cost, it adds the bought stat, it subtracts the cost from
// points, and it increases the price. HTML is updated after each
// {{
$("#pic_size").click(function() {
    if (points >= size_cost) {
        click_size += .05;
        $("#size").html("Click size: " + (Math.round(click_size * 100)/100));
        points -= size_cost;
        $("#stat2").html((Math.round(points * 100)/100));
        size_cost *= 1.2;
        $("#price_size").html("Cost: " + (Math.round(size_cost * 100)/100) + " points");
    }
});

$("#pic_machine").click(function() {
    if (points >= machine_cost) {
        machines += 1;
        $("#machines").html("Machines: " + (Math.round(machines * 100)/100));
        points -= machine_cost;
        $("#stat2").html((Math.round(points * 100)/100));
        machine_cost *= 1.35;
        $("#price_machines").html("Cost: " + (Math.round(machine_cost * 100)/100) + " points");
    }
});

$("#pic_speed").click(function() {
    if (points >= speed_cost) {
        speed += 5;
        $("#speed").html("Speed: " + (Math.round(speed * 100)/100) + "%")
        points -= speed_cost;
        $("#stat2").html((Math.round(points * 100)/100));
        speed_cost *= 1.25;
        $("#price_speed").html("Cost: " + (Math.round(speed_cost * 100)/100) + " points");
    }
});
// }}

$("#study20").click(function() {
    $(".flashcard").css('display', 'flex');
/*    $("#overcard").html('<div id="overcard-question" class="qna">aaaaaaaaaaaaa</div> <form action="http://www.example.com/comments.php">aaa<div id="overcard-answer" class="qna"><input type="textarea" name="answer_guess" rows="4">abab</textarea></form></div>'); */
}); 


updateSpeed = setInterval(update, 10);















