[English](README.en.md) | [日本語](README.md)

# crane_x7_examples

CRANE-X7のためのパッケージ、3班の発表で使うプログラムをまとめたパッケージです。

## システムの起動方法

CRANE-X7の制御信号ケーブルを制御用パソコンへ接続します。
Terminalを開き、`crane_x7_bringup`の`demo.launch`を起動します。
このlaunchファイルには次のオプションが用意されています。

- fake_execution (default: true)

実機を使用する/使用しない

### シミュレータを使う場合

実機無しで動作を確認する場合、
制御信号ケーブルを接続しない状態で次のコマンドを実行します。

```sh
roslaunch crane_x7_bringup demo.launch fake_execution:=true
```

### 実機を使う場合

実機で動作を確認する場合、
制御信号ケーブルを接続した状態で次のコマンドを実行します。

```sh
roslaunch crane_x7_bringup demo.launch fake_execution:=false
```

ケーブルの接続ポート名はデフォルトで`/dev/ttyUSB0`です。
別のポート名(例: /dev/ttyUSB1)を使う場合は次のコマンドを実行します。

```sh
roslaunch crane_x7_bringup demo.launch fake_execution:=false port:=/dev/ttyUSB1
```

### Gazeboを使う場合

次のコマンドで起動します。実機との接続やcrane_x7_bringupの実行は必要ありません。

```sh
roslaunch crane_x7_gazebo crane_x7_with_table.launch
```

# playing card picking program 

## インストール方法
---
ターミナルで次のようなコマンドを打つ
~~~ 
git clone https://github.com/mirobo3/mirobo3_3_2020_crane_x7_ros.git
~~~
ホームに戻ってから.gazeboディレクトリに移動し、次のコマンドを実行します
~~~
rm -rf models
git clone https://github.com/mirobo3/models.git 
~~~


これでセットアップ完了です

モデルに関しての説明はこちらです。  
[https://github.com/mirobo3/models/blob/master/README.md](https://github.com/mirobo3/models/blob/master/README.md)

## 使い方
---
gazebo上で動かす場合

Terminalを開き、次のようなコマンドを実行します
~~~
roslaunch crane_x7_gazebo crane_x7_card_stand.launch
~~~

実行すると次のような状態になっていれば成功です

![スクリーンショット 2020-11-15 011604](https://user-images.githubusercontent.com/72371743/99151777-be2bbf80-26e0-11eb-9635-d5e99a318b96.png)

gazeboが起動したら、別のターミナルを開き、下記のコマンドを実行
~~~
rosrun crane_x7_example test.py
~~~

実機で動かす場合

下記リンク先の手順にしたがって実機と接続します

[実機との接続の仕方](#実機を使う場合)

接続したら、次のコマンドを実行します
~~~
rosrun crane_x7_example test2.py
~~~

## ファイル一覧

- arm_move
- arm_move2
- arm_move_card0
- arm_move_card1
- hand_grip
- joint_rotation
- pick1
- pose_groupstae_example
- [test](#test.py)
- [test2](#test2.py)

--- 
## arm_move.py

アームがただ移動するプログラムです

[ファイル一覧に戻る](#ファイル一覧)

---
## arm_move2.py
  card2を掴みに行くプログラム

### arm_move_card0

card0を掴みに行くプログラム

### arm_move_card1

card1を掴みに行くプログラム

[ファイル一覧に戻る](#ファイル一覧)

---

## test.py

gazeboで動かす場合に使うコードです

3枚のトランプからプログラム内で決められたトランプをつかみ、持ち上げ、回し、落とします

下記のコマンドでコードを実行します
~~~
rosrun crane_x7_example test.py
~~~

### test2.py

実機で動かす場合に使うtest.pyの改良コードです

下記のコマンドで実行できます
~~~
rosrun crane_x7_example test2.py
~~~

[ファイル一覧に戻る](#ファイル一覧)

