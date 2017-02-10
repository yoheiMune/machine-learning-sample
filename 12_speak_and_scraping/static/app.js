
/**
 * 音声認識のインスタンス.
 */
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

/**
 * 開始ボタンを押した時のイベント.
 */
function handleStartButtonClick() {

    // 音声認識のインスタンスを生成します.
    recognition = new webkitSpeechRecognition();

    // 言語は日本語にします.
    recognition.lang = 'ja';

    // 音声認識開始時のイベント.
    recognition.onstart = function() {
        console.log('onstart');
        document.querySelector('.js-btn-group').classList.add('--recording');
    };

    // 音声認識エラー発生時のイベント.
    recognition.onerror = function(event) {
        console.log('onerror:', event.error);
        document.querySelector('.js-btn-group').classList.remove('--recording');
    };

    // 音声認識終了時のイベント.
    recognition.onend = function() {
        console.log('onend');
        document.querySelector('.js-btn-group').classList.remove('--recording');
    };

    // 音声認識の結果を取得した時のイベント.
    recognition.onresult = event => {
      console.log('onresult');
      let text = event.results.item(0).item(0).transcript;

      if (text.indexOf('ニュース') !== -1) {
        // ニュースだったら、API経由でおすすめ記事を取得する.
        showRecommendArticle();
      
      } else {
        // ニュース以外はわからないよ〜.
        let synthes = new SpeechSynthesisUtterance('ごめんなさい、ニュース以外はわかりません');
        synthes.lang = "ja-JP";
        speechSynthesis.speak(synthes);        
      }
    };

    // 音声認識を開始します.
    recognition.start();
}

/**
 * 停止ボタンを押した時のイベント.
 */
function handleStopButtonClick() {
    if (recognition) {
        recognition.stop();
    }
}

/**
 * API経由でおすすめニュースを取得して、音声で発します.
 */
function showRecommendArticle() {

    api('/api/recommend_article').then(response => {
        let { content, link } = JSON.parse(response);
        console.log(content);

        content = content.split("-")[0];

        let synthes = new SpeechSynthesisUtterance(content);
        synthes.lang = "ja-JP";
        speechSynthesis.speak(synthes);

        document.getElementById('text').innerHTML = `<a href="${link}">${content}</a>`;
    });
}

/**
 * アプリ起動時に、説明を表示します.
 */
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

/**
 * アプリを起動します.
 */
window.addEventListener('DOMContentLoaded', () => {

    // アプリの説明を行います.
    startIntro().then(() => {

        // ボタンの表示と挙動
        document.querySelector('.js-btn-group').classList.add('--visible');
        document.getElementById('startButton').onclick = handleStartButtonClick;
        document.getElementById('stopButton').onclick = handleStopButtonClick;
    });
});