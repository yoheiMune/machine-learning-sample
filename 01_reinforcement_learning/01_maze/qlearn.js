(function () {

    // ソート
    function shuffle(o){
        for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
        return o;
    }
    // 小数丸め
    function floorNumber (num, digit) {
        if (digit === undefined) {
            digit = 2;
        }
        var magic = Math.pow(10, digit);
        return Math.floor(num * magic) / magic;
    };


    /**
        Q Learning.
    */
    window.QLearn = function (size, maze) {
        this.q = [];
        this.size = size;
        this.maze = maze;
        this.actions = ["top", "left", "bottom", "right"];
        this.displayInterval = 16;
        this.initialize();
    }
    var p = QLearn.prototype;


    /**
        initialize Q-factor to 0.
    */
    p.initialize = function () {
        this.q = [];
        for (var i = 0; i < this.size; i++) {
            var row = [];
            this.q.push(row);
            for (var j = 0; j < this.size; j++) {
                row.push({top: 0, left: 0, bottom: 0, right: 0});
            }
        }
        this.pos = [0, 0];
        this.goal = [this.size - 1, this.size - 1];
        // console.debug("Q:", this.q);
        // console.debug("pos:", this.pos);
        // console.debug("goal:", this.goal);
    }

    /**
        学習する
    */
    p.learn = function () {

        console.debug("******");
        console.debug("pos:", this.pos);

        // 終了判定
        if (this.pos[0] === this.goal[0] && this.pos[1] === this.goal[1]) {
            this.iterCount++;
            this.actCount = 0;
            this.pos = [0, 0];
            return this._doNext();
        }
        if (this.iterCount >= this.maxIter) {
            return this._finishAction();
        }
        if (this.actCount >= this.maxAct) {
            this.iterCount++;
            this.actCount = 0;
            this.pos = [0, 0];
            return this._doNext();
        }

        // 行動をインクリメント
        this.actCount++;

        // アクションを選択する
        var action = this.selectAction(this.pos);
        this.currentAction = action;
        console.debug("action:", action);

        // 環境から報酬を受け取る
        var rewardAndState = this.getRewardAndNextState(this.pos, action);
        var reward = rewardAndState[0];
        var nextPos = rewardAndState[1];
        // console.debug(this.pos, action, reward, nextPos);
        console.debug("reward:", reward);
        console.debug("nextpos:", nextPos);

        // Q値を更新する
        this.updateQValue(this.pos, action, reward, nextPos);
        // console.debug('update: ', this.q[this.pos[0]][this.pos[1]][action]);

        // 位置を更新する
        this.pos = nextPos;

        // エージェントの位置を表示する
        this.maze.showAgent(this.pos);

        // Q値表示
        this._showQValue();

        // 次へ
        this._doNext();
    }

    /**
        Q値を更新する
        // Q(s<t>,a<t>) <- (1 - α)Q(s<t>,a<t>) + α[r<t> + γ * max(Q(<s+1>, a))]        
    */
    p.updateQValue = function (pos, action, reward, nextPos) {

        var qValue = this.q[pos[0]][pos[1]][action];

        // 次のPosの最大報酬を見つける
        var nextMaxReward = -999;
        var nextQ = this.q[nextPos[0]][nextPos[1]];
        for (act in nextQ) {
            if (nextMaxReward < nextQ[act]) {
                nextMaxReward = nextQ[act];
            }
        }

        var newQValue = (1 - this.alpha) * qValue + this.alpha * (reward + this.gampa * nextMaxReward);
        // console.debug("newQValue: ", newQValue);
        this.q[pos[0]][pos[1]][action] = newQValue;
        // console.debug(this.q[pos[0]][pos[1]]);
    }

    /**
        行動を起こして環境から報酬を受け取る
    */
    p.getRewardAndNextState = function (pos, action) {

        posMaze_x = pos[0] + 1;
        posMaze_y = pos[1] + 1;
        console.debug('maze: ', posMaze_x, posMaze_y);

        switch (action) {
            case 'top':
                console.debug("---- top");
                // 壁
                if (this.maze.box[posMaze_x][posMaze_y - 1] === 0) {
                    console.debug("-- wall");
                    return [this.penalty, pos];
                // ゴール
                } else if (pos[0] === this.goal[0] && (pos[1] - 1) === this.goal[1]) {
                    console.debug("-- goal");
                    return [this.goalReward, [pos[0], pos[1]-1]];
                // 通路
                } else {
                    console.debug("-- pass");
                    return [this.backPenalty, [pos[0], pos[1]-1]];
                }
                break;
            case 'bottom':
                console.debug("---- bottom");
                // 壁
                if (this.maze.box[posMaze_x][posMaze_y + 1] === 0) {
                    console.debug("-- wall");
                    return [this.penalty, pos];
                // ゴール
                } else if (pos[0] === this.goal[0] && (pos[1] + 1) === this.goal[1]) {
                    console.debug("-- goal");
                    return [this.goalReward, [pos[0], pos[1]+1]];
                // 通路
                } else {
                    console.debug("-- pass");
                    return [this.passReward, [pos[0], pos[1]+1]];
                }
                break;
            case 'left':
                console.debug("---- left");
                // 壁
                if (this.maze.box[posMaze_x - 1][posMaze_y] === 0) {
                    console.debug("-- wall");
                    return [this.penalty, pos];
                // ゴール
                } else if ((pos[0] - 1) === this.goal[0] && pos[1] === this.goal[1]) {
                    console.debug("-- goal");
                    return [this.goalReward, [pos[0]-1, pos[1]]];
                // 通路
                } else {
                    console.debug("-- pass");
                    return [this.backPenalty, [pos[0]-1, pos[1]]];
                }
                break;
            case 'right':
                console.debug("---- right");
                // 壁
                if (this.maze.box[posMaze_x + 1][posMaze_y] === 0) {
                    console.debug("-- wall");
                    return [this.penalty, pos];
                // ゴール
                } else if ((pos[0] + 1) === this.goal[0] && pos[1] === this.goal[1]) {
                    console.debug("-- goal");
                    return [this.goalReward, [pos[0]+1, pos[1]]];
                // 通路
                } else {
                    console.debug("-- pass");
                    return [this.passReward, [pos[0]+1, pos[1]]];
                }
                break;
            default:
                // ありえないはず
                console.error("default???");
                return [0, pos];
        }
    }



    /**
        アクションを選択する（ε-グリーディー戦略）  
    */
    p.selectAction = function (pos) {
        var q = this.q[pos[0]][pos[1]];
        
        // イプシロン
        var epsilon = this._getEpsilon();

        // explore
        if (Math.random() <= epsilon) {
            this.actionType = 'non-greedy';
            return shuffle(this.actions)[0];
        // greedy
        } else {
            this.actionType = 'greedy';
            var maxVal  = -999, maxAction = "top";
            // シャッフルしないと、q=0の場合に同じものばかり選ばれる
            shuffle(this.actions).forEach(function (action) {
                if (maxVal < q[action]) {
                    maxAction = action;
                    maxVal = q[action];
                }
            });
            return maxAction;
        }
    }

    /**
        ε取得
    */
    p._getEpsilon = function () {
        var base = this.maxIter * this.maxAct;
        var epsilon = this.epsilon - (this.iterCount * this.maxAct + this.actCount) / base;
        epsilon = Math.max(0, epsilon);
        this.currentEpsilon = epsilon;
        return epsilon;
    }

    /**
        学習設定
    */
    p.learningSetting = function () {
        // reward
        this.penalty = -10;       // 壁にぶつかったら-1
        // this.backPenalty = -1;   // 戻ると-1
        this.backPenalty = 0;   // 戻ると-1
        // this.passReward = 1;     // 進めば+1
        this.passReward = 0;     // 進めば+1
        this.goalReward = 100;   // ゴールに達したら+100
        // settings
        this.alpha = 0.3;        // learning rate.
        this.gampa = 0.9;        // discount rate.
        this.epsilon = 1;      // ε-グリーディー戦略
        this.maxIter = Math.floor(Math.max(40, Math.pow(this.size, 2.5)));     // 学習回数
        this.maxAct  = this.maxIter;     // 学習1回あたりの最大行動回数
        this.iterCount = 0;      // 現在の学習回数
        this.actCount = 0;       // 現在の行動カウント
    }


    /**
        Greedy行動のみの設定
    */
    p.greedySetting = function () {
        // settings
        this.alpha = 0;        // learning rate.
        this.gampa = 0;        // discount rate.
        this.epsilon = 0;      // ε-グリーディー戦略
        this.maxIter = 1;     // 学習回数
        this.maxAct  = Math.pow(this.size);     // 学習1回あたりの最大行動回数
        this.iterCount = 0;      // 現在の学習回数
        this.actCount = 0;       // 現在の行動カウント
        this.pos = [0, 0];
    }

    /**
        次の行動を行う
    */
    p._doNext = function () {
        var that = this;
        setTimeout(function () {
            console.debug("iter:", that.iterCount, ", act:", that.actCount);
            that.learn();
        }, this.displayInterval);
    }

    /**
        終了処理
    */
    p._finishAction = function () {
        console.debug("finish");
        this._showQValue();

    }


    /**
        Q値を表示する
    */
    p._showQValue = function () {
        // iteration
        var snipet = '';
        snipet += 'maxIter=' + this.maxIter + ', iter=' + this.iterCount + ', maxAct=' + this.maxAct + ', act=' + this.actCount + ', action=' + this.currentAction + '<br>actionType=' + this.actionType + '<br>epsilon=' + this.currentEpsilon;
        document.querySelector("#console1").innerHTML = snipet;
        // actions
        var snipet = '';
        var actions = ['top', 'left', 'bottom', 'right'];
        for (var i = 0; i < this.size; i++) {
            snipet += '<tr>';
            for (var j = 0; j < this.size; j++) {
                // i is col, j is row
                if (this.pos[0] === j && this.pos[1] === i) {
                    snipet += '<td class="current">';    
                } else {
                    snipet += '<td>';                    
                }
                snipet += 'x=' + i + ', y=' + j + '<br>';
                var that = this;
                actions.forEach(function (action) {
                    // i is col, j is row
                    var val = that.q[j][i][action];
                    if (val < 0) {
                        snipet += '  ' + action + '\t: q=<span class="red">' + floorNumber(val) + '</span><br>';
                    } else {
                        snipet += '  ' + action + '\t: q=<span class="">' + floorNumber(val) + '</span><br>';
                    }
                });
                snipet += '</td>';
            }
            snipet += '</tr>';
        }
        document.querySelector("#console2").innerHTML = snipet;        
    }







})();