let preview = document.getElementById("preview");
let recording = document.getElementById("recording");
let startButton = document.getElementById("startButton");
//let stopButton = document.getElementById("stopButton");
//let downloadButton = document.getElementById("downloadButton");
let logElement = document.getElementById("log");
var httpRequest = new XMLHttpRequest();

let recordingTimeMS = 20000;

function log(msg) {
    logElement.innerHTML += msg + "\n";
}

function wait(delayInMS) {
    return new Promise(resolve => setTimeout(resolve, delayInMS));
}

function startRecording(stream, lengthInMS) {
    let recorder = new MediaRecorder(stream);
    let data = [];

    recorder.ondataavailable = event => data.push(event.data);
    recorder.start();
    log(recorder.state + " for " + (lengthInMS / 1000) + " seconds...");

    let stopped = new Promise((resolve, reject) => {
        recorder.onstop = resolve;
        recorder.onerror = event => reject(event.name);
    });

     
    let recorded = wait(lengthInMS).then(
        () => recorder.state == "recording" && recorder.stop() );

    return Promise.all([
            stopped,
            recorded
        ])
        .then(() => data);
}

function stop(stream) {
    stream.getTracks().forEach(track => track.stop());
}

function alertContents() {
    try {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                alert(httpRequest.responseText);
            } else {
                alert('There was a problem with the request.');
            }
        }
    } catch (e) {
        alert('Caught Exception: ' + e.description);
    }
}

startButton.addEventListener("click", function() {
    navigator.mediaDevices.getUserMedia({
            video: true,
            audio: true
        }).then(stream => {
            preview.srcObject = stream;
            //downloadButton.href = stream;
            preview.captureStream = preview.captureStream || preview.mozCaptureStream;
            return new Promise(resolve => preview.onplaying = resolve);
        }).then(() => startRecording(preview.captureStream(), recordingTimeMS))
        .then(recordedChunks => {
            let recordedBlob = new Blob(recordedChunks, {
                type: "video/webm"
            });
            recording.src = URL.createObjectURL(recordedBlob);
            var form = document.getElementById('send_recording_form');
            var o_data = new FormData(form);
            o_data.set('recording', recordedBlob, 'recording_' + Math.floor(Math.random() * 2000000 + 1));
            request.onreadystatechange = alertContents;
            request.open("POST", form.action);
            request.send(o_data);
            //downloadButton.href = recording.src;
            //downloadButton.download = "RecordedVideo.webm";

            log("Successfully recorded " + recordedBlob.size + " bytes of " +
                recordedBlob.type + " media.");
        })
        .catch(log);
}, false);
/*stopButton.addEventListener("click", function() {
    stop(preview.srcObject);
}, false);*/
