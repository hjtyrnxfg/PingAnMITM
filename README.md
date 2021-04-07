只适用西门，其他需要自己抓controllerID

名字硬编码在程序里，需要自己改一下

二维码来自 https://github.com/szl0834/PingAnChengDian.git

找一台服务器安装：
```bash
pip install mitmproxy
mitmdump -s PingAnMITM.py -p 9009 --set block_global=false
```
防火墙开启9009端口

手机代理服务器指向刚才配置的服务器。

访问mitm.it，安装根证书。

之后微信正常扫码即可。不用时记得关掉代理。
