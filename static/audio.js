
$(document).ready(function() {
  function handleSuccess(stream) {
    // Setup recorder and handlers
    var context = new AudioContext();
    var source = context.createMediaStreamSource(stream);
    var recorder = new WebAudioRecorder(source, {
      workerDir: "static/",   // must end with slash
      numChannels: 1,
    });

    recorder.onComplete = (function(rec, blob) {
      // prints out size, type: audio/wav
      console.log(blob);
      $.ajax({
          type: "POST",
          url: "/audioprocess",
          data: blob,
          processData: false,
          contentType: false
      })
      .done(function(data) {
        // prints out the object
        // console.log(data);
        // do something with the data
        // #bigContainer - contains all the files

        // prints out the text
        console.log(data['text']);
        var bigDiv = document.getElementById('bigContainer')
        bigDiv.style.marginTop = "0.4vh";
        bigDiv.style.marginBottom = "0.6vh";

        var smallDiv = document.createElement('div')
        var spanData = document.createElement('div')
        bigDiv.style.padding="2px"
        // dynamically get the colour
        spanData.innerHTML = data['text'];
        spanData.style.marginLeft="0.8em"

        smallDiv.style.backgroundColor=data['color']
        smallDiv.style.color="#FFFFFF"
        smallDiv.style.fontSize="16px"
        smallDiv.style.margin="1.2em"
        smallDiv.style.borderRadius = "8px"


        smallDiv.append(spanData)
        bigDiv.append(smallDiv)
      })
    });
  

    // Start recording handler
    $("#mediaButton").mousedown(function() {
      console.log("recording...");
      recorder.startRecording();
      // if it is running - check the time seconds every second
      var recall = setInterval(checktime, 1000);
      function checktime() {
        time = recorder.recordingTime();
        console.log(time);
        // if time is over 4
        if (time >= 4) {
          $('#mediaButton').mouseup();
          $('#mediaButton').mousedown();
        }
      }
    })
  
    // End recording handler
    $("#mediaButton").mouseup(function() {
      console.log("done recording.");
      console.log("recording length: " + recorder.recordingTime());
      if (recorder.recordingTime() > 2) {
        recorder.finishRecording();j
      }
    })
  }

  
  navigator.mediaDevices.getUserMedia({ audio: true, video: false })
      .then(handleSuccess);

})
