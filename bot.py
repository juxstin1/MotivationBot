import random

def get_motivational_quote():
    quotes = [
        "Believe you can and you're halfway there. —Theodore Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. —Confucius",
        "We may encounter many defeats but we must not be defeated. —Maya Angelou",
        "The only limit to our realization of tomorrow will be our doubts of today. —Franklin D. Roosevelt",
        "Everything you’ve ever wanted is on the other side of fear. —George Addair",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. —Winston Churchill",
        "What you get by achieving your goals is not as important as what you become by achieving your goals. —Zig Ziglar",
        "You don’t have to be great to start, but you have to start to be great. —Zig Ziglar",
        "It's not whether you get knocked down, it's whether you get up. —Vince Lombardi",
        "Your time is limited, don't waste it living someone else's life. —Steve Jobs",
        "The best way to predict the future is to invent it. —Alan Kay",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. —Albert Schweitzer",
        "Only I can change my life. No one can do it for me. —Carol Burnett",
        "Life is 10% what happens to us and 90% how we react to it. —Charles R. Swindoll",
        "The only limit to our realization of tomorrow is our doubts of today. —Franklin D. Roosevelt",
        "In the middle of difficulty lies opportunity. —Albert Einstein",
        "You miss 100% of the shots you don’t take. —Wayne Gretzky",
        "Life is what happens when you're busy making other plans. —John Lennon",
        "Dream big and dare to fail. —Norman Vaughan",
        "It always seems impossible until it is done. —Nelson Mandela",
        "The future belongs to those who believe in the beauty of their dreams. —Eleanor Roosevelt",
        "Keep your face always toward the sunshine—and shadows will fall behind you. —Walt Whitman",
        "The only way to do great work is to love what you do. —Steve Jobs",
        "Don't count the days, make the days count. —Muhammad Ali",
        "Every moment is a fresh beginning. —T.S. Eliot",
        "Do not wait to strike till the iron is hot; but make it hot by striking. —William Butler Yeats",
        "The journey of a thousand miles begins with one step. —Lao Tzu",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. —Christian D. Larson",
        "Success is stumbling from failure to failure with no loss of enthusiasm. —Winston Churchill",
        "I attribute my success to this: I never gave or took any excuse. —Florence Nightingale"
    ]
    
    # Select a random quote
    quote = random.choice(quotes)
    return quote

def display_quote():
    input("Press Enter for a new motivational quote or fortune:")
    print("Here is your motivational quote or fortune:")
    print(get_motivational_quote())

if __name__ == "__main__":
    while True:
        display_quote()
