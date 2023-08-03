#!/usr/bin/env python3

# モジュールのインポート
import rospy
from ros_practice_msgs.msg import Person

# クラスの定義
class Talker():
    # コンストラクタの定義
    def __init__(self):
        # パブリッシャの生成
        # トピック名、メッセージの型、キューサイズ
        self.person_pub = rospy.Publisher("/person", Person, queue_size=10)
    
    # メッセージをパブリッシュする関数
    def publish(self):
        # 送るメッセージの定義
        msg = Person()
        msg.name = "上田 隆一"
        msg.age = 45
        msg.hobbies = ["確率ロボティクス", "シェル芸"]
        
        # メッセージをパブリッシュする
        self.person_pub.publish(msg)
        
        # 見やすいように整える
        # 多分もっと賢いやり方があるはず...
        hobbies = f"{msg.hobbies[0]}、{msg.hobbies[1]}"
        
        # 画面に表示
        rospy.loginfo(f"私は{msg.name}、{msg.age}歳！趣味は{hobbies}!")  

if __name__ == "__main__":
    # ノードの生成
    rospy.init_node("custom_talker_node")
    
    # クラスのインスタンス化
    talker = Talker()
    
    # ループの周期
    # この場合1Hz、1秒に1回
    rate = rospy.Rate(1)
    
    # ROSが立ち上がっている間は...
    while not rospy.is_shutdown():
        # メッセージをパブリッシュする
        talker.publish()
        
        # 定義した周期になるように一定時間待つ
        rate.sleep()
