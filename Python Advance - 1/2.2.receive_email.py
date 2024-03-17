import email
import imaplib

# from anup_password import MAIL_PASSWORD

user = 'anupdchavda@gmail.com'

server = imaplib.IMAP4_SSL('imap.gmail.com')

server.login(user, 'asfsdfas')

server.select('inbox')

# status, data = server.search(None, 'ALL')

# status,data = server.search(None,"FROM","ebird","SUBJECT","rare")

status, data = server.search(None, "FROM", "cc.statements")

print(status)
print("DATA", data)
#
mail_ids = []
for block in data:
    # the split function called without parameter
    # transforms the text or bytes into a list using
    # as separator the white spaces:
    # b'1 2 3'.split() => [b'1', b'2', b'3']
    mail_ids += block.split()
#
print(mail_ids)
mail_ids = mail_ids[:1]
#
for i in mail_ids:
    # the fetch function fetch the email given its id
    # and format that you want the message to be
    status, mail_data = server.fetch(i, '(RFC822)')
    print("STAUS", status)
    # print("MAIL DATA", mail_data)
    for response_part in mail_data:
        # so if its a tuple...
        # print("RP", response_part)
        print("RESPION",response_part)
        if isinstance(response_part, tuple):
            # we go for the content at its second element
            # skipping the header at the first and the closing
            # at the third
            message = email.message_from_bytes(response_part[1])
            # print(message)
            #             # with the content we can extract the info about
            #             # who sent the message and its subject
            mail_from = message['from']
            mail_subject = message['subject']
            print("FROM", mail_from)
            print("SUBJECT", mail_subject)
            #             # then for the text we have a little more work to do
            #             # because it can be in plain text or multipart
            #             # if its not plain text we need to separate the message
            #             # from its annexes to get the text
            #             #
            if message.is_multipart():
                print('Multipart types:')
                for part in message.walk():
                    # charset = part.get_content_charset()
                    # print("P", part)
                    # content = part.get_payload(decode=True)
                    # print(content)
                    # content = content.decode(charset).encode('utf-8')
                    # print(content)
                    con_type = part.get_content_type()
                    print("CONTENT TYPE", con_type)
                    if con_type == 'text/plain':
                        print("TP", part.get_payload())
                    elif con_type == 'text/html':
                        print("TH", part.get_payload())
                    elif con_type == 'image/jpeg':
                        print("IJ", part.get_payload())
                    elif con_type == 'application/pdf':
                        print("AP", part.get_payload())
            else:
                print("MSG", message.get_payload())
