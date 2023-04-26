import subprocess

'''
对象结构型适配器
'''


class ExecuteCmd:
    def __init__(self, cmd):
        self.cmd = cmd

    def cmd_exe(self):
        result = ''
        result_code = 0
        try:
            result = subprocess.check_output(self.cmd, shell=True)
        except subprocess.CalledProcessError as e:
            result_code = 1
        return result, result_code


class NewCmd:
    def __init__(self, cmd):
        self.cmd = cmd

    def run_cmd(self):
        result = ''
        result_code = 0
        try:
            result = subprocess.check_output(self.cmd, shell=True)
        except subprocess.CalledProcessError as e:
            result_code = 1
        return result, result_code


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.obj.__dict__.update(adapted_methods)

    def __getattr__(self, item):
        return self.obj.__dict__[item]


# 旧接口可以不适配
old_obj = ExecuteCmd('calc').cmd_exe()

# 新接口需要适配
new_obj = NewCmd('calc')
trans_obj = Adapter(new_obj, dict(cmd_exe=new_obj.run_cmd))
# 适配完成，可以和旧系统一样使用cmd_exe执行命令
trans_obj.cmd_exe()

'''
类结构型适配器，使用一个新类去适配旧系统的接口
1. 创建一个新的类
2. 继承需要进行转换的类
3. 在新的类中实现旧系统的接口
'''


class AdapterClass(NewCmd):
    def cmd_exe(self):
        '''直接在适配器中实现旧系统的接口'''
        return self.run_cmd()


new_boj_class = AdapterClass('calc').cmd_exe()
