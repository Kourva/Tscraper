<div align="left">
    <img align="left" width=400 src="https://www.v-user.com/images/web-blog/pages/how-to-join-telegram-group-via-link.webp" />
    <h1 align="center">
        Tscraper
    </h1>
    <h4>
        Automated Telegram Scraper that scrapes data when you join the groups
    </h4>
    <div align="center">
      <kbd>
        <img align="center" src="https://img.shields.io/github/license/Kourva/Tscraper?style=flat-square&logo=github&logoColor=%23ff5500&labelColor=black&color=%23ff5500" />
        <img align="center" src="https://img.shields.io/github/languages/code-size/Kourva/Tscraper?style=flat-square&logo=python&logoColor=%23ff5500&labelColor=%23000000&color=%23ff5500" />
        <img align="center" src="https://img.shields.io/github/stars/Kourva/Tscraper?style=flat-square&logo=polestar&logoColor=%23ff5500&labelColor=%23000000&color=%23ff5500" />
       </kbd>
      </div>
</div>

<br><br><br>

# ¶ About
[**Tscraper**](https://github.com/Kourva/Tscraper) is an automated telegram group scraper tool with automated login process (You don't need to enter number or 2fa everytime you run the code). This scraper will run on your account and when you join the group, it will start scraping all members and save it into [SQLite3](https://docs.python.org/3/library/sqlite3.html) database...
*Note*: This tool will not scrape `Hidden Members` in groups!

<br>

# ⌗ Installation
> First of all, make sure you have [python3](https://www.python.org/downloads/) & `git` installed on your machine...
1. **Clone the repository**:
    ```bash
    git clone https://github.com/Kourva/Tscraper
    ```

2. **Navigate to Tcraper and make** [Virtual Environment](https://docs.python.org/3/library/venv.html):
    ```bash
    cd Tscraper && virtualenv venv && source venv/bin/activate
    ```

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

Let's pause the installation and configure some data...

<br>

# ✎ Configuration
For this scraper you need: **`api-ID` || `api-Hash` || `Phone-number` || `2FA password`**
+ Get **api-ID** && **api-Hash**: 
    Get your api-ID and api-Hash from official [Telegram](https://my.telegram.org) website. See [help](https://core.telegram.org/api/obtaining_api_id)

Now open the `credential.json` and replace those data...
```json
{
    "api_id": 11111111,                              // API ID here (Integer)
    "api_hash": "0000000000000000000000000000000",   // API Hash here (Str)
    "phone_number": "+1234567890",                   // Phone Number here (Includes +)
    "password": "test_password"                      // 2FA password (or leave blank)
}
```

**Let's look at our SQLite3 database** (You don't have to do somthing here):
```sql
CREATE TABLE "users" (
    "chat_id"     INTEGER UNIQUE,
    "username"    TEXT,
    "access_hash" TEXT
);
```
**Sample:** Database is located in `Users/tuser.db`<br>

chat_id | username | access_hash 
--- | --- | --- 
102948275 | telegram_user | -12c4qw32wkf12b8339b377 | 
195467618 | None | 91qw382w419500139b1n26 |

<br>

# ★ Start & Run
Now let's start the bot. You can use proxy with proxychains or start it normally...
```bash
python main.py                    # Without proxy
```
```bash
proxychains -q python main.py     # With proxy (Edit proxy in /etc/proxychains4.conf)
```
You just need to type **OTP code** sent to your phone number, after logging, new session with your phone number as its name will be created in root directory of Tscraper `.` for example: **13412428592.session**

<br>

# ヅ Common Issues
If you get an error like this, `Server sent a very new message with ID xxxxxxxxxxxxxxxxxxx, ignoring`, just fix your device clock using ntpdate:
```bash
sudo ntpdate 0.pool.ntp.org && sudo hwclock -w
```
Don't act like a bot (like joining to many groups in short time), Telegram will ban your account, make sure to join groups with at least 60 seconds delay between each!

<br>

<h3 align="center">❦ Thanks for your support ❦</h3>
