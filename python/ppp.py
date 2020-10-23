import requests
from fake_useragent import UserAgent

############## 数据存储
import time


##################################

class ZhihuOne(object):

    def __init__(self,totle):

        self._offset = 0
        self._totle = totle
        #self._ua = UserAgent()


    def run(self):

        print("正在抓取 {} 数据".format(self._offset))
        headers = {
            "upgrade-insecure-requests":"1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"
        }
        # 406321189
        with requests.Session() as s:
            try:
                with s.get("https://www.zhihu.com/api/v4/questions/406321189/answers?include=comment_count,content,voteup_count,reshipment_settings,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset={}&sort_by=default".format(self._offset),headers=headers,timeout=3) as rep:
                    data =  rep.json()
                    if data:
                        print(data["data"][0])
            except Exception as e:
                print(e.args)

            finally:

                if self._offset <= self._totle:
                    self._offset  = self._offset + 5 # 每次+5
                    print("防止被办，休息3s")
                    time.sleep(3)
                    self.run()
                else:
                    print("所有数据获取完毕")




if __name__ == '__main__':
    # 偏移量是0,5,10   i=1  (i-1)*5
    zhi = ZhihuOne(1084)  
    zhi.run()