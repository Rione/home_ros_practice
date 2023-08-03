#!/usr/bin/env python3

# モジュールのインポート
import rospy
from ros_practice_msgs.msg import Person

# クラスの定義
class Listener():
    # コンストラクタの定義
    def __init__(self):
        # サブスクライバの生成
        # トピック名、メッセージの型、データを受け取ったら実行する関数
        self.text_sub = rospy.Subscriber("/person", Person, self.callback)
    
    # コールバック関数の定義
    def callback(self, msg):
        # 受け取ったメッセージを変数に代入
        name = msg.name
        age = msg.age
        hobbies = msg.hobbies
        
        # 見やすいように整える
        # 多分もっと賢いやり方があるはず...
        hobbies = f"{hobbies[0]}、{hobbies[1]}"
        
        # 画面に表示
        rospy.loginfo(f"あ、あなたは...{name}、{age}歳!趣味は{hobbies}なのか...")

if __name__ == "__main__":
    # ノードの生成
    rospy.init_node("custom_listener_node")
    
    # クラスのインスタンス化
    listener = Listener()
    
    # Ctrl-Cが押されるまで実行
    rospy.spin()
