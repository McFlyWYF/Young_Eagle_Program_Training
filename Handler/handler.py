import abc


class Manager(metaclass=abc.ABCMeta):
    '''抽象处理者'''

    def __init__(self, name):
        self.superior = None  # 责任链的下一个处理者
        self.name = name

    def setSuperior(self, superior):
        # 设置责任链的下一个处理者
        self.superior = superior

    @abc.abstractmethod
    def handleRequest(self, clientRequest):
        # 处理请求
        pass


class ProjectManager(Manager):
    '''具体处理者：项目经理'''

    def handleRequest(self, clientRequest):
        if clientRequest.applicationType == 'business' and clientRequest.businessDay <= 3:
            return '外出公干%s天，%s审批意见：OK，审批结束' % (clientRequest.businessDay, self.name)
        else:
            print('外出公干%s天，%s审批意见：OK，审批由%s继续处理' % (clientRequest.businessDay, self.name, self.superior.name))
            return self.superior.handleRequest(clientRequest)


class DepartmentHead(Manager):
    '''具体处理者：部门主管'''

    def handleRequest(self, clientRequest):
        if clientRequest.applicationType == 'business' and clientRequest.businessDay <= 7:
            return '外出公干%s天，%s审批意见：OK，审批结束' % (clientRequest.businessDay, self.name)
        else:
            print('外出公干%s天，%s审批意见：OK，审批由%s继续处理' % (clientRequest.businessDay, self.name, self.superior.name))
            return self.superior.handleRequest(clientRequest)


class President(Manager):
    '''具体处理者：总经理'''

    def handleRequest(self, clientRequest):
        if clientRequest.applicationType == 'business':
            return '%s审批意见：OK，审批结束' % self.name


class Client(object):
    '''客户类；发起请求'''

    def __init__(self, applicationType, businessDay):
        self.applicationType = applicationType
        self.businessDay = businessDay

    def submit(self, manager):
        response = manager.handleRequest(self)
        print(response)
        return response


if __name__ == '__main__':
    # 初始化责任链
    project_manager = ProjectManager('项目经理')
    department_head = DepartmentHead('部门主管')
    president = President('总经理')

    project_manager.setSuperior(department_head)  # 项目经理的上级是部门主管
    department_head.setSuperior(president)  # 部门主管的上级是总经理

    # 客户类进行请求
    client = Client(applicationType='business', businessDay=2)
    client.submit(project_manager)
    print('-----------------------request 1 end---------------------------')

    client = Client(applicationType='business', businessDay=6)
    client.submit(project_manager)
    print('-----------------------request 2 end---------------------------')

    client = Client(applicationType='business', businessDay=12)
    client.submit(project_manager)
    print('-----------------------request 3 end---------------------------')
