# 🚀 Coinbase Job Applicator

Welcome to the "I Really, Really Want to Work at Coinbase" script!  
So, you've noticed that Coinbase is packed with job opportunities that scream your name, and you want to apply to all of them in record time? I can help 😊<br><br>
Introducing this little Python script that will turbocharge your job application process, because manually filling out forms is so 2010.

## 🤖 What This Script Does

This script is your personal job application assistant.
It's like having a very enthusiastic friend who really wants you to work at Coinbase, but doesn't get tired or make typos. Here's what it does:

1. Fills out job applications faster than you can say "blockchain"
2. Uploads your resume and cover letter (because who doesn't love a good cover letter to confirm you really want this job?)
3. Answers all those pesky questions about your experience with Coinbase products and other things
4. Handles both single URL applications and bulk applications from a list
5. Gives you a chance to review before submitting, in case you want to add a joke or two

## 🛠️ Prerequisites

Before you embark on this automated job-seeking adventure, make sure you have:

- Python (preferably a version that's not too old)
- The things included in the requirements.txt file (see below)
- ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)
- A burning desire to work at Coinbase (optional, but recommended)

## 🎭 Features

- **Two Exciting Modes**: Choose between applying to jobs one at a time (for the cautious) or in bulk (for the brave).
- **Automatic Form Filling**: Because filling out form for the 100th time is nobody's idea of fun (even with browther prefill, trus me).
- **Resume and Cover Letter Upload**: Automatically uploads your documents, saving you precious seconds you could spend dreaming about your future Coinbase job.
- **Smart Dropdown Handling**: It selects options from dropdowns like a pro. It's basically a sommelier, but for job applications.
- **Duplicate Job ID Check**: Prevents you from accidentally applying to the same job twice, because enthusiasm is good, but desperation is not.

## 🚀 How to Use

1. Clone this repo (or just copy-paste the code, we won't judge)
2. Install the required packages:
   ```
   python -m venv .venv
   pip install requirements.txt
   ```
3. Update the constants at the top of the script with your personal info.
4. Add the job URLs you want to apply to in the `url_list.txt` file.
   ```
   https://www.coinbase.com/careers/positions/1234567
   https://www.coinbase.com/careers/positions/7654321
   etc...
   ```
5. Run the script:
   ```
   python coinbase_applicator.py
   ```
6. Choose your mode:
   - "One by one URL mode". Doesn't use the URL list, just prompts you to enter the URL
   - "URL list mode". Make sure you prefilled the `url_list.txt` file with the job URLs you want to apply to.
7. The script will pull the first job URL from the list and start the application process.
8. Review the application before submitting, DON'T CLICK ON THE SUBMIT BUTTON, instead click return in your terminal.
9. The script will then add "#" in front of the applied job in url_list.txt and move on to the next job URL in the list, and so on.

## ⚠️ Disclaimer

This script is for educational purposes only. Please use responsibly and in accordance with Coinbase's application policies. I am not responsible if you end up with 50 job offers and can't decide which one to take.

## 🤔 FAQs

Q: Will this guarantee me a job at Coinbase?
A: About as much as buying Bitcoin guarantees you'll be rich. Results may vary.

Q: What if I actually get an interview?
A: Congratulations! Unfortunately, we haven't automated that part yet. You're on your own there, champ.

Q: Is it okay to use this?
A: We recommend checking with Coinbase's HR department. When in doubt, stick to the old-fashioned way of applying – it builds character!

## 🎉 Good Luck!

May your applications be plentiful and your callbacks swift. Remember, in the world of crypto, persistence is key – both in mining and in job hunting!

Happy applying, and may the odds be ever in your favor! 🍀