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

もし、本パッケージをビルドしていない場合は下記のコマンドを実行してください
~~~
cd 
cd ~/catkin_ws/
catkin_make
~~~

## 使い方
--- 
gazebo上で動かす場合

ターミナルを開き、次のようなコマンドを実行します
~~~
roslaunch crane_x7_gazebo crane_x7_hand.launch
~~~
実行すると次のような状態になっていれば成功です
<img src = "https://user-images.githubusercontent.com/72371137/102042393-173c5f80-3e15-11eb-872f-88d2ea6e82e5.png" width = 70%>

gazeboが起動したら、別のターミナルを開き、下記のコマンドを実行
~~~
~~~

実機で動かす場合

下記リンク先の手順に従って実機と接続します

[実機との接続の仕方](#実機を使う場合)

接続出来たら、次のコマンドを実行し、realsenseを起動させます
~~~
roslaunch realsense2_camera rs_camera.launch 
~~~
起動後、別のターミナルを開き
~~~

~~~
実機と手の距離

## プログラム一覧
--- 
- [choki.py](#choki.py)
- [gu.py](#gu.py)
- [par.py](#par.py)
- [hand_action.py](#hand_action.py)
- [main2.py](#main2.py)
- [main_node2.py](#main_node2.py)
- [main_node3.py](#main_node3.py)
- [par_new.py](#par_new.py)
- [pose2.py](#pose2.py)
- [pose3.py](#pose3.py)

※これらのプログラムを単体で動かしたい場合はプログラム内の#rospy.init_node("gripper_action_cliant")と書いてある行の＃を消してください

---
choki.py\
gu.py\
par.py\
par_new.py

アームが出せる手のプログラムです

---
hand_action.py

悔しがる動きをさせるプログラムです

---
main_node2.py\
main_node3.py\
main2.py

crane_x7がじゃんけんで負けてくれるプログラムです

数字が違うプログラムだと動きが違います\
main_node2.py main_node3.py でエラーが起きたときはmain2.pyを実行してください
~~~
rosrun crane_x7_example (実行したいプログラム)
~~~

---
pose2.py\
pose3.py

最初はグー～～ポンまでの動きをするプログラムです

