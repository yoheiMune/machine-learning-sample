(function () {

    // ref: 迷路作り
    // http://www5d.biglobe.ne.jp/~stssk/maze/make.html

    // 配列をシャッフルする
    function shuffle (o) {
        for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
        return o;
    }

    /**
        迷路を表現するクラス
    */
    window.Maze = function (size) {
        // 壁と通路の関係上、サイズは奇数にしとく
        this.size = (size % 2 === 0 ? size + 1 : size);
        this.box = [];
        this.$maze = document.querySelector("#maze");
    };

    /**
        アルゴリズムタイプ
    */
    Maze.ALGO = {STICK: 1};

    var p = Maze.prototype;

    /**
        迷路を表示する
    */
    p.show = function () {
        var snipet = '';
        for (var i = 0; i < this.size; i++) {
            for (var j = 0; j < this.size; j++) {
                if (this.box[j][i] === 0) {
                    // 壁
                    snipet += '<div class="w"></div>';
                } else {
                    // 通路
                    snipet += '<div class="p"></div>';
                }
            }
        }
        this.$maze.innerHTML = snipet;
        this.$maze.style.height = (this.size * 10) + 'px';
        this.$maze.style.width  = (this.size * 10) + 'px';
    }

    /**
        迷路を作る
    */
    p.create = function (options) {
        options = options || {};
        if (options.algorithm === Maze.ALGO.STICK) {
            this._createByStick();
        }
        this.show();
    }

    /**
        迷路を作る（棒倒し）
    */
    p._createByStick = function () {

        // 初期化
        // まずは壁と通路を交互に作成する
        this.box = [];
        for (var i = 0; i < this.size; i++) {
            var row = [];
            this.box.push(row);
            for (var j = 0; j < this.size; j++) {
                // 最初の行と最後行は壁
                if (i === 0 || (i + 1) === this.size) {
                    row.push(0);
                // 最初の列と最後の列も壁
                } else if (j === 0 || (j + 1) === this.size) {
                    row.push(0);
                // 奇数行は全部通路
                } else if (i % 2 === 1) {
                    row.push(1);
                // 偶数行は壁と通路を交互に配置
                } else {
                    // 壁と通路
                    row.push(j % 2);
                }
            }
        }

        // debug
        // return;

        // その後の壁の行は下左右に倒してOK（重なるのはNG）
        var direction = ['bottom', 'left', 'right'];
        for (var r = 0; r < this.box.length; r++) {
            // 最初と最後の行は対象外
            if (r === 0 || (r + 1) === this.box.length) {
                continue;
            }
            // 壁がある行のみを対象
            if (r % 2 === 1) {
                continue;
            }
            // 行を取り出す
            var row = this.box[r];

            // 最初の行のみ、上下左右倒してOK（重なるのはNG）
            var direction = ['top', 'bottom', 'left', 'right'];
            if (r >= 4) {
                // 最初以外は、上には倒しちゃだめー
                direction = direction.slice(1);
            }

            for (var i = 0; i < row.length; i++) {
                // 端っこは対象外
                if (i === 0 || (i + 1) === row.length) {
                    continue;
                }
                if (i % 2 === 0) {
                    direction = shuffle(direction);
                    for (var j = 0; j < direction.length; j++) {
                        if (direction[j] === "top") {
                            if (this.box[r-1][i] === 1) {
                                this.box[r-1][i] = 0;
                                break;
                            }
                        }
                        if (direction[j] === "left") {
                            if (this.box[r][i-1] === 1) {
                                this.box[r][i-1] = 0;
                                break;
                            }
                        }
                        if (direction[j] === "right") {
                            if (this.box[r][i+1] === 1) {
                                this.box[r][i+1] = 0;
                                break;
                            }
                        }
                        if (direction[j] === "bottom") {
                            if (this.box[r+1][i] === 1) {
                                this.box[r+1][i] = 0;
                                break;
                            }
                        }
                    }
                }
            }
        }
    }

})();
