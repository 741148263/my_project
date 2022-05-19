from send_mail import EmailHandler
from utils import parse_input_args, user_info_encode

if __name__ == '__main__':
    config = parse_input_args()
    if config.encrypt:
        security_key = user_info_encode(*config.encrypt.split(";"))
        print(security_key, file=open("SECURITY_KEY.txt", "w"))
        print("秘钥已生成，请将SECURITY_KEY.txt文件中的秘钥保存在SECURITY_KEY环境变量中。")
    else:
        EmailHandler(config).sendmail()
