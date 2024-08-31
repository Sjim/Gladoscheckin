import smtplib
import ssl
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def send_email(sender, receiver, subject, content, smtp_server, smtp_port, username, password):
    # 创建邮件内容
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = formataddr((str(Header('发件人名称', 'utf-8')), sender))
    message['To'] = formataddr((str(Header('收件人名称', 'utf-8')), receiver))
    message['Subject'] = Header(subject, 'utf-8')

    smtp_obj = None
    try:
        # 创建SSL上下文
        context = ssl.create_default_context()

        # 连接到SMTP服务器
        print("正在连接到SMTP服务器...")
        smtp_obj = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)  # 使用SMTP_SSL直接连接到SSL端口
        smtp_obj.set_debuglevel(1)  # 启用调试输出
        smtp_obj.login(username, password)
        print("登录成功")

        # 发送邮件
        smtp_obj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(f"邮件发送失败: {str(e)}")
    finally:
        if smtp_obj:
            try:
                smtp_obj.quit()
            except smtplib.SMTPServerDisconnected:
                pass  # 忽略断开连接的错误


def send(text):
    import datetime

    # 生成当前时间的字符串
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 将时间字符串添加到邮件主题
    email_subject = f"自动签到报告 - {current_time}"
    send_email(
        sender='1225747052@qq.com',
        receiver='522022320096@smail.nju.edu.cn',
        subject=email_subject,
        content=text,
        smtp_server='smtp.qq.com',
        smtp_port=465,  # 使用SSL端口
        username='1225747052@qq.com',
        password='gxbszqaisuwdjdai'  # 使用授权码而不是QQ密码
    )
