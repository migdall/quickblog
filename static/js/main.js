let preview = document.getElementById("preview");
let recording = document.getElementById("recording");
let startButton = document.getElementById("startButton");
let stopButton = document.getElementById("stopButton");
let downloadButton = document.getElementById("downloadButton");
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
            downloadButton.href = stream;
            preview.captureStream = preview.captureStream || preview.mozCaptureStream;
            return new Promise(resolve => preview.onplaying = resolve);
        }).then(() => startRecording(preview.captureStream(), recordingTimeMS))
        .then(recordedChunks => {
            let recordedBlob = new Blob(recordedChunks, {
                type: "video/webm"
            });
            var saying_id = document.getElementById("saying_id_input").value;
            var question_id = document.getElementById("question_id_input").value;
            recording.src = URL.createObjectURL(recordedBlob);
            downloadButton.href = recording.src;
            downloadButton.download = saying_id + "-" + question_id + ".webm";

            log("Successfully recorded " + recordedBlob.size + " bytes of " +
                recordedBlob.type + " media.");
        })
        .catch(log);
}, false);
stopButton.addEventListener("click", function() {
    stop(preview.srcObject);
}, false);
