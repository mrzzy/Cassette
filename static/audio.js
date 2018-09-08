
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
      console.log(blob);
      $.ajax({
          type: "POST",
          url: "/audioprocess",
          data: blob,
          processData: false,
          contentType: false
      });
    });
  

    // Start recording handlerj
    $("#mediaButton").mousedown(function() {
      console.log("recording...");
      recorder.startRecording();
    })
  
    // End recording handler
    $("#mediaButton").mouseup(function() {
      console.log("done recording.");
      console.log("recording length: " + recorder.recordingTime());
      recorder.finishRecording();
    })
  }

  
  navigator.mediaDevices.getUserMedia({ audio: true, video: false })
      .then(handleSuccess);

})
