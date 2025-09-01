# 配置文件，包含直播源URL、黑名单URL、公告信息、EPG URL、测速超时时间和线程池最大工作线程数

# 优先使用的IP版本，这里设置为ipv4
ip_version_priority = "ipv4"

# 直播源URL列表
source_urls = [
    "https://cnb.cool/junchao.tang/live/-/git/raw/main/%E5%85%A8%E7%90%83%E9%80%9A.py",
    "http://kds.shanxixr.com/migu01.txt",
    "http://is.is-great.org/i/0885557.txt",
    "https://115.190.105.236/vip/qwt.m3u",
    "https://115.190.105.236/vip/vip.m3u",
    "https://live.catvod.com/mq.php?catvod.com=m3u",
    "http://is.is-great.org/i/9892017.txt",
    "https://mm.qiuye.us.kg/6.txt",
    "http://gg.7749.org//i/ds.txt",
    "https://is.is-great.org/i/9892017.txt?i=1",
    "http://go8.myartsonline.com/zx/0/TVBTV28.txt",
    "http://kkk.888.3116598.xyz/user/HKTV.txt",
    "http://gg.7749.org/z/i/gdss.txt",
    "https://live.kakaxi-1.ink/ipv4.txt",
    "https://live.kakaxi-1.ink/ipv4.1.txt",
    "https://raw.githubusercontent.com/iodata999/frxz751113-IPTVzb1/refs/heads/main/结果.m3u",
    "http://8.138.7.223/2025.txt",
    "https://cnb.cool/junchao.tang/llive/-/git/raw/main/中国IPTV",
    "https://www.iyouhun.com/tv/myIPTV/ipv6.m3u",
    "https://www.iyouhun.com/tv/myIPTV/ipv4.m3u",
    "http://live.nctv.top/x.txt",   
    "https://live.izbds.com/tv/iptv4.txt",
    "http://47.120.41.246:8899/zb.txt",
    "http://rihou.cc:555/gggg.nzk",
    "http://1.94.31.214/live/livelite.txt",
    "http://api.mytv666.top/lives/free.php?type=txt",
    "http://zhibo.feylen.top/fltv/js/ku9live.php?tpye=fl.txt",
    "http://92.112.21.169:30000/mytv.m3u",
    "http://lisha521.dynv6.net.fh4u.org/tv.txt",
    "https://web.banye.tech:7777/tv/hlj.txt",
    "https://iptv.catvod.com/tv.m3u",
    "https://live.zbds.top/tv/iptv4.txt",
    "https://gitee.com/xxy002/zhiboyuan/raw/master/dsy",
    "https://iptv.laobaitv.net",
    "https://tv-1.iill.top/m3u/Gather",
    "https://fy.188766.xyz/?url=http://mursor.ottiptv.cc&mishitong=false&lunbo=false",

]

# 直播源黑名单URL列表，去除了重复项
url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "http://[2409:8087:1a01:df::7005]:80/ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226419/index.m3u8",
    "http://[2409:8087:5e00:24::1e]:6060/000000001000/1000000006000233001/1.m3u8",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
    "[2409:8087:2001:20:2800:0:df6e:eb22]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb23]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]/ott.mobaibox.com/",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb24]",
    "2409:8087:2001:20:2800:0:df6e:eb25]:80",
    "stream1.freetv.fun",
    "chinamobile",
    "gaoma",
    "[2409:8087:2001:20:2800:0:df6e:eb27]"
]

# 公告信息
announcements = [
    {
        "channel": "更新日期",
        "entries": [
            {
                "name": None,
                "url": "https://codeberg.org/alantang/photo/raw/branch/main/Robot.mp4",
                "logo": "https://codeberg.org/alantang/photo/raw/branch/main/SuperMAN.png"
            }
        ]
    }
]

# EPG（电子节目指南）URL列表
epg_urls = [
    "https://epg.v1.mk/fy.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
# 测速超时时间（秒）
TEST_TIMEOUT = 10

# 测速线程池最大工作线程数
MAX_WORKERS = 20
