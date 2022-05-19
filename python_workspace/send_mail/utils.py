import argparse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

AUTHOR = "马涛 Email:741148263@qq.com"
EPILOG = f"首次使用，请先配置环境SECURITY_KEY，并重新启动终端工具。在使用过程中，如有问题请联系{AUTHOR}"

SECRET_KEY = "django-insecure-3hmk7^m6t!jn4@6vpq75pht)98agnm!&73inxy5k=4w=63x@yw"
expiration = 60 * 60 * 24 * 365 * 100


def parse_input_args():
    parser = argparse.ArgumentParser(epilog=EPILOG)
    parser.add_argument("-f", "--from_address", default="741148263@qq.com", help="发件人")
    parser.add_argument("-r", "--recipient", default=None, help="收件人，多个收件人请使用';'分隔")
    parser.add_argument("-c", "--CC", default=None, help="抄送人，多个抄送人请使用';'分隔")
    parser.add_argument("-a", "--attachment", default=None, help="发送附件,多个附件请使用';'分隔")
    parser.add_argument("-t", "--traverse", default="False", choices=["True", "False"],
                        help="遍历报告目录下的jpg、png、xlsx、docx、pdf等文件，并将其添加为附件")
    parser.add_argument("-html", "--html_report", default=None, help="html报告路径，可与 -t 参数配合使用")
    parser.add_argument("-e", "--encrypt", default=None, help="首次输入用户名和密码进行加密，并且配置环境变量。格式如下；用户名;密码")
    parser.add_argument("-s", "--subject", default=None, help="邮件主题")
    return parser.parse_args()


def user_info_encode(username, pwd):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return s.dumps({"username": username, "pwd": pwd}).decode()


def _user_info_decode(security_code):
    s = Serializer(SECRET_KEY)
    user_info = s.loads(security_code)
    return user_info["username"], user_info["pwd"]
