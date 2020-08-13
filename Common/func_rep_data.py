import re
from Common.func_option import conf


class EnvData:
    pass


def rep_data(case_data, mark, real_data):
    for key, value in case_data.items():
        if value is not None and isinstance(value, str):
            if value.find(mark) != -1:
                case_data[key] = value.replace(mark, real_data)
    return case_data


def req_data_by_re(data):
    res = re.findall("#(.*?)#", data)
    if res:
        for item in res:
            try:
                val = conf.get("re_data", item)
            except:
                try:
                    val = getattr(EnvData, item)
                except AttributeError:
                    continue
            data = data.replace("#{}#".format(item), val)
    return data


def clear_EnvData():
    datas= dict(EnvData.__dict__.items())
    for key in datas:
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)

if __name__ == '__main__':
    case = {"name": "这是一个'#name#'的项目", "leader": "可优'#name#'","tester": "某人", "programmer": "某人", "publish_app": "XXX应用", "desc": "xxxx描述"}
    setattr(EnvData, "name", "lalalalal")
    case = req_data_by_re(case)
    print(case)