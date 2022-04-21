import configparser
import os
import sys
import random
import urllib.request

argv = sys.argv
__ver__ = "1.3"
try:
    a = argv[1]
except:
    argv += [""]


if argv[1] == "update":
    print("正在获取配置")
    try:
        reqs = request = urllib.request.Request("http://www.thisisxd.tk/files/cave.ini", headers={
                                                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"})
        req = urllib.request.urlopen(reqs)
        text = req.read().decode("utf-8")
        with open("config.ini", "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"配置获取失败：{e}")
        sys.exit(1)
    else:
        sys.exit()
elif argv[1] == "help":
    print(f"""CAVE {__ver__} (By This is XiaoDeng) - 帮助
    用法：python3 cave.py [模式] [参数]
    模式列表：
        help            查看此页面
        update          更新配置
        show <id>       查看指定投稿
        search <text>   搜索（来自CAVE SEARCH）
        about           查看帮助
        license         查看开源许可证
    """)
    sys.exit(0)
elif argv[1] == "about":
    print(f"""CAVE {__ver__} (By This is XiaoDeng) - 关于
    版本：{__ver__}
    作者：这里是小邓
    贡献名单：
        XXTG666
            回声洞收集模块
        IT Craft Develop Team 群友
            回声洞投稿
    """)
    sys.exit(0)
elif argv[1] == "license":
    print(f"""Copyright © 2022 This is XiaoDeng
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    """)
    sys.exit(0)
else:
    try:
        proDir = os.path.split(os.path.realpath(__file__))[0]
        configPath = os.path.join(proDir, "config.ini")
        conf = configparser.RawConfigParser(allow_no_value=True)
        conf.read(configPath, encoding="utf-8")
    except:
        print("读取文件失败，请先 python3 cave.py update 后重试")
        sys.exit(1)
    try:
        l = int(conf.get("配置", "回声洞数量"))
        if argv[1] == "search":
            text = argv[2]
            print(f"正在从{l}条回声洞投稿中查找{text}：")
            out = ""
            for i in range(l-1):
                if (text in conf.get(str(i+1), "内容")) or (text in conf.get(str(i+1), "投稿人")) or (text in str(i+1)):
                    out += "[" + str(i+1) + "] "+conf.get(str(i+1),
                                                          "内容")+" ——"+conf.get(str(i+1), "投稿人")
                    out += "\n\n"
            out = out.replace("§", "\n")
        elif argv[1] == "show":
            i = int(argv[2]) - 1
            out = "[" + str(i+1) + "] "+conf.get(str(i+1), "内容") + \
                " ——"+conf.get(str(i+1), "投稿人")
        else:
            i = random.randint(0, l - 1)
            out = "[" + str(i+1) + "] "+conf.get(str(i+1), "内容") + \
                " ——"+conf.get(str(i+1), "投稿人")
        print(out.replace("\\u005b", "[").replace(
            "\\u005d", "]").replace("§", "\n"))
    except Exception as e:
        print("读取文件失败，请先 python3 cave.py update 后重试")
        print(f"错误信息：{e}")
        sys.exit(1)
