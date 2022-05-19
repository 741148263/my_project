import mimetypes
import os
import time
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils import _user_info_decode
from smtplib import SMTP

SUPPORT_FILE = [".jpg", ".png", ".pdf", ".docx", ".xlsx"]


class EmailHandler:
    def __init__(self, para):
        self.server = None
        self.para = para
        self.to_user = []
        self.from_user = None
        self.cc = ""
        self.report_path = None
        self.attachments = []
        self.msg = MIMEMultipart()
        self.login()
        self.parse_config()
        self.init_msg()

    def login(self):
        self.server = SMTP(host="smtp.qq.com")
        self.server.login(*_user_info_decode(os.getenv("SECURITY_KEY")))

    def parse_config(self):
        self.from_user = self.para.from_address
        self.to_user = self.para.recipient
        if self.para.html_report:
            if os.path.exists(self.para.html_report):
                self.report_path = self.para.html_report
            else:
                print(f"请检查 【{self.report_path}】 是否存在？")
        if self.para.CC:
            self.cc = self.para.CC
        if self.para.attachment:
            attachments = self.para.attachment.split(";")
            for attachment in attachments:
                if os.path.exists(attachment):
                    self.attachments.append(attachment)
                else:
                    print(f"请检查 【{attachment}】 是否存在？")
        if eval(self.para.traverse):
            if self.report_path:
                for _, _, files in os.walk(os.path.dirname(self.report_path)):
                    for file in files:
                        if os.path.splitext(file)[1] in SUPPORT_FILE:
                            self.attachments.append(os.path.join(os.path.dirname(self.report_path), file))
            else:
                print("没有要遍历的文件夹")

    def init_msg(self):
        self.msg["From"] = self.from_user
        self.msg['To'] = self.to_user
        self.msg["CC"] = self.cc
        self.msg["Subject"] = Header("[请查收]" + f'[{time.strftime("%Y-%m-%d %H:%M:%S")}]' + self.para.subject)

    def sendmail(self):
        if self.report_path:
            with open(self.report_path, "r", encoding="utf-8") as report_file:
                content = report_file.read()
                self.msg.attach(MIMEText(content, "html", "utf-8"))
        if self.attachments:
            for file in self.attachments:
                file_type, coding = mimetypes.guess_type(file)
                if file_type is None or coding is not None:
                    file_type = "application/octet-stream"
                major_type, minor_type = file_type.split("/")
                with open(file, "rb") as attachment_file:
                    if major_type == "image":
                        attachment = MIMEImage(attachment_file.read(), _subtype=minor_type)
                    else:
                        attachment = MIMEApplication(attachment_file.read(), _subtype=minor_type)
                    attachment_name = os.path.basename(file)
                    attachment.add_header("Content-Disposition", "attachment", filename=attachment_name)
                    self.msg.attach(attachment)
        self.server.sendmail(from_addr=self.from_user, to_addrs=self.to_user, msg=self.msg.as_string())

    def quit(self):
        self.server.quit()
