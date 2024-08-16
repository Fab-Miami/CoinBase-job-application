# 🚀 Coinbase Job Applicator

Welcome to the "I Really, Really Want to Work at Coinbase" script!  
So, you've noticed that Coinbase is packed with job opportunities that scream your name, and you want to apply to all of them in record time? Say no more.
Introducing this little Python thing that will turbocharge your job application process at Coinbase, because manually filling out forms is so 2010.

## 🤖 What This Script Does

This script is your personal job application assistant.
It's like having a very enthusiastic friend who really wants you to work at Coinbase, but doesn't get tired or make typos. Here's what it does:

1. Fills out job applications faster than you can say "blockchain"
2. Uploads your resume and cover letter (because who doesn't love a good cover letter?)
3. Answers all those pesky questions about your experience with Coinbase products
4. Handles both single URL applications and bulk applications from a list
5. Gives you a chance to review before submitting, in case you want to add a joke or two

## 🛠️ Prerequisites

Before you embark on this automated job-seeking adventure, make sure you have:

- Python (preferably a version that's not old enough to apply for jobs itself)
- Selenium (because we're not savages who manually click buttons)
- ChromeDriver (make sure it's the right version, or things get weird)
- A burning desire to work at Coinbase (optional, but recommended)

## 🚀 How to Use

1. Clone this repo (or just copy-paste the code, we won't judge)
2. Install the required packages:
   ```
   pip install requirements.txt
   ```
3. Update the constants at the top of the script with your personal info.
4. Run the script:
   ```
   python coinbase_applicator.py
   ```
5. Choose your mode:
   - "One by one URL mode" for when you're feeling picky
   - "URL list mode" for when you're feeling ambitious
6. The script will pull the first job URL from the list and start the application process.
7. Review the application before submitting, DON'T CLICK ON THE SUBMIT BUTTON, instead click return in your terminal.
8. The script will then add "#" in front of the applied job in url_list.txt and move on to the next job URL in the list, and so on.

## 🎭 Features

- **Two Exciting Modes**: Choose between applying to jobs one at a time (for the cautious) or in bulk (for the brave).
- **Automatic Form Filling**: Because filling out form for the 100th time is nobody's idea of fun (even with browther prefill, trus me).
- **Resume and Cover Letter Upload**: Automatically uploads your documents, saving you precious seconds you could spend dreaming about your future Coinbase job.
- **Smart Dropdown Handling**: It selects options from dropdowns like a pro. It's basically a sommelier, but for job applications.
- **Duplicate Job ID Check**: Prevents you from accidentally applying to the same job twice, because enthusiasm is good, but desperation is not.

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