
// when the button gets clicked

$("#mediaButton").ready(function() {
  $("#mediaButton").click(function() {
    console.log('clicked');
    var value = document.getElementById("playerIcon").innerHTML; 
    console.log(value);
    if (value === 'Play') {
      // change value to a stop button
      $('#playerIcon').text('Stop')
    } else {
      // change vlaue to a play button
      $('#playerIcon').text('Play')
    }
  })
})

// mic = new p5.AudioIn()
// mic.start();

// // create a sound recorder
// recorder = new p5.SoundRecorder();
// recorder.setInput(mic)
// soundFile = new p5.SoundFile();
