import streamlit as st
from datetime import datetime

# Sample data
tweets = [
    {
        "user": "user1",
        "content": "This is the first tweet!",
        "time": datetime(2023, 6, 4, 14, 30)
    },
    {
        "user": "user2",
        "content": "Hello Twitter! #firstTweet",
        "time": datetime(2023, 6, 4, 15, 45)
    },
    {
        "user": "user3",
        "content": "Loving Streamlit for data apps!",
        "time": datetime(2023, 6, 4, 16, 10)
    }
]

# Streamlit App
st.title("Twitter Feed")
st.sidebar.title("Menu")
st.sidebar.write("Here you can add additional menu items.")

# Tweet input
st.subheader("Compose new Tweet")
new_tweet = st.text_area("What's happening?")
if st.button("Tweet"):
    if new_tweet:
        new_tweet_data = {
            "user": "current_user",
            "content": new_tweet,
            "time": datetime.now()
        }
        tweets.insert(0, new_tweet_data)
        st.success("Your tweet has been posted!")
    else:
        st.error("Tweet content cannot be empty.")

# Display tweets
st.subheader("Latest Tweets")
for tweet in tweets:
    st.write(f"**{tweet['user']}** - {tweet['time'].strftime('%Y-%m-%d %H:%M:%S')}")
    st.write(tweet['content'])
    st.markdown("---")