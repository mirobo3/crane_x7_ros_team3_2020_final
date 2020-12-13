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

# 忖度マニピュレータ（じゃんけん編）

## インストール方法
ターミナルを開き次のコマンドを打ちます
~~~
cd ~/catkin_ws/src
git clone https://github.com/mirobo3/crane_x7_ros_team3_2020_final.git
~~~

シミュレーターを使う場合は次のコマンドを実行してください
  
手のモデルをインストールします
~~~
cd 
cd .gazebo
rm -rf models
git clone https://github.com/mirobo3/models.git
~~~
これでセットアップ完了です

## 使い方
--- 
gazebo上で動かす場合

ターミナルを開き、次のようなコマンドを実行します
~~~
roslaunch crane_x7_gazebo crane_x7_hand.launch
~~~
実行すると次のような状態になっていれば成功です


gazeboが起動したら、別のターミナルを開き、下記のコマンドを実行
~~~
~~~

実機で動かす場合

下記リンク先の手順に従って実機と接続します

[実機との接続の仕方](#実機を使う場合)

接続出来たら、次のコマンドを実行します
~~~
~~~
実機と手の距離

## ファイル一覧
--- 

