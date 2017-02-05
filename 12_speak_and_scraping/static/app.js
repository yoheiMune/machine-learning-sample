

let recognition;

function handleStartButtonClick() {
    console.log('handleStartButtonClick');

    recognition = new webkitSpeechRecognition();
    recognition.lang = 'ja';
    // recognition.lang = 'ja-JP';
    // recognition.onresult = function(e) {
    //     alert('aaaaaa');
    //     console.log(e);
    //     if (e.results.length > 0) {
    //         console.log(e.results);
    //         let value = e.results[0][0].transcript;
    //         console.log(value);
    //     }
    // };

    recognition.onstart = function() {
        console.log('onstart');
    };

    recognition.onerror = function(event) {
        console.log('onerror:', event.error);
    };

    recognition.onend = function() {
        console.log('onend');
    };

    // recognition.addEventListener('result', event => {
    //   console.log('onresult2');
    //   alert(event.results.item(0).item(0).transcript);
    // }, false);

    recognition.onresult = event => {
      console.log('onresult2');
      let text = event.results.item(0).item(0).transcript;
      alert(text);

      if (text.indexOf('ニュース') !== -1) {
        showRecommendArticle();
      }
    };

    // recognition.onresult = function(event) {
    //     console.log('onresult');
    //   var interim_transcript = '';
    //   // if (typeof(event.results) == 'undefined') {
    //   //   recognition.onend = null;
    //   //   recognition.stop();
    //   //   upgrade();
    //   //   return;
    //   // }
    //   for (var i = event.resultIndex; i < event.results.length; ++i) {
    //     if (event.results[i].isFinal) {
    //       final_transcript += event.results[i][0].transcript;
    //     } else {
    //       interim_transcript += event.results[i][0].transcript;
    //     }
    //   }
    //   final_transcript = capitalize(final_transcript);
    //   final_span.innerHTML = linebreak(final_transcript);
    //   interim_span.innerHTML = linebreak(interim_transcript);
    //   if (final_transcript || interim_transcript) {
    //     showButtons('inline-block');
    //   }
    // };

    recognition.start();
}

function handleStopButtonClick() {
    console.log('handleStopButtonClick');

    if (recognition) {
        console.log('aaaaaaaaa');
        recognition.stop();
    }
}

function showRecommendArticle() {

  $.getJSON('/api/recommend_article').then(({ content, link }) => {
    console.log(content);

    let synthes = new SpeechSynthesisUtterance(content);
    synthes.lang = "ja-JP";
    speechSynthesis.speak(synthes);

    document.getElementById('result').innerHTML = `
        <a href="${link}">${content}</a><br>
    `;

  });

}

// test.
showRecommendArticle();


function startApplication() {

    let startButton = document.getElementById('startButton');
    startButton.addEventListener('click', handleStartButtonClick);

    let stopButton = document.getElementById('stopButton');
    stopButton.addEventListener('click', handleStopButtonClick);
}

window.addEventListener('DOMContentLoaded', startApplication);