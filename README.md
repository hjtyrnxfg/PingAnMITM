只适用西门,西二门（西二门id不确定对不对)，其他需要自己抓controllerID, ~~推荐自己再加一个遇到不认识的controllerID自动显示进校数据的功能，防止突击换二维码之后进不来（欢迎PR）~~ 已实现

~~名字硬编码在程序里，需要自己改一下。这里拦截的API可能多了点。有可能只拦截/passObjectApi/temp/sign就可以用（依旧欢迎PR）~~ 加入了不替换名字的功能，只拦截/passObjectApi/temp/sign。此时行人二维码为真实二维码


内置二维码来自 https://github.com/szl0834/PingAnChengDian.git 

找一台服务器安装：
```bash
pip install mitmproxy
mitmdump -s PingAnMITM.py -p 9009 --set block_global=false --allow-host smaco2.uestc.edu.cn
```
以上命令只拦截smaco2.uestc.edu.cn域名下的数据。天府健康码似乎做了ssl pinning，如果也过代理会打不开

防火墙开启9009端口（端口自行更改）

手机代理服务器指向刚才配置的服务器。

访问mitm.it，安装根证书。

之后微信正常扫码即可。不用时记得关掉代理。
