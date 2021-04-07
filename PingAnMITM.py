import mitmproxy.http
from mitmproxy import ctx, http
import json
import datetime

class PingAnMITM:
    def __init__(self):
        # use fake ones
        self.name="bibibi"
        self.stdnum=20187695751
        self.phone=18708647894
        self.qrbegintime=datetime.datetime.now()
        
    def userinfo(self):
        return {
            "userInfo":{
                "id":"000000000000000000",
                "creationTime":1568019081390,
                "lastUpdateTime":1568019081486,
                "creator":"stateless action",
                "lastEditor":"stateless action",
                "extend":"{\"obgrpId\":\"000000000000000000\",\"obgrpName\":\"硕士研究生\",\"edtime\":\"20251231\"}",
                "name":self.name,
                "loginId":str(self.stdnum),
                "password":"",
                "salt":"",
                "state":1,
                "email":None,
                "mobilePhone":str(self.phone),
                "openIds":"",
                "authType":"【登记】研究生（硕士）",
                "roleList":[
                    {
                        "id":"223485441217662110",
                        "creationTime":1568019081390,
                        "lastUpdateTime":1568019081486,
                        "creator":"3210343",
                        "lastEditor":"3210343",
                        "extend":None,
                        "name":"【角色】学生类登记用户",
                        "description":"",
                        "shiroStr":"stuNormal",
                        "enable":True,
                        "permissions":None
                    }
                ],
                "userGroups":[
                    {
                        "id":"168109806165429102",
                        "creationTime":1554816501128,
                        "lastUpdateTime":1554816501245,
                        "creator":"admin",
                        "lastEditor":"admin",
                        "extend":None,
                        "name":"电子科学与工程学院（示范性微电子学院）",
                        "description":"电子科学与工程学院（示范性微电子学院）",
                        "enable":True,
                        "code":"21",
                        "codeLevel":"1",
                        "roleList":None,
                        "groupTypes":[
                            {
                                "id":"c5343f6a756d4a3ba124090c89656324",
                                "creationTime":1547886703067,
                                "lastUpdateTime":1557846213685,
                                "creator":"admin_lz",
                                "lastEditor":"3210343",
                                "extend":None,
                                "name":"org",
                                "description":"【用户分组】单位（系统内置）"
                            }
                        ],
                        "institution":None
                    },
                    {
                        "id":"168103607646817657",
                        "creationTime":1554815023289,
                        "lastUpdateTime":1561709597789,
                        "creator":"admin",
                        "lastEditor":"3210343",
                        "extend":None,
                        "name":"【登记】研究生（硕士）",
                        "description":"【登记】研究生（硕士）",
                        "enable":True,
                        "code":"14",
                        "codeLevel":"1",
                        "roleList":None,
                        "groupTypes":[
                            {
                                "id":"19575e0a41e14ba6a664080d234bc1a6",
                                "creationTime":1548645587918,
                                "lastUpdateTime":1557846115462,
                                "creator":"admin",
                                "lastEditor":"3210343",
                                "extend":None,
                                "name":"reg",
                                "description":"【用户分组】登记（系统内置）"
                            }
                        ],
                        "institution":None
                    }
                ],
                "adapterList":[
                    {
                        "id":"1",
                        "creationTime":None,
                        "lastUpdateTime":None,
                        "creator":None,
                        "lastEditor":None,
                        "extend":None,"code":"uestc-portal",
                        "name":"uestc-portal",
                        "description":"uestc-portal",
                        "authServiceUrl":"http://smaco-authslot:5000",
                        "inst":"00000000000000000000000000000000",
                        "usrgrpPid":None
                    }
                ]
            },
            "selfConfig":{
                "currentOrg":{
                    "id":"168109806165429102",
                    "creationTime":1554816501128,
                    "lastUpdateTime":1554816501245,
                    "creator":"admin",
                    "lastEditor":"admin",
                    "extend":None,
                    "name":"电子科学与工程学院（示范性微电子学院）",
                    "description":"电子科学与工程学院（示范性微电子学院）",
                    "enable":True,
                    "code":"21",
                    "codeLevel":"1",
                    "roleList":None,
                    "groupTypes":[
                        {
                            "id":"c5343f6a756d4a3ba124090c89656324",
                            "creationTime":1547886703067,
                            "lastUpdateTime":1557846213685,
                            "creator":"admin_lz",
                            "lastEditor":"3210343",
                            "extend":None,
                            "name":"org",
                            "description":"【用户分组】单位（系统内置）"
                        }
                    ],
                    "institution":None
                },
                "currentReg":{
                    "id":"168103607646817657",
                    "creationTime":1554815023289,
                    "lastUpdateTime":1561709597789,
                    "creator":"admin",
                    "lastEditor":"3210343",
                    "extend":None,
                    "name":"【登记】研究生（硕士）",
                    "description":"【登记】研究生（硕士）",
                    "enable":True,
                    "code":"14",
                    "codeLevel":"1",
                    "roleList":None,
                    "groupTypes":[
                        {
                            "id":"19575e0a41e14ba6a664080d234bc1a6",
                            "creationTime":1548645587918,
                            "lastUpdateTime":1557846115462,
                            "creator":"admin",
                            "lastEditor":"3210343",
                            "extend":None,
                            "name":"reg",
                            "description":"【用户分组】登记（系统内置）"
                        }
                    ],
                    "institution":None
                },
                "currentInst":{
                    "id":"93a1e81bc14e4f0e8deae84b68892bb2",
                    "creationTime":None,
                    "lastUpdateTime":1553859803144,
                    "creator":None,
                    "lastEditor":"3210343",
                    "extend":None,
                    "description":"电子科技大学（University of Electronic Science and Technology of China）坐落于四川省会成都市，直属中华人民共和国教育部，由教育部、工业和信息化部、四川省和成都市共建。位列国家“985工程”、“211工程”、“世界一流大学和一流学科”，入选“2011计划”、“111计划”、“卓越工程师教育培养计划”、“国家建设高水平大学公派研究生项目”、“中国政府奖学金来华留学生接收院校”，两电一邮成员。是一所完整覆盖整个电子类学科，以电子信息科学技术为核心，以工为主，理工渗透，理、工、管、文、医协调发展的多科性研究型全国重点大学，被誉为“中国电子类院校的排头兵”。",
                    "name":"电子科技大学",
                    "code":"10614"
                }
            },
            "groupIds":"168109806165429102,168103607646817657"
        }

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host != "smaco2.uestc.edu.cn":
            return
            
        ctx.log.warn("path: %s" % flow.request.path)
        if flow.request.path.startswith("/shiroApi/wx/getWxSession"):
            resp={
                "status":1,
                "msg":"登录成功",
                "data":{
                    "Authorization":"00000000-0000-0000-0000-000000000000",
                    "name":self.name,
                    "username":str(self.stdnum),
                },
                "expire":0,
            }
            ctx.log.warn("got getWxSession")
            flow.response = http.HTTPResponse.make(200, json.dumps(resp))
            return
        if flow.request.path.startswith("/shiroApi/selfInfo"):
            resp={
                "status":1,
                "msg":"200 OK",
                "data":self.userinfo(),
                "expire":0
            }
            ctx.log.warn("got selfinfo")
            flow.response = http.HTTPResponse.make(200, json.dumps(resp))
            return
        if flow.request.path.startswith("/pipe/pass/getObjectQrcode"):
            qrtime=(self.qrbegintime-datetime.datetime.now()).seconds
            if qrtime<=0 or qrtime>1000:
                qrtime=300
                self.qrbegintime=datetime.datetime.now()+datetime.timedelta(seconds=qrtime)
            resp={
                "status":1,
                "msg":"200 OK",
                "data":{
                    "type":1,
                    "picPath":"12345",
                    "ttl":qrtime
                },
                "expire":0
            }
            ctx.log.warn("got getObjectQrcode")
            flow.response = http.HTTPResponse.make(200, json.dumps(resp))
            return
        if flow.request.path.startswith("/qrcode12345"):
            ctx.log.warn("got qrcode")
            with open("code.png", "rb") as f:
                flow.response = http.HTTPResponse.make(200, f.read())
            return
        if flow.request.path.startswith("/passObjectApi/temp/sign"):
            if "controllerId" not in flow.request.query.keys():
                ctx.log.warn("can not get controllerId from %s" % flow.request.pretty_url)
                flow.response = http.HTTPResponse.make(404)
                return
            if flow.request.query["controllerId"]=="1000020$7$0$0": # out
                resp={
                    "status":1,
                    "msg":"研究生用户，出校登记成功！",
                    "data":{
                        "id":"000000000000000000",
                        "creationTime":None,
                        "lastUpdateTime":None,
                        "creator":None,
                        "lastEditor":None,
                        "passTimeServer":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        "passStatus":"研究生用户，出校登记成功！",
                        "controllerId":"1000020$7$0$0",
                        "loginId":str(self.stdnum),
                        "auditType":"",
                        "userInfo":json.dumps(self.userinfo())
                    }
                }
                ctx.log.warn("got sign out")
                flow.response = http.HTTPResponse.make(200, json.dumps(resp))
                return
            elif flow.request.query["controllerId"]=="1000017$7$0$0": # in
                resp={
                    "status":1,
                    "msg":"研究生用户，入校授权有效！",
                    "data":{
                        "id":"000000000000000000",
                        "creationTime":None,
                        "lastUpdateTime":None,
                        "creator":None,
                        "lastEditor":None,
                        "passTimeServer":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        "passStatus":"研究生用户，入校授权有效！",
                        "controllerId":"1000017$7$0$0",
                        "loginId":str(self.stdnum),
                        "auditType":"",
                        "userInfo":json.dumps(self.userinfo())
                    }
                }
                ctx.log.warn("got sign in")
                flow.response = http.HTTPResponse.make(200, json.dumps(resp))
                return
            else:
                ctx.log.warn("unknown controllerId %s" % flow.request.query["controllerId"])
                flow.response = http.HTTPResponse.make(404)
                return

addons = [
    PingAnMITM()
]
