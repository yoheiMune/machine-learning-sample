
let recognition;


/**
 * サーバー通信を行う.
 */
function api(url) {
    return new Promise((resolve, reject) => {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onreadystatechange = function (e) {
            if (this.readyState === 4 && this.status === 200) {
                resolve(this.responseText);
            }
        }
        xhr.send();
    });
}


function handleStartButtonClick() {
    console.log('handleStartButtonClick');

    recognition = new webkitSpeechRecognition();
    recognition.lang = 'ja';

    recognition.onstart = function() {
        console.log('onstart');
        document.querySelector('.js-btn-group').classList.add('--recording');
    };

    recognition.onerror = function(event) {
        console.log('onerror:', event.error);
        document.querySelector('.js-btn-group').classList.remove('--recording');
    };

    recognition.onend = function() {
        console.log('onend');
        document.querySelector('.js-btn-group').classList.remove('--recording');
    };


    recognition.onresult = event => {
      console.log('onresult2');
      let text = event.results.item(0).item(0).transcript;
      alert(text);

      if (text.indexOf('ニュース') !== -1) {
        showRecommendArticle();
      }
    };

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

    api('/api/recommend_article').then(response => {
        let { content, link } = JSON.parse(response);
        console.log(content);

        content = content.split("-")[0];

        let synthes = new SpeechSynthesisUtterance(content);
        synthes.lang = "ja-JP";
        speechSynthesis.speak(synthes);

        document.getElementById('text').innerHTML = `
            <a href="${link}">${content}</a><br>
        `;
    });

}

// test.
// showRecommendArticle();

function startIntro() {

    let elm = document.getElementById('text');

    return new Promise((resolve, reject) => {

        let texts = "「おすすめニュースを教えて」と聞いてみてください。".split('');

        function showMessage(texts, cb) {
            if (texts.length === 0) {
                return cb();
            }
            let ch = texts.shift();
            elm.innerHTML += ch;
            setTimeout(() => {
                showMessage(texts, cb);
            }, 120);
        }

        elm.innerHTML = '';
        showMessage(texts, resolve);
    });

}


function startApplication() {

    startIntro().then(() => {

        // TODO ボタン表示など.
        document.querySelector('.js-btn-group').classList.add('--visible');

        let startButton = document.getElementById('startButton');
        startButton.addEventListener('click', handleStartButtonClick);

        let stopButton = document.getElementById('stopButton');
        stopButton.addEventListener('click', handleStopButtonClick);
    });

}

window.addEventListener('DOMContentLoaded', startApplication);