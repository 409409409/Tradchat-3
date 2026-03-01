import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ast
import getpass

# Gmail SMTP configuration
EMAIL_ADDRESS = "tradchatforkids@gmail.com"


APP_PASSWORD = input("Enter Gmail App Password: ")


def send_email(recipient_email, recipient_first_name, recipient_last_name):
    """Send email to a single recipient"""
    
    # Email content
    subject = "🎨 We're Back! The Tradchat Art Contest is LIVE!"
    
    body = f"""Hey {recipient_first_name} {recipient_last_name}!

We know we've been quiet for a few months, but we're officially back and ready to get serious. We missed all the energy of this community and we're excited to become more involved.

While we are currently working on a better TradChat with capacity for more features and members, we want to bring the old TradChat back to its former days in waiting time.

The Art Contest (Hosted by Julianne):
If one desire burns our souls most it is desire, as Catholics, to bring beauty and truth into this dark world. Everyone has that spark in them, and this contest is a perfect chance to let your Catholic artist out of you as we explore some of the greatest mysteries of our religion (spoiler alert...)

TradChat 3 (in-progress):
Since we don't email much we want to take this time to pre-answer some likely questions about TradChat 3:

Why is it called TradChat 3?:
This name has been thrown around a lots. The reason is because, before TradChat you know, we had a first prototype which frankly, failed.

Why have I heard about this for a year and a half but seen nothing yet?:
Before earlier this year our team primarily consisted of two people who couldn't take on the task since due to starting college.
However with a larger team and better technology new projects are now feasible.

What features will TradChat 3 have that TradChat 2 will not?:
This has yet to be seen. The main reason we want it is for a better website structure where weak foundations and servers won't cause it to crash every few weeks. Since you're receiving this email it means you have an account with us, but in the past we had over 80 people who our server lost track of, they won't even receive this email because of our infamous September Crash.

In addition though, we plan on having a more attactive design along with new features and fun things on the new TradChat as well.

If you have any questions about the contest or new site, reach out to us at: tradchatforkids@gmail.com

Stay tuned—big things are coming.

God bless,

The TradChat Team"""

    # Create message
    message = MIMEMultipart()
    message["From"] = EMAIL_ADDRESS
    message["To"] = recipient_email
    message["Subject"] = subject
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Create SMTP session
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        
        # Login with app password
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        
        # Send email
        text = message.as_string()
        server.sendmail(EMAIL_ADDRESS, recipient_email, text)
        server.quit()
        
        print(f"✅ Email sent successfully to {recipient_email}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email to {recipient_email}: {e}")
        return False

def main():
    """Main function to send emails to all accounts"""
    
    print("🚀 Starting TradChat Art Contest Email Campaign...")
    
    with open('accounts.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Parse the content as a Python list/dictionary structure
    # Assuming the file contains something like: [{'Michael': [data1, data2, data3, data4, data5, data6, email]}, ...]
    accounts = eval(content)
    
    if not accounts:
        print("❌ No accounts found in accounts.txt!")
        return
    
    print(f"📧 Found {len(accounts)} accounts to email")
    
    # Send emails to each account
    success_count = 0
    fail_count = 0
    
    for account in accounts:
        print(f"\n📨 Processing account: {account}")
        
        # Extract email, first name, and last name
        # Based on your description: email is 7th, first name is 3rd, last name is 4th
        try:
            # Extract data from the account structure
            account_data = accounts[account]  # This is the list [data1, data2, data3, data4, data5, data6, email]
            
            email = account_data[7]  # 7th item (index 6)
            first_name = account_data[4]  # 3rd item (index 2)
            last_name = account_data[5]  # 4th item (index 3)
            
            print(f"   Email: {email}")
            print(f"   Name: {first_name} {last_name}")
            
            if email and first_name and last_name:
                if send_email(email, first_name, last_name):
                    success_count += 1
                else:
                    fail_count += 1
            else:
                print(f"   ❌ Missing required fields for account {account}")
                fail_count += 1
                
        except Exception as e:
            print(f"   ❌ Error processing account: {e}")
            fail_count += 1
    
    # Print summary
    print(f"\n📊 Email Campaign Summary:")
    print(f"   ✅ Successfully sent: {success_count}")
    print(f"   ❌ Failed to send: {fail_count}")
    print(f"   📈 Total processed: {len(accounts)}")
    
    if success_count > 0:
        print(f"\n🎉 Campaign completed! {success_count} TradChatters notified about the art contest!")

if __name__ == "__main__":
    main()