import smtplib
import databaseConnection
from email.message import EmailMessage

def sendEmail(selectBillnoEntry):
    meternocheck = None
    meterNole = None
    namele = None
    mobileNole = None
    emaille = None
    addressle = None
    tempunits = None
    creationTime = None
    finalbillamount = None
    selectBillnoEntry = str(selectBillnoEntry)

    conn = databaseConnection.getsqliteconnection()
    cur = conn.cursor()
    cur2 = conn.cursor()

    print(selectBillnoEntry)
    cur2.execute("SELECT * from bills where billNo=?", (selectBillnoEntry,))
    rowss = cur2.fetchall()
    print(rowss, meternocheck, tempunits)
    countt = 0

    for r in rowss:
        meternocheck = r[1]
        tempunits = str(r[2])
        finalbillamount = str(r[3])
        creationTime = str(r[4])
        countt += 1
        print(r[1])



    cur.execute("SELECT * from consumerDetails WHERE meterNo=?", (str(meternocheck)))
    rows = cur.fetchall()
    count = 0
    for row in rows:
        meterNole = str(row[0])
        namele = str(row[1])
        mobileNole = str(row[2])
        emaille = str(row[3])
        addressle = str(row[4])
        count += 1
    print(rows)
    sender_email = "nishantriis@gmail.com"
    tempunits = str(tempunits)
    creationTime = str(creationTime)
    finalbillamount = str(finalbillamount)
    password = "nisshant769"
    # rec_email = str(row[3])

    message = EmailMessage()
    message.set_content(
        'Meter Number:   ' + meterNole + '\nCostumer Name:   ' + namele + '\nMobile Number:   ' + mobileNole + '\nEmail :   ' + emaille + '\nAddress :   ' + addressle + '\nUnits Consumed :   ' + tempunits + '\nBill Generated On :   ' + creationTime + '\nRate :   8 Rupees per Unit' '\nTotal Ammount :   ' + finalbillamount + ' Rupees only')
    rec_email = emaille
    message['Subject'] = 'Electricity Bill'
    message['From'] = sender_email
    message['To'] = rec_email

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    server.login(sender_email, password)
    print("Login success")

    print(message)
    server.send_message(message)

    # server.sendmail(sender_email, rec_email, message)
    print("Email has been sent to ", rec_email)
    server.quit()

# sendEmail()

