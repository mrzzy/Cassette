
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
        var spanData = document.createElement('span')
        bigDiv.style.padding="2px"
        // dynamically get the colour
        spanData.innerHTML = data['text'];

        spanData.style.color=data['color']
        spanData.style.fontSize="16px"
        spanData.style.margin="2px"

        bigDiv.append(spanData)
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
