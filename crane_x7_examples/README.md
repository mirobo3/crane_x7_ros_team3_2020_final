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

realsenseをgazebo上で使えるようにパッケージをgitcloneします
~~~
cd ~/catkin_ws/src
git clone https://github.com/mirobo3/crane_x7_d435.git
~~~


もし、本パッケージをビルドしていない場合は下記のコマンドを実行してください
~~~
cd 
cd ~/catkin_ws/
catkin_make
source ~/catkin_ws/devel/setup.bash
~~~

## 使い方
--- 
gazebo上で動かす場合

ターミナルを開き、次のようなコマンドを実行します
~~~
roslaunch crane_x7_d435 bringup_sim_test.launch
~~~
実行すると次のような状態になっていれば成功です
<img src = https://user-images.githubusercontent.com/72371743/102318912-6fae6100-3fbd-11eb-8668-d3b5d1629f96.png width =500px />

gazeboが起動したら、別のターミナルを開き、下記のコマンドを実行
~~~
rosrun image cvbridge_hand_gesture_subpub_python.py
rosrun crane_x7_examples main_node3.py
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
rosrun image cvbridge_hand_gesture_subpub_python.py
rosrun crane_x7_examples main_node3.py
~~~
実機と手の距離は以下の画像のようになるべく四角の中に手の全体が入るようにしてください   
<img src=https://user-images.githubusercontent.com/72371743/102319767-b81a4e80-3fbe-11eb-8ede-5ce5d4336eb4.jpg width=500px />


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

crane_x7がじゃんけんで負けてくれるプログラムです

数字が違うプログラムだと動きが違います\
main_node2.py main_node3.py 
~~~
rosrun crane_x7_example (実行したいプログラム)
~~~

---
pose2.py\
pose3.py

最初はグー～～ポンまでの動きをするプログラムです

