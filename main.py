print("================= //Feri Ganteng// ================")
print("""String Session Generator for Telethon and Pyrogram
              (Made by @Xflicks)\n""")

print("""1. Please go-to my.telegram.org
2. Login using your Telegram account
3. Click on API Development Tools
4. Create a new application""")
print("==================================================")
print("What you want to generate? ")
select = input("1. Pyrogram\n2. Telethon\n\n• Enter option (1 or 2): ")

if select == "1":
    print("\n//Generate String Session for Pyrogram Base//")
    APP_ID = int(input("• Enter API ID: "))
    API_HASH = input("• Enter API HASH: ")
    import pyrogram
    import tgcrypto
    with pyrogram.Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as app:
        str_session = app.export_session_string()
        app.send_message(
            "me",
            f"#HU_STRING_SESSION\n\n```{str_session}\n\nGenerate using @UserLazyXBot String Session Generator"
        )
        print("\nDone!, please check your Telegram Saved Messages ")

elif select == "2":
    print("\n//Generate String Session for Telethon Base//")
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    APP_ID = int(input("• Enter API ID: "))
    API_HASH = input("• Enter API HASH: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        str_session = client.session.save()
        client.send_message(
            "me",
            f"#STRING_SESSION\n\n{str_session}```\n\nGenerate using @Xflicks String Session Generator"
        )
        print("\nDone!, please check your Telegram Saved Messages ")

else:
    print("Please only select 1 or 2 ")
