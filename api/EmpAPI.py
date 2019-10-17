from day07接口测试人力资源管理系统 import app


class EmpCRUD:
    # 函数1增
    def add(self,session,username,mobile,workNumber):
        myAddEmp={"username":username,'mobile':mobile,
                  'workNumber':workNumber
        }
        return session.post(app.BASE_UEL+'user',json=myAddEmp,
                            headers={"Authorization":"Bearer "+app.TOKEN})
    # 函数2改
    def update(self,session,userId,username):
        return session.put(app.BASE_UEL+'user/'+userId,json={'username':username},
                           headers={"Authorization":"Bearer "+app.TOKEN})
    # 函数3查
    def get(self,session,userId):
        return session.get(app.BASE_UEL+'user/'+userId,
                           headers={"Authorization":"Bearer "+app.TOKEN})
    # 函数4删
    def delete(self,session,userId):
        return session.delete(app.BASE_UEL + 'user/' + userId,
                           headers={"Authorization": "Bearer " + app.TOKEN})