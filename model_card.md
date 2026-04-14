# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder Lite

---

## 2. Intended Use

This recommender suggests a small set of songs from a classroom dataset based on a listener's stated genre, mood, energy, and acoustic preference. It is meant for experimentation and explanation, not for real user-facing recommendations.

## Non-Intended Use

This is not a model for real listeners or production music apps. It should not be used to judge a person's taste, predict emotions, or make business decisions.

---

## 3. How the Model Works

The model compares each song to the user's preferences and gives points for matches. Genre is worth 1.0 point, mood is worth 1.0 point, energy is scored by closeness to the target energy, and acousticness can add a small bonus when it fits the user's preference. The final score is the sum of those parts, and the highest-scoring songs are ranked first. I changed the starter logic by making the energy feature much more important than before, so songs near the user's target energy move up quickly.

---

## 4. Data

The catalog contains 10 songs. It includes pop, lofi, rock, ambient, jazz, indie pop, and synthwave, but the dataset is still small and leans toward chill or mainstream styles. I did not add or remove songs during this phase. Some kinds of musical taste are missing, especially more experimental, non-English, or heavily niche genres.

---

## 5. Strengths

The recommender works well when a user has a clear vibe in mind, such as happy pop, chill lofi, or intense rock. It also gives explanations that are easy to understand because the score is broken into named reasons. In the profiles I tested, the top results usually matched my intuition about the mood and energy of the songs.

---

## 6. Limitations and Bias

The system still relies on a small set of explicit labels, so it can miss songs that feel right even when they do not match the exact genre or mood strings. Because the catalog is tiny, it can repeat similar songs or artists and make the list feel narrow. The energy score is symmetric around the user's target, which means songs above and below the target can get the same reward even when a listener would not experience them the same way. The dataset also leans heavily toward pop, lofi, and chill-style music, so users with other tastes may see less variety. That can create a filter bubble where the recommender keeps circling safe matches instead of exploring.

---

## 7. Evaluation

I tested three profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. I checked whether the top results matched the vibe of each profile and whether the same songs kept appearing no matter what I asked for. The results mostly made sense: the lofi profile favored slower, more acoustic songs, and the rock profile pushed Storm Runner to the top because it matched genre, mood, and high energy. What surprised me was how strongly the energy weight affected the ranking after the experiment, because it let some songs rise even when they did not match genre. That showed the model is sensitive to weighting choices, which is useful for experimentation but also a sign that a single feature can dominate too easily.

---

## 8. Future Work

If I had more time, I would add more songs, include more user preferences, and improve diversity in the top results. I would also try a better energy formula that treats too-high and too-low energy differently, instead of only using one distance score.

I would also test a softer genre weight so one label does not dominate every ranking.

---

## 9. Personal Reflection

My biggest learning moment was seeing how much the rankings changed when I changed just one weight. The AI tools helped me move faster and think through the logic, but I still had to check the output carefully because a small prompt mistake or weight change could affect the whole result. I was surprised that such a simple scoring system could still feel like a real recommender when the top songs matched the user's vibe. If I extended this project, I would add more songs, make the scoring less rigid, and test whether the recommender can stay diverse.