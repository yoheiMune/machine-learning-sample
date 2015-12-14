(function () {


    function shuffle(o){
        for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
        return o;
    }

    window.Maze = function (size) {

        this.size = (size % 2 === 0 ? size + 1 : size);
        this.box = [];
        this.$maze = document.querySelector("#maze");
        this.BOX_SIZE = 10;
        this.defaultDuration = 100;
        this.initialize();
    };
    var p = Maze.prototype;

    /**
        アルゴリズムタイプ
    */
    Maze.ALGO = {
        STICK: 1
    };

    /**
        初期化メソッド
    */
    p.initialize = function () {
        for (var i = 0; i < this.size; i++) {
            var row = [];
            this.box.push(row);
            for (var j = 0; j < this.size; j++) {
                row.push(0);
            }
        }
        this.show();
    }


    /**
        迷路表示
    */
    p.show = function () {
        var snipet = '';
        for (var i = 0; i < this.size; i++) {
            for (var j = 0; j < this.size; j++) {
                if (i === 1 && j === 1) {
                    snipet += '<div class="s"></div>';
                } else if (i === this.size - 2 && j === this.size - 2) {
                    snipet += '<div class="e"></div>';
                } else if (this.box[i][j] === 0) {
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
                // それ以外は交互に
                } else {
                    // 壁
                    if (j % 2 == 0) {
                        row.push(0);
                    // 通路
                    } else {
                        row.push(1);
                    }

                }
            }
        }

        // その後の壁の行は下左右に倒してOK（重なるのはNG）
        var direction = ['bottom', 'left', 'right'];
        for (var r = 0; r < this.box.length; r++) {
            // 最初と最後の行は対象外
            if (r === 0 || (r + 1) === this.box.length) {
                continue;
            }
            // 壁行じゃないと対象外
            if (r % 2 === 1) {
                continue;
            }
            // 行を取り出す
            var row = this.box[r];

            // 最初の行のみ、上下左右倒してOK（重なるのはNG）
            var direction = ['top', 'bottom', 'left', 'right'];
            if (r >= 4) {
                direction = direction.slice(1);
            }
            // console.debug(direction);

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
                                // console.debug("top", r, i);
                                break;
                            }
                        }
                        if (direction[j] === "left") {
                            if (this.box[r][i-1] === 1) {
                                this.box[r][i-1] = 0;
                                // console.debug("left", r, i);
                                break;
                            }
                        }
                        if (direction[j] === "right") {
                            if (this.box[r][i+1] === 1) {
                                this.box[r][i+1] = 0;
                                // console.debug("right", r, i);
                                break;
                            }
                        }
                        if (direction[j] === "bottom") {
                            if (this.box[r+1][i] === 1) {
                                this.box[r+1][i] = 0;
                                // console.debug("bottom", r, i);
                                break;
                            }
                        }
                    }
                }
            }
        }
    }



})();
