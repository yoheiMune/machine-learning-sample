"use strict";

/**
 * 描画中か否かを判定するフラグ.
 */
let drawing = false;
let points = [];

let canvas;
let context;

function api(url) {
    return new Promise((resolve, reject) => {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onreadystatechange = function (e) {
            if (this.readyState === 4 && this.status === 200) {
                resolve(this.responseText);
            }
        }
        // let formData = new FormData();
        // formData.append('data', data);
        xhr.send();
    });
}

function draw() {

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.lineWidth = 40;
    context.lineCap = 'round';

    for (let i = 0; i < points.length; i++) {
        let p1 = points[i];
        let p2 = points[i + 1];
        if (p1 && p2) {
            context.beginPath();
            context.moveTo(p1.x, p1.y);
            context.lineTo(p2.x, p2.y);
            context.stroke();
        }
    }

    requestAnimationFrame(draw);
}

function judge() {

    // 28 x 28 に圧縮する.
    let img = new Image();
    img.src = canvas.toDataURL();

    // tmp.
    let resultPanel = document.getElementById('result');
    // resultPanel.innerHTML = '';
    // resultPanel.appendChild(img);

    let tmpCanvas = document.createElement('canvas');
    tmpCanvas.width = 28;
    tmpCanvas.height = 28;
    tmpCanvas.getContext('2d').drawImage(img, 0, 0, 28, 28);

    let imgResize = new Image();
    imgResize.src = tmpCanvas.toDataURL();

    // resultPanel.innerHTML = '';
    // resultPanel.appendChild(imgResize);

    // 28x28
    let data = [];
    var imgd = tmpCanvas.getContext('2d').getImageData(0, 0, 28, 28);
    var pixcels = imgd.data;
    for (let i = 0; i < pixcels.length; i += 4) {
        let alpha = pixcels[i + 3];
        data.push(alpha);
    }

    console.log('alpha.size=', data.length, 28*28);

    let url = '/api/judge?data=' + data.join(',');

    api(url).then(result => {
        resultPanel.innerHTML = result;
    });

}









function handleMouseDown(e) {
    console.log('down');
    drawing = true;
    points = [];
}

function handleMouseMove(e) {

    let rect = canvas.getBoundingClientRect();
    let x = Math.max(0, e.clientX - rect.left);
    let y = Math.max(0, e.clientY - rect.top);
    
    if (drawing) {
        points.push({x, y});
        draw();
    }
}

function handleMouseUp() {
    console.log('upOrLeave');
    drawing = false;

    judge();
}

function handleDelButtonClick() {
    console.log('handleDelButtonClick');
    points = [];
}

// function handleJudgeButtonClick() {
//     console.log('handleJudgeButtonClick');
//     judge();
// }

function startApplication() {

    canvas = document.getElementById('canvas');
    context = canvas.getContext('2d');

    console.log(canvas.width, canvas.height);

    canvas.addEventListener('mousedown', handleMouseDown);
    canvas.addEventListener('mousemove', handleMouseMove);
    canvas.addEventListener('mouseup', handleMouseUp);
    canvas.addEventListener('mouseleave', handleMouseUp);

    let delButton = document.getElementById('delButton');
    delButton.addEventListener('click', handleDelButtonClick);

    // let judgeButton = document.getElementById('judgeButton');
    // judgeButton.addEventListener('click', handleJudgeButtonClick);

}

window.addEventListener('DOMContentLoaded', startApplication);