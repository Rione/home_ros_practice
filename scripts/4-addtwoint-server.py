#!/usr/bin/env python3

# モジュールのインポート
import rospy
from ros_practice_msgs.srv import AddTwoInt, AddTwoIntResponse

# クラスの定義
class Server():
    # コンストラクタの定義
    def __init__(self):
        # サービスの定義
        # サービス名、メッセージの型、データを受け取ったら実行する関数
        self.addint_srv = rospy.Service("/addtwoint", AddTwoInt, self.callback)
    
    # コールバック関数の定義
    def callback(self, req):
        # 画面に表示
        rospy.loginfo(f"Recieved x = {req.x} y = {req.y}")
        
        # サービスの返り値の定義
        res = AddTwoIntResponse()
        res.z = req.x + req.y
        
        # 画面に表示
        rospy.loginfo(f"Sending z = {res.z}")
        
        # 値を返す
        return res

if __name__ == "__main__":
    # ノードの生成
    rospy.init_node("addtwoint_server_node")
    
    # クラスのインスタンス化
    server = Server()
    
    # Ctrl-Cが押されるまで実行
    rospy.spin()
