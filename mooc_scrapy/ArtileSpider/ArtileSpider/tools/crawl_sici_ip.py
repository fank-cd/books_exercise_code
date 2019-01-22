# coding:utf-8
import requests
from scrapy.selector import Selector
import MySQLdb
from random import randrange
from time import sleep
conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="1234",db="article_spider",charset="utf8")
cursor = conn.cursor()


def crawl_ips():

    # 爬取西刺的免费IP代理
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
    headers = {
        "HOST": "www.xicidaili.com",
        "Referer": "https://www.xicidaili.com",
        "User-Agent": agent
    }

    for i in range(1500):
        re = requests.get("https://www.xicidaili.com/nn/{0}".format(i), headers=headers)

        selector = Selector(text=re.text)
        all_trs = selector.xpath(".//table[@id='ip_list']/tr")
        # print(all_trs)
        # all_trs = selector.css("#ip_list tr")
        ip_list = []
        for tr in all_trs[1:]:
            speed_atr = tr.xpath(".//div[@class='bar']/@title").extract()[0]
            if speed_atr:
                speed = float(speed_atr.split("秒")[0])
            all_texts = tr.css("td::text").extract()
            ip = all_texts[0]
            port = all_texts[1]
            proxy_type = all_texts[5]

            ip_list.append((ip, port, proxy_type, speed))
            print(all_texts)
        for ip_info in ip_list:
            cursor.execute(
                "insert proxy_ip(ip,port,speed,proxy_type) VALUES('{0}','{1}',{2},'HTTP')".format(
                    ip_info[0], ip_info[1], ip_info[3], ip_info[2]
                )
            )

            conn.commit()
            sleep(randrange(2, 10))

            # speed = tr.css(".bar::attr(title)").extract()
        # print(re.text)


class GetIP(object):
    def delete_ip(self,ip):
        delete_sql = """
            delete from proxy_ip where ip ='{0}'
        
        """.format(ip)

        cursor.execute(delete_sql)
        conn.commit()
        return True

    def judge_ip(self, ip, port):
        # 判断IPs会否可用
        http_url = "http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip, port)
        try:
            proxy_dict = {
                "http": proxy_url,
            }

            response = requests.get(http_url, proxies=proxy_dict)
        except Exception as e:
            print("invail ip and port")
            self.delete_ip(ip)
            return False

        else:
            code = response.status_code
            if code >=200 and code < 300:
                print("effective ip")
                return True

            else:
                print("invalid ip and port")
                return False
                self.delete_ip(ip)
                return False


    def get_random_ip(self):
        # 从数据库中随机获取一个可用的IP

        random_sql = """
        SELECT ip,port FROM proxy_ip
        ORDER BY RAND()
        LIMIT 1
        """

        result = cursor.execute(random_sql)

        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]

            judge_re = self.judge_ip(ip, port)
            if judge_re:
                return "http://{0}:{1}".format(ip,port)
            else:
                return self.get_random_ip()


# crawl_ips()
if __name__ == '__main__':
    get_ip = GetIP()
    ip = get_ip.get_random_ip()
